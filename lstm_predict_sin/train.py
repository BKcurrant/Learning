# 执行训练并预测

import tensorflow as tf

from make_data import *
from define_lstm_model import lstm_model



def train_sin(sess, train_X, train_y):
    # 将训练数据以数据集的方式提供给计算图。
    ds = tf.data.Dataset.from_tensor_slices((train_X, train_y))
    ds = ds.repeat().shuffle(1000).batch(BATCH_SIZE)
    X, y = ds.make_one_shot_iterator().get_next()

    # 调用模型，得到预测结果、损失函数，和训练操作。
    with tf.variable_scope("model"):
        _, loss, train_op = lstm_model(X, y, True)

        sess.run(tf.global_variables_initializer())

        # 训练模型。
        for i in range(TRAINING_STEPS):
            _, l = sess.run([train_op, loss])
            if i % 1000 == 0:
                print("train step: " + str(i) + ", loss: " + str(l))

