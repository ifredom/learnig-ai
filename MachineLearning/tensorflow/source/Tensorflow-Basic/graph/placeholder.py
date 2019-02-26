import tensorflow as tf

# placeholder 类似于c++的cin，要求用户运行时输入
# 此函数可以理解为形参，用于定义过程，在执行的时候再赋具体的值

# tf.placeholder(dtype, shape=None, name=None)
# dtype：数据类型。常用的是tf.float32,tf.float64等数值类型
# shape：数据形状。默认是None，就是一维值，也可以是多维，比如[2,3], [None, 3]表示行不定,列是3，
# name：名称。

input1 = tf.placeholder(tf.float32, [2, 2])
input2 = tf.placeholder(tf.float32, [2, 2])

input3 = tf.placeholder(tf.float32)
input4 = tf.placeholder(tf.float32)

# 矩阵乘法
output1 = tf.matmul(input1, input2)
# 数字乘法
output2 = tf.multiply(input3, input4)

with tf.Session() as sess:
    # feed_dict 是关键字，必须写成这个名字，后面紧跟传入的参数
    print(sess.run(output1, feed_dict={
          input1: [[1, 2], [3, 4]], input2: [[1, 1], [1, 1]]}))
    print(sess.run(output2, feed_dict={input3: 3, input4: 4}))

