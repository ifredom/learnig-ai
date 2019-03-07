import tensorflow as tf


# 进入一个交互式 TensorFlow 会话.
# sess = tf.InteractiveSession()

state = tf.Variable(3, name="counter")
one = tf.constant(1, name="one")
print(state.name)

new_value = tf.add(state, one)
update = tf.assign(state, new_value)
print(new_value)
print(update)

# 初始化所有全局变量，并添加到默认graph图中
init = tf.global_variables_initializer()

# print(state.eval())

with tf.Session()as sess:
  print(sess.run(init))
  for _ in range(3):
    sess.run(update)
    print(sess.run(state))

# 参考资料 
# https://morvanzhou.github.io/tutorials/machine-learning/tensorflow/2-4-variable/
# 其中初始化不一样
