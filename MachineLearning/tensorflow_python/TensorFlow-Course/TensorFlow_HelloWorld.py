

from __future__ import print_function
import tensorflow as tf
import os

# Defining some sentence!
welcome = tf.constant('Welcome to TensorFlow world!')

# Run the session
with tf.Session() as sess:
    print("output: ", sess.run(welcome))


# Closing the session.
sess.close()