---
type: concept
course: Machine Learning
priority: A
status: draft
aliases: []
related: []
---

# Loss Function

## 一句话定义

loss function 衡量单个样本的预测错误。它解决的是某一次预测错了多少，以及这个错误如何给梯度计算提供直接信号。

## 核心思想

模型输出 $\hat y$ 后，loss 把 $\hat y$ 和真实标签 $y$ 的差距变成可微或可优化的数值。多个样本的 loss 汇总为 [[cost-function]]，再由 [[gradient-descent]] 或 [[backpropagation]] 产生参数更新。

## 核心边界 / Objective / Assumption

loss 作用于单个样本，例如 $x^{(i)} \in \mathbb{R}^n$、标签 $y^{(i)}$、预测 $\hat y^{(i)}=f_\theta(x^{(i)})$。cost function 通常是多个 loss 的平均或总和，并可加入 regularization。loss 是反向传播或梯度计算的直接信号，但它不等同于最终业务指标。

## 模型假设 / 局限

loss 需要匹配任务和输出形式。回归可用 squared error；二分类概率更适合 logistic loss；多分类可用 softmax loss。如果 loss 选择不合适，optimization 可能仍然进行，但训练方向会偏离任务目标。对于不可微指标如 accuracy，通常需要可微 surrogate loss。

## 在 Machine Learning 中的位置

loss 位于模型预测和整体训练目标之间：model prediction → [[loss-function]] → [[cost-function]] → [[gradient-descent]]。在线性回归中它支撑 MSE；在分类和神经网络中，它决定错误信号如何通过 autograd/backpropagation 传播。

## 重要公式 / 算法

- 公式 / 算法名称：Squared Error Loss
- 解决的问题：衡量单个回归预测的误差。
- 核心含义：$L(\hat y,y)=\frac12(\hat y-y)^2$；$\hat y=f(x)$ 是预测，$y$ 是真实值，二者通常是标量。
- 相关概念链接：[[linear-regression]]、[[cost-function]]

- 公式 / 算法名称：Logistic Loss
- 解决的问题：衡量二分类概率预测错误。
- 核心含义：$L(f(x),y)=-y\log(f(x))-(1-y)\log(1-f(x))$；$y\in\{0,1\}$，$f(x)\in(0,1)$ 是预测为 1 的概率。
- 相关概念链接：[[logistic-regression]]、[[classification]]

- 公式 / 算法名称：Softmax Loss
- 解决的问题：衡量多分类中正确类别概率是否足够高。
- 核心含义：index.md 给出 $loss=-\ln(a_i)$ when $y=i$；$a_i$ 是正确类别的预测概率。
- 相关概念链接：[[softmax]]、[[classification]]

## 容易混淆点

- loss function vs cost function：loss 是单样本，cost 是整体目标。
- loss function vs accuracy：loss 可连续指导优化，accuracy 通常不可直接求梯度。
- logistic loss vs squared error：分类概率更适合交叉熵，不适合直接套平方误差。
- loss vs regularization：regularization 惩罚参数，不是样本预测误差本身。

## 相关概念

- [[cost-function]]
- [[gradient-descent]]
- [[classification]]
- [[linear-regression]]
- [[backpropagation]]

## 跨课程连接

- CS61A：loss 是单个输入输出对上的错误函数。
- CS61B：训练时需要批量计算样本 loss 并聚合，涉及数据组织和复杂度。
- CSAPP：log、exp、浮点下溢、内存布局和向量化会影响 loss 计算稳定性。
- UMich DL：loss 是 autograd 图的终点，也是 optimizer 更新参数的信号来源。
