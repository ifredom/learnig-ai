# tensorflowapi中文翻译

自己翻译的版本

## 调用方法

定义于tensorflow/python/layers/core.py。密集连接层的功能接口。

```bash
tf.layers.dense(
    inputs,
    units,
    activation=None,
    use_bias=True,
    kernel_initializer=None,
    bias_initializer=tf.zeros_initializer(),
    kernel_regularizer=None,
    bias_regularizer=None,
    activity_regularizer=None,
    kernel_constraint=None,
    bias_constraint=None,
    trainable=True,
    name=None,
    reuse=None
)
```

该层实现了操作： outputs = activation(inputs * kernel + bias) 其中activation作为activation 参数传递的激活函数（如果不是None），kernel是由图层创建的权重矩阵，并且bias是由图层创建的偏向量（仅当use_bias是True）。

> 参数：
inputs：张量输入。
units：整数或长整数，输出空间的维数。
activation：激活功能（可调用）。将其设置为“无”以保持线性激活。
use_bias：Boolean，该层是否使用偏差。
kernel_initializer：权重矩阵的初始化函数。如果None（默认），使用默认初始化程序初始化权重tf.get_variable。
bias_initializer：偏置的初始化函数。
kernel_regularizer：权重矩阵的正则化函数。
bias_regularizer：正规函数的偏差函数。
activity_regularizer：输出的正则化函数。
kernel_constraint：由a更新后应用于内核的可选投影函数Optimizer（例如，用于实现层权重的范数约束或值约束）。该函数必须将未投影的变量作为输入，并且必须返回投影变量（必须具有相同的形状）。在进行异步分布式培训时，使用约束是不安全的。
bias_constraint：由a更新后应用于偏置的可选投影函数Optimizer。
trainable：Boolean，如果True还将变量添加到图集合中 GraphKeys.TRAINABLE_VARIABLES（请参阅参考资料tf.Variable）。
name：String，图层的名称。
reuse：Boolean，是否以同一名称重用前一层的权重。
返回：
输出张量与inputs最后一个尺寸的大小相同units。