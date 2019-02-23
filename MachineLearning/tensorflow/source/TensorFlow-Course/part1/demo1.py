# demo1 用于演示tensorflow基本的运行过程，
# 过程：如何输入Tensor(张量)，如何输出结果 result = sess.run(a)，以及op必须运行于session(会话)当中
# 在这里a,b是tensor(张量)
# sess = tf.Session() ,sess是会话

import tensorflow as tf
import os
# 这一句的作用查看问题集合： AVX2
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


a = tf.constant(5.0, name="a")
b = tf.constant(10.0, name="a")

# Some basic operations
x = tf.add(a, b, name="add")
y = tf.div(a, b, name="divide")

# Launch the graph in a session.
with tf.Session() as sess:
    print("a =", sess.run(a))
    print("b =", sess.run(b))
    print("a + b =", sess.run(x))
    print("a/b =", sess.run(y))

# 关闭摘要编辑器
sess.close()

# 运行
# python demo1.py