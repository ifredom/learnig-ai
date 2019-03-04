# 什么是线性回归？

在统计学中，线性回归（Linear regression）是利用称为线性回归方程的最小二乘函数对一个或多个自变量和因变量之间关系进行建模的一种回归分析。

## 什么是回归分析[统计学]

回归分析（regression analysis)是确定两种或两种以上变量间相互依赖的定量关系的一种统计分析方法。

## 什么是正态分布[高中数学]

[google搜索wiki](https://zh.wikipedia.org/wiki/%E6%AD%A3%E6%80%81%E5%88%86%E5%B8%83)
标准正态分布又称为u分布，是以0为均数、以1为标准差的正态分布，记为N（0，1）
期望值μ=0，即曲线图象对称轴为Y轴，标准差σ=1  

* 读音： μ(miu 四声) σ(西格玛)
* 标准差：在概率统计中最常使用作为测量一组数值的离散程度之用。标准差定义：为方差开算术平方根，反映组内个体间的离散程度；标准差与期望值之比为标准离差率
* 方差：σ^2= ∑（X- X_）^2 / （N-1）.其中 σ^2为总体方差，X为变量，X_为总体平均值，N为样本总数。
* 中位数（又称中值，Median），统计学中的专有名词，代表一个样本、种群或概率分布中的一个数值，中位数：将一组数据按大小顺序排列，处在最中间位置的一个数叫做这组数据的中位数。
对于有限的数集，可以通过把所有观察值高低排序后找出正中间的一个作为中位数。如果观察值有偶数个，通常取最中间的两个数值的平均数作为中位数。、
* 中位数与平均数区别。 平均数：一组数据的总和除以这组数据个数所得到的商叫这组数据的平均数。
* 众数（mode）指一组数据中出现次数最多的数据值

### 概率密度函数

* 正态分布的概率密度函数均值为 μ, 方差为 σ^2 (或标准差 σ)是高斯函数的一个实例.

* 连续型随机变量的概率密度函数（Probability density function）（在不至于混淆时可以简称为密度函数）是一个描述这个随机变量的输出值，在某个确定的取值点附近的可能性的函数。

### 累积分布函数

累积分布函数，又叫分布函数，是概率密度函数的积分，能完整描述一个实随机变量X的概率分布

## 什么是最小二乘法?

[wiki百科](https://zh.wikipedia.org/wiki/%E6%9C%80%E5%B0%8F%E4%BA%8C%E4%B9%98%E6%B3%95)

### 数学知识拓展

* 中位数定义：一组数据按从小到大的顺序依次排列，处在中间位置的一个数（或最中间两个数据的平均数，注意：和众数不同，中位数不一定在这组数据中）。
中位数的优缺点：中位数是样本数据所占频率的等分线，它不受少数几个极端值得影响，有时也会成为优点。

* 平均数是指在一组数据中所有数据之和再除以数据的个数。平均数是统计中的一个重要概念。小学数学里所讲的平均数一般是指算术平均数，也就是一组数据的和除以这组数据的个数所得的商。

* 平均数的优缺点：平均数是表示一组数据集中趋势的量数，它是反映数据集中趋势的一项指标。它受少数几个极端值得影响。


### 伪随机数 和随机种子

> 计算机中的随机数是由随即种子和特定的计算方法生成的。

[参考资料](https://blog.csdn.net/xzp7772009/article/details/7849030)