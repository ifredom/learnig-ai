
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import xlrd
import os
import random
from sklearn.utils import check_random_state

# NumPy(Numerical Python) 是 Python 语言的一个扩展程序库，
# 支持大量的维度数组与矩阵运算，此外也针对数组运算提供大量的数学函数库。

# xlrd 是 Python 语言的一个扩展程序库，
# 支持对Excel表格操作

# lineModel是用来分析随机变量分布，并拟合方差的统计学方法。
# 开始之前，首先需要有数据，这里先不使用随机数，使用有序数据。

# Generating artificial data.
n = 50
XX = np.arange(n)  # 创建一个数组，并赋值 从0到49
print(XX)
rs = check_random_state(0)  # 设置随机种子

# randint(a, b,size) 用来生成[a, b]之间的随意整数，包括两个边界值。size 个数不指定，默认为一个
#  生成一个随机数，并给每一个值加上2.0 * XX  在这里： y = a + bx
YY = rs.randint(-10, 10, size=(n,)) + 2.0 * XX

# stack()堆叠数组.
# 参考资料：https://blog.csdn.net/csdn15698845876/article/details/73380803
data = np.stack([XX, YY], axis=1)

# 模型训练次数，默认值：50
num_epochs = 60

# 创建两个变量，权重和偏差，初始值设置为0
W = tf.Variable(0.0, name="weights")
b = tf.Variable(0.0, name="bias")


####################
##### 必要功能 #####
###################

#  创建占位符 X 和 Y
def inputs():
    """
    定义place_holders。
        返回:
        返回数据和标签位置保持器。
    """
    X = tf.placeholder(tf.float32, name="X")
    Y = tf.placeholder(tf.float32, name="Y")
    return X, Y

# 创建预测
# 输入X,返回 X*W + b


def inference(X):
    return X * W + b

# 损失函数
# 通过将预测值与实际值进行比较来计算损失。X输入值，Y实际值，返回损失值。


def loss(X, Y):
    # 开始预测
    Y_predicted = inference(X)
    return tf.reduce_sum(tf.squared_difference(Y, Y_predicted))/(2*data.shape[0])

# 训练方法


def train(loss):
    learning_rate = 0.0001
    return tf.train.GradientDescentOptimizer(learning_rate).minimize(loss)


with tf.Session() as sess:

    # 初始化变量[w 和 b].
    sess.run(tf.global_variables_initializer())

    # 获取输入张量
    X, Y = inputs()

    # 返回损失值，以及创建训练operator.
    train_loss = loss(X, Y)
    train_op = train(train_loss)

    # Step 8: 训练模型
    for epoch_num in range(num_epochs):
        loss_value, _ = sess.run([train_loss, train_op],  feed_dict={X: data[:, 0], Y: data[:, 1]})

        # 打印每一个时间点的损失值
        print('epoch %d, loss=%f' % (epoch_num+1, loss_value))

        # 保存权重和偏差
        wcoeff, bias = sess.run([W, b])

########################
#### 评估和绘图. ########
#### matplotlib 这个库，将他作为一个专门用来绘制图形的库来看待 ########
########################
Input_values = data[:, 0]
Labels = data[:, 1]
Prediction_values = data[:, 0] * wcoeff + bias

# 绘图方法
plt.plot(Input_values, Labels, 'ro', label='main')
plt.plot(Input_values, Prediction_values, label='Predicted')

# 保存结果
plt.legend()
plt.show()
plt.close()

# 参考文档
# 源代码位置 https://github.com/machinelearningmindset/TensorFlow-Course/blob/master/codes/ipython/2-basics_in_machine_learning/linear_regression/code/linear_regression.ipynb
# sklearn文档 https://scikit-learn.org/stable/auto_examples/plot_isotonic_regression.html

# 类似介绍 https://blog.csdn.net/qq_14905099/article/details/49908089
