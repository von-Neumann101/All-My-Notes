---
type: concept
course: Machine Learning
priority: A
status: draft
aliases: []
related: []
---

# Gradient Descent

## 一句话定义

梯度下降是一种用目标函数梯度迭代更新参数的优化方法。它解决的是如何让 [[cost-function]] 逐步变小，从而训练模型。

## 核心思想

objective 告诉我们当前参数有多差，gradient 告诉我们参数变化对 objective 的影响方向。梯度下降沿负梯度方向更新参数，并用 learning rate $\alpha$ 控制步长。它不定义模型或 loss，只负责 optimization。

## 核心边界 / Objective / Assumption

objective 是要最小化的 $J(w,b)$；gradient 是 $\nabla J$；update rule 是参数更新公式；learning rate $\alpha$ 是 hyperparameter。以线性回归为例，$X \in \mathbb{R}^{m \times n}$，$w \in \mathbb{R}^n$，$b \in \mathbb{R}$，$y \in \mathbb{R}^m$。$w$ 和 $b$ 必须同步更新。Optimization 只保证训练目标被优化，不直接保证 generalization。

## 模型假设 / 局限

梯度下降适用于目标函数可求梯度或可用近似梯度的场景。对凸的线性回归 MSE，它可以收敛到全局最小；对复杂神经网络，可能遇到局部结构、学习率敏感和训练不稳定。若有可靠 closed-form solution，小规模线性回归可直接解；复杂模型通常需要 iterative solution。

## 在 Machine Learning 中的位置

梯度下降接在 [[cost-function]] 之后，把误差转化为参数变化。它向后连接 [[optimization]]、[[backpropagation]]、Adam 和 mini-batch；在线性回归、逻辑回归和神经网络训练中都是核心机制。

## 重要公式 / 算法

- 公式 / 算法名称：Gradient Descent Update Rule
- 解决的问题：用梯度更新参数。
- 核心含义：$w_{new}=w-\alpha\frac{\partial}{\partial w}J(w,b)$，$b_{new}=b-\alpha\frac{\partial}{\partial b}J(w,b)$；$w,b$ 是参数，$\alpha$ 是学习率。
- 相关概念链接：[[cost-function]]、[[optimization]]

- 公式 / 算法名称：Vector Update
- 解决的问题：批量更新多维参数。
- 核心含义：$w \leftarrow w-\alpha\nabla_w J$；$w,\nabla_wJ \in \mathbb{R}^n$，shape 必须一致。
- 相关概念链接：[[linear-regression]]

- 公式 / 算法名称：Linear Regression Gradient Descent
- 解决的问题：最小化线性回归平方误差。
- 核心含义：$w_{new}=w-\alpha\frac{1}{m}\sum_{i=1}^{m}(f_{w,b}(x^{(i)})-y^{(i)})x^{(i)}$；$m$ 是样本数。
- 相关概念链接：[[loss-function]]

## 容易混淆点

- gradient descent vs backpropagation：前者更新参数，后者计算神经网络梯度。
- objective vs update rule：objective 是目标，update rule 是改变参数的方法。
- learning rate vs gradient：学习率是超参数，梯度来自目标函数。
- optimization vs generalization：训练目标下降不代表新数据一定更好。

## 相关概念

- [[cost-function]]
- [[loss-function]]
- [[linear-regression]]
- [[optimization]]
- [[backpropagation]]

## 跨课程连接

- CS61A：梯度下降是迭代改进过程，每次根据当前状态生成下一个状态。
- CS61B：批量样本训练涉及数据组织、复杂度和 mini-batch 处理。
- CSAPP：训练速度受浮点误差、内存布局、cache、SIMD/向量化性能影响。
- UMich DL：autograd 计算梯度，optimizer 执行 update rule，tensor shape 必须匹配参数 shape。
