# tf.Variable(initializer， name)

```python
# initializer 是初始化参数，可以有 tf.random_normal，tf.constant，tf.constant等，是将一个 tensor 传递给 Variable() 构造函数
# name 就是变量的名字，用法如下:
tf.Variable(initializer， name)
```

## 深入剖析tf.Variable这个核心概念顺序

1.图变量的初始化方法
2.两种定义图变量的方法
3.scope如何划分命名空间
4.图变量的复用
5.图变量的种类