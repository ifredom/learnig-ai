# 什么是graph(图)?

A Graph包含一组 tf.Operation对象，表示计算单位; 和 tf.Tensor对象，表示在操作之间流动的数据单元。

## 怎么创建与操作 graph

> graph 是由 Variable 和 Operation来组成的一个操作流图。

1. TF在library加载以后，会自动创建一个Graph对象，并把它作为default graph，我们创建的操作会自动放在这个default graph里。我们也可以不使用TF自动创建的graph，而是创建自己的graph对象并设置为default，然后添加各种操作，参见（`default_graph.py`）

2. 如果打算运行自己创建的graph，一定要把它传递给tf.Session的graph参数.参见（`self_graph.py`）

3. 在实际工作中，我们需要创建包含成百上千个节点的graph。如何有效的组织和查看graph就显得尤为重要。参见（`name_scope_graph.py`）,才考资料[graph讲解](https://www.jianshu.com/p/a5d725e90565)