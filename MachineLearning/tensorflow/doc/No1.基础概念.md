# tensorflow学习1

http://www.tensorfly.cn/tfdoc/get_started/basic_usage.html
使用 TensorFlow, 你必须明白 TensorFlow:


使用图 (graph) 来表示计算任务.
在被称之为 会话 (Session) 的上下文 (context) 中执行图.
使用 tensor 表示数据.
通过 变量 (Variable) 维护状态.
使用 feed 和 fetch 可以为任意的操作(arbitrary operation) 赋值或者从其中获取数据.

## tf.Session是什么


## numpy

## 其他

* __future__ 是为了让python2平滑过渡到py3的一个工具集
* tf.add 和 tf.divide 方法未来会被废弃，使用 tf.math.add 和 tf.math.divide