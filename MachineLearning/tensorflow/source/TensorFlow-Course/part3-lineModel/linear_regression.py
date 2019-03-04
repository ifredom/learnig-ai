
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

# randint(a, b) 用来生成[a, b]之间的随意整数，包括两个边界值。
#  生成一个随机数，  在这里： y = a + bx
YY = rs.randint(-10, 10, size=(n,)) + 2.0 * XX  

# stack()堆叠数组
# 参考资料：https://blog.csdn.net/csdn15698845876/article/details/73380803
data = np.stack([XX, YY], axis=1)

num_epochs = 50

# creating the weight and bias.
# The defined variables will be initialized to zero.
W = tf.Variable(0.0, name="weights")
b = tf.Variable(0.0, name="bias")


###############################
##### Necessary functions #####
###############################

#  Creating placeholders for input X and label Y.
def inputs():
    """
    Defining the place_holders.
    :return:
            Returning the data and label place holders.
    """
    X = tf.placeholder(tf.float32, name="X")
    Y = tf.placeholder(tf.float32, name="Y")
    return X, Y

# Create the prediction.


def inference(X):
    """
    Forward passing the X.
    :param X: Input.
    :return: X*W + b.
    """
    return X * W + b


def loss(X, Y):
    '''
    compute the loss by comparing the predicted value to the actual label.
    :param X: The input.
    :param Y: The label.
    :return: The loss over the samples.
    '''

    # Making the prediction.
    Y_predicted = inference(X)
    return tf.reduce_sum(tf.squared_difference(Y, Y_predicted))/(2*data.shape[0])


# The training function.
def train(loss):
    learning_rate = 0.0001
    return tf.train.GradientDescentOptimizer(learning_rate).minimize(loss)


with tf.Session() as sess:

    # Initialize the variables[w and b].
    sess.run(tf.global_variables_initializer())

    # Get the input tensors
    X, Y = inputs()

    # Return the train loss and create the train_op.
    train_loss = loss(X, Y)
    train_op = train(train_loss)

    # Step 8: train the model
    for epoch_num in range(num_epochs):
        loss_value, _ = sess.run([train_loss, train_op],
                                 feed_dict={X: data[:, 0], Y: data[:, 1]})

        # Displaying the loss per epoch.
        print('epoch %d, loss=%f' % (epoch_num+1, loss_value))

        # save the values of weight and bias
        wcoeff, bias = sess.run([W, b])

###############################
#### Evaluate and plot ########
###############################
Input_values = data[:,0]
Labels = data[:,1]
Prediction_values = data[:,0] * wcoeff + bias

# uncomment if plotting is desired!
plt.plot(Input_values, Labels, 'ro', label='main')
plt.plot(Input_values, Prediction_values, label='Predicted')

# Saving the result.
plt.legend()
plt.show()
plt.close()

# 参考文档
# 源代码位置 https://github.com/machinelearningmindset/TensorFlow-Course/blob/master/codes/ipython/2-basics_in_machine_learning/linear_regression/code/linear_regression.ipynb
# sklearn文档 https://scikit-learn.org/stable/auto_examples/plot_isotonic_regression.html

# 类似介绍 https://blog.csdn.net/qq_14905099/article/details/49908089
