import tensorflow as tf

# 通过name scope的方式来组织节点，并利用TensorBoard来可视化


with tf.name_scope("scope_A"):
  a = tf.add(1, 2,name="A_add")
  b = tf.multiply(a, 3,name="A_mul")

with tf.name_scope("scope_B"):
  c = tf.add(4, 5,name="B_add")
  d = tf.multiply(c, 6,name="B_mul")

e = tf.add(b,d,name="output")
print(e)

# write a graph to disk

writer = tf.summary.FileWriter('./name_scope_1',graph=tf.get_default_graph())
writer.close()


# 运行此文件后，再接着在终端中启动TensorBoard
