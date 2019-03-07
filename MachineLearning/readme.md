# tensorflow是什么

* 哲学三问：是什么？ 为什么？怎么办？

* tensorflow 文件，记录使用python进行学习的`主要过程`，

* tensorflowJs里含有使用js学习tensofflow的过程中做的一些demo

> [tensorflow中文API文档](https://www.tensorflow.org/guide?hl=zh-cn)

## 学习方法

> 学习tensorflow还是需要不少知识前置的。只是，先对tensoflow整体脉络是什么，有什么用做一个清楚的认识，然后的找一个教程开始学习。
> 需要哪里,再去查询学习哪里。
> 项目首页 有对人工智能-->机器学习-->深度学习-->tensorflow 的介绍

## 学习顺序

> 根据 TensorFlow-Course 教程[](https://github.com/machinelearningmindset/TensorFlow-Course)开始学习

1. 2019-02-23 学习了 `tensorflow_python\TensorFlow-Course\part1` 和 `tensorflow_python\TensorFlow-Course\part2`. 学习过程中，发现对pthon基础操作了解的不够。然后在[廖雪峰大佬的python教程](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000)这里，巩固了`python基础` 和`高级特性`，代码练习写在`pthon/basic` ，

2. 2019-02-25 接下来发现要学习 TensorFlow-Course 教程的part3部分，需要对tensorflow的基础 Tensor(张量) Variable(变量)  Session(会话) Graph(图表) 这些基础知识有更深入的了解，所以先去巩固这个基础。其中，谷歌搜索`如何学习tensor`和`如何学习graph`，伴随查看[tensorflowAPI](https://www.tensorflow.org/guide/tensors?hl=zh-cn)这里,将这几个低阶API基础都完整理解一遍。

3. 2019-02-27 接下来发现要学习 TensorFlow-Course 教程的part4部分,总算要开始运行第一个模型：线性回归。发现需要补充数学知识。google搜索内容，学习过程为：什么是线性回归？--> 什么是简单回归?-->什么是最小二乘法-->什么是正态分布？-->什么是标准正态分布？-->什么是标准差/中位数/众数/概率密度函数 --> 线性回归 -->多项式回归。代码写在 `tensorflow_python\TensorFlow-Course\part3-lineModel`

4. 2019-03-01 接上一次学习，将那些`高中数学知识`重新温习巩固了一遍，然后开始写第一个模型，也是最简单的模型：线性回归。[直接复制参考代码](https://github.com/machinelearningmindset/TensorFlow-Course/blob/master/codes/python/2-basics_in_machine_learning/linear_regression/code/linear_regression.py)。代码写在 `tensorflow_python\TensorFlow-Course\part3-lineModel`

5. 2019-03-05 上一次`part3-lineModel.py`的代码成功运行了，但是为了理解里面的每一行代码（都是使用的最常用的库），需要谷歌搜索`什么是随机种子？stack()这个方法的用法？什么是权重(A)和偏差(B)（y=Ax+B）？matplotlib这个库是做什么用的?`.这里需要注意的是matplotlib只需要知道他是绘图用的，暂时不必理会里面那一堆API.
