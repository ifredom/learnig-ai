import tensorflow as tf

# indefault graph
a = tf.add(1, 2)
sess = tf.Session()
r = sess.run(a)
print(r)

# Create a new grapph
g = tf.Graph()
with g.as_default():
  a = tf.add(3, 4)
sess = tf.Session(graph = g)
r1 = sess.run(a)
print(r1)
