#!/usr/bin/env python
# coding: utf-8

# 迁移学习，将一个问题上训练好的模型通过简单的调整使其适用于一个新问题。在数据量足够的情况下，迁移学习的效果不如完全重新训练。但是迁移学习的所需训练时间和训练样本数远小于训练完整模型。
# 这里是利用ImageNet数据集上训练好的Inception-v3模型来解决一个新的图像分类问题。
# 保留模型中所有卷积层参数，替换最后一层全连接层。
# 最后一层全连接层之前的网络成称之为瓶颈层。将新的图像通过训练好的的卷积神经网络直接到瓶颈层的过程可以看成是对图像进行特征提取的过程。在训练好的Inception-v3模型中，因为瓶颈层的输出再通过一个单层的全连接层神经网络可以很好地区分1000中类别的图像，所以有理由认为瓶颈层的输出的节点向量可以被作为任何图像的一个更加精简且表达能力更强的特征向量。在新数据集上，可以直接利用这个训练好的神经网络对图像进行特征提取，然后再将提取得到的特征向量作为输入来训练一个新的单层全连接神经网络处理新的分类问题。

# # 下载数据

# In[1]:


# wget http://download.tensorflow.org/example_images/flower_photos.tgz
# tar xzf flower_photos.tgz

# wget http://download.tensorflow.org/models/inception_v3_2016_08_228.tar.gz
# inception_v3_2016_08_228.tar.gz
#inception_v3.ckpt


# # 标定文件地址

# In[17]:


import glob
import os.path
import numpy as np
import tensorflow as tf
from tensorflow.python.platform import gfile

# 原始输入数据的目录，有5个子目录，每个子目录底下保存这属于该类别的所有图片。
INPUT_DATA = '../TS/datasets/flower_photos'

# 输出文件地址。整理后的图片数据通过numpy的格式保存。
OUTPUT_FILE = '../TS/datasets/flower_processed_data.npy'

# 测试数据和验证数据比例。
VALIDATION_PERCENTAGE = 10
TEST_PERCENTAGE = 10


# # 数据处理过程

# In[18]:


# 读取数据并将数据分割成训练数据、验证数据和测试数据。
def create_image_lists(sess, testing_percentage, validation_percentage):
    sub_dirs = [x[0] for x in os.walk(INPUT_DATA)]
    is_root_dir = True
    
    # 初始化各个数据集。
    training_images = []
    training_labels = []
    testing_images = []
    testing_labels = []
    validation_images = []
    validation_labels = []
    current_label = 0
    
    # 读取所有的子目录。
    for sub_dir in sub_dirs:
        if is_root_dir:
            is_root_dir = False
            continue

        # 获取一个子目录中所有的图片文件。
        extensions = ['jpg', 'jpeg', 'JPG', 'JPEG']
        file_list = []
        dir_name = os.path.basename(sub_dir)
        for extension in extensions:
            file_glob = os.path.join(INPUT_DATA, dir_name, '*.' + extension)
            file_list.extend(glob.glob(file_glob))
        if not file_list: continue
        print("processing:", dir_name)
        
        i = 0
        # 处理图片数据。
        for file_name in file_list:
            i += 1
            # 读取并解析图片，将图片转化为299*299以方便inception-v3模型来处理。
            image_raw_data = gfile.FastGFile(file_name, 'rb').read()
            image = tf.image.decode_jpeg(image_raw_data)
            if image.dtype != tf.float32:
                image = tf.image.convert_image_dtype(image, dtype=tf.float32)
            image = tf.image.resize_images(image, [299, 299])
            image_value = sess.run(image)
            
            # 随机划分数据聚。
            chance = np.random.randint(100)
            if chance < validation_percentage:
                validation_images.append(image_value)
                validation_labels.append(current_label)
            elif chance < (testing_percentage + validation_percentage):
                testing_images.append(image_value)
                testing_labels.append(current_label)
            else:
                training_images.append(image_value)
                training_labels.append(current_label)
            if i % 200 == 0:
                print(i, "images processed.")
        current_label += 1
    
    # 将训练数据随机打乱以获得更好的训练效果。
    state = np.random.get_state()#可理解为设定状态，记录下数组被打乱的操作
    np.random.shuffle(training_images)
    np.random.set_state(state)#接收get_state()返回的值，并进行同样的操作
    np.random.shuffle(training_labels)
#     解析numpy.random.get_state()和numpy.random.set_state()
#     get_state()：可理解为设定状态，记录下数组被打乱的操作
#     set_state()：接收get_state()返回的值，并进行同样的操作
#     一般结合random.shuffle()函数使用
#     将实例与标签两个数组同时打乱，但打乱后，实例与标签任然是一一对应的关系
 
    return np.asarray([training_images, training_labels,
                       validation_images, validation_labels,
                       testing_images, testing_labels])


# # 进行数据处理过程

# In[ ]:


with tf.Session() as sess:
    processed_data = create_image_lists(sess, TEST_PERCENTAGE, VALIDATION_PERCENTAGE)
    # 通过numpy格式保存处理后的数据。
    np.save(OUTPUT_FILE, processed_data)


# # 定义训练过程中将要使用到的数据

# In[7]:


import glob
import os.path
import numpy as np
import tensorflow as tf
from tensorflow.python.platform import gfile
import tensorflow.contrib.slim as slim

# 加载通过TensorFlow-Slim定义好的inception_v3模型。
import tensorflow.contrib.slim.python.slim.nets.inception_v3 as inception_v3

