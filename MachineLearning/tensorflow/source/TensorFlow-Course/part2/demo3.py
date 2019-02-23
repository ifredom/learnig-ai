# demo3演示：如何定义变量并初始化它们
import tensorflow as tf
from tensorflow.python.framework import ops

# 创建变量，并设置一些默认值.
# weights： 权重   biases：偏差 ：custom：自定义
weights = tf.Variable(tf.random_normal([2, 3], stddev=0.1), name="weights")
biases = tf.Variable(tf.zeros([3]), name = "biases")
custom_variable = tf.Variable(tf.zeros([3]), name = "custom")

# 获取所有变量的张量并将它们存储在一个列表中。
all_variables_list = ops.get_collection(ops.GraphKeys.GLOBAL_VARIABLES)

# variable_list_custom 定义为我们想要初始化的变量列表.
variable_list_custom = [weights, custom_variable]

# 初始化.必须在模型中的所有其他操作之前运行变量
init_custom_op = tf.variables_initializer(var_list = variable_list_custom)

# 全局初始化
# 方式一。创建一个节点来初始化变量
init_all_op = tf.global_variables_initializer()

# 方式二。
init_all_op = tf.variables_initializer(var_list = all_variables_list)

# ### 初始化使用其他变量
# 创建另一个与 weights 具有相同值的变量。
WeightsNew = tf.Variable(weights.initialized_value(), name = "WeightsNew")

# 现在，必须初始化变量。
init_WeightsNew_op = tf.variables_initializer(var_list = [WeightsNew])

# ### Running the session
with tf.Session() as sess:
    # 运行初始化程序操作。
    print(sess.run(init_all_op))
    print(sess.run(init_custom_op))
    print(sess.run(init_WeightsNew_op))


def logs(content):
    print(content)
