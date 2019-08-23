# 预测正弦函数

import tensorflow as tf
from make_data import *
from train import train_sin
from test import run_eval


with tf.Session() as sess:
    # 使用训练好的模型对测试数据进行预测。
    train_sin(sess, train_X, train_y)
    print("Evaluate model after training.")
    run_eval(sess, test_X, test_y)