# 处理好之后的数据文件。
INPUT_DATA = '../TS/datasets/flower_processed_data.npy'
# 保存训练好的模型的路径。
TRAIN_FILE = 'train_dir/model'
# 谷歌提供的训练好的模型文件地址。因为GitHub无法保存大于100M的文件，所以
# 在运行时需要先自行从Google下载inception_v3.ckpt文件。
CKPT_FILE = '../TS/datasets/inception_v3.ckpt'

# 定义训练中使用的参数。
LEARNING_RATE = 0.0001
STEPS = 300
BATCH = 32
N_CLASSES = 5

# 不需要从谷歌训练好的模型中加载的参数。
CHECKPOINT_EXCLUDE_SCOPES = 'InceptionV3/Logits,InceptionV3/AuxLogits'
# 需要训练的网络层参数明层，在fine-tuning的过程中就是最后的全联接层。
TRAINABLE_SCOPES='InceptionV3/Logits,InceptionV3/AuxLogit'


# # 获取谷歌训练模型中的常量

# In[8]:


def get_tuned_variables():
    exclusions = [scope.strip() for scope in CHECKPOINT_EXCLUDE_SCOPES.split(',')]

    variables_to_restore = []
    # 枚举inception-v3模型中所有的参数，然后判断是否需要从加载列表中移除。
    for var in slim.get_model_variables():
        excluded = False
        for exclusion in exclusions:
            if var.op.name.startswith(exclusion):
                excluded = True
                break
        if not excluded:
            variables_to_restore.append(var)
    return variables_to_restore


# # 获取需要的训练的变量

# In[9]:


def get_trainable_variables():    
    scopes = [scope.strip() for scope in TRAINABLE_SCOPES.split(',')]
    variables_to_train = []
    
    # 枚举所有需要训练的参数前缀，并通过这些前缀找到所有需要训练的参数。
    for scope in scopes:
        variables = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES, scope)
        variables_to_train.extend(variables)
    return variables_to_train


# # 训练过程

# In[10]:


def main():
    # 加载预处理好的数据。
    processed_data = np.load(INPUT_DATA)
    training_images = processed_data[0]
    n_training_example = len(training_images)
    training_labels = processed_data[1]
    
    validation_images = processed_data[2]
    validation_labels = processed_data[3]
    
    testing_images = processed_data[4]
    testing_labels = processed_data[5]
    print("%d training examples, %d validation examples and %d testing examples." % (
        n_training_example, len(validation_labels), len(testing_labels)))

    # 定义inception-v3的输入，images为输入图片，labels为每一张图片对应的标签。
    images = tf.placeholder(tf.float32, [None, 299, 299, 3], name='input_images')
    labels = tf.placeholder(tf.int64, [None], name='labels')
    
    # 定义inception-v3模型。因为谷歌给出的只有模型参数取值，所以这里
    # 需要在这个代码中定义inception-v3的模型结构。虽然理论上需要区分训练和
    # 测试中使用到的模型，也就是说在测试时应该使用is_training=False，但是
    # 因为预先训练好的inception-v3模型中使用的batch normalization参数与
    # 新的数据会有出入，所以这里直接使用同一个模型来做测试。
    with slim.arg_scope(inception_v3.inception_v3_arg_scope()):
        logits, _ = inception_v3.inception_v3(
            images, num_classes=N_CLASSES, is_training=True)
    
    trainable_variables = get_trainable_variables()
    # 定义损失函数和训练过程。
    tf.losses.softmax_cross_entropy(
        tf.one_hot(labels, N_CLASSES), logits, weights=1.0)
    total_loss = tf.losses.get_total_loss()
    train_step = tf.train.RMSPropOptimizer(LEARNING_RATE).minimize(total_loss)
    
    # 计算正确率。
    with tf.name_scope('evaluation'):
        correct_prediction = tf.equal(tf.argmax(logits, 1), labels)
        evaluation_step = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
                
    # 定义加载Google训练好的Inception-v3模型的Saver。
    load_fn = slim.assign_from_checkpoint_fn(
      CKPT_FILE,
      get_tuned_variables(),
      ignore_missing_vars=True)
    
    # 定义保存新模型的Saver。
    saver = tf.train.Saver()
    
    with tf.Session() as sess:
        # 初始化没有加载进来的变量。
        init = tf.global_variables_initializer()
        sess.run(init)
        
        # 加载谷歌已经训练好的模型。
        print('Loading tuned variables from %s' % CKPT_FILE)
        load_fn(sess)
            
        start = 0
        end = BATCH
        for i in range(STEPS):            
            _, loss = sess.run([train_step, total_loss], feed_dict={
                images: training_images[start:end], 
                labels: training_labels[start:end]})

            if i % 30 == 0 or i + 1 == STEPS:
                saver.save(sess, TRAIN_FILE, global_step=i)
                
                validation_accuracy = sess.run(evaluation_step, feed_dict={
                    images: validation_images, labels: validation_labels})
                print('Step %d: Training loss is %.1f Validation accuracy = %.1f%%' % (
                    i, loss, validation_accuracy * 100.0))
                            
            start = end
            if start == n_training_example:
                start = 0
            
            end = start + BATCH
            if end > n_training_example: 
                end = n_training_example
            
        # 在最后的测试数据上测试正确率。
        test_accuracy = sess.run(evaluation_step, feed_dict={
            images: testing_images, labels: testing_labels})
        print('Final test accuracy = %.1f%%' % (test_accuracy * 100))


# In[11]:


if __name__ == '__main__':
    main()

