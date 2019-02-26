from __future__ import print_function
import tensorflow as tf
import os

# 通过name scope的方式来组织节点，并利用TensorBoard来可视化

gf = tf.Graph()
with gf.as_default():
    with tf.name_scope("scope_A"):
        a = tf.add(1, 2, name="A_add")
        b = tf.multiply(a, 3, name="A_mul")
        print(a.graph is tf.get_default_graph())  # 结果为True
        assert b.graph is gf

    with tf.name_scope("scope_B"):
        c = tf.add(4, 5, name="B_add")
        d = tf.multiply(c, 6, name="B_mul")

    e = tf.add(b, d, name="output")

# 将数据写入文件（磁盘）
writer = tf.summary.FileWriter('./logs_1', graph=gf)
writer.close()

# 运行此文件后,会生成一个文件夹 name_scope_1,里面包含一张图的数据
# >> python name_scope_graph.py

# 接着在终端中启动 TensorBoard
# >> tensorboard --logdir='./logs_1'
