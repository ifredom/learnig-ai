import tensorflow as tf

# Create a new grapph
g1 = tf.Graph()
# Create a new grapph
g2 = tf.Graph()

with g1.as_default():
  # multiply 加法运算
  a = tf.add(1, 2)
sess = tf.Session(graph = g1)
r1 = sess.run(a)
print(r1)


with g2.as_default():
  # multiply 乘法运算
  b = tf.multiply(1, 2)  
sess = tf.Session(graph = g2)
r2 = sess.run(b)
print(r2)

