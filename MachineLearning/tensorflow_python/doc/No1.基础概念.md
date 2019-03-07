# tensorflow中的必须知道的一些基础概念

使用 TensorFlow, 必须明白 TensorFlow的是如何整体运作的，其中：

* 使用图 (graph) 来表示计算任务.在被称之为 会话 (Session) 的上下文 (context) 中执行图.
* 使用 tensor 表示数据.
* 通过 变量 (Variable) 维护状态.
* 使用 feed 和 fetch 可以为任意的操作(arbitrary operation) 赋值或者从其中获取数据.

> 基础概念学习完成后补充.

## 综述

TensorFlow 是一个编程系统, 使用图来表示计算任务.
 图中的节点被称之为 op (operation 的缩写). 一个 op 获得 0 个或多个 Tensor, 执行计算, 产生 0 个或多个 Tensor. 每个 Tensor 是一个类型化的多维数组. 例如, 你可以将一小组图像集表示为一个四维浮点数数组, 这四个维度分别是 [batch, height, width, channels].

一个 TensorFlow 图描述了计算的过程. 为了进行计算, 图必须在 会话 里被启动. 会话 将图的 op 分发到诸如 CPU 或 GPU 之类的 设备 上, 同时提供执行 op 的方法. 这些方法执行后, 将产生的 tensor 返回. 在 Python 语言中, 返回的 tensor 是 numpy ndarray 对象; 在 C 和 C++ 语言中, 返回的 tensor 是 tensorflow::Tensor 实例.

## 图 (graph) 是什么？

## Session 是什么？

## 节点 (operation) 是什么？

一个节点。包含了一堆操作表达式

## 变量 (Variable) 是什么？

## feed和 fetch  操作 是什么？




## 其他

* __future__ 是为了让python2平滑过渡到py3的一个工具集
* tf.add 和 tf.divide 方法未来会被废弃，使用 tf.math.add 和 tf.math.divide


### TensorBoard

安装tensorflow的时候，会自动安装TensorBoard.
TensorBoard 是一套专门用来展现 TensorFlow 图的可视化工具，绘制图像生成的定量指标图以及显示附加数据

启动命令

```bash
tensorboard --logdir=path/to/log-directory
```

启动后，会给出一个访问地址，默认端口是6006.浏览器访问 `http://localhost:6006`即可看到效果

### 参考资料

[文档介绍]（http://www.tensorfly.cn/tfdoc/get_started/basic_usage.html）