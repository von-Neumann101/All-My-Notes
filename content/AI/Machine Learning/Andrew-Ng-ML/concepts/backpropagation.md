---
type: concept
course: Machine Learning
priority: A
status: draft
aliases: []
related: []
---

# Backpropagation

## 一句话定义

backpropagation 是在神经网络中从输出层向输入层高效计算参数梯度的方法。它解决的是如何为 [[gradient-descent]] 提供每个权重和偏置的偏导数。

## 核心思想

[[forward-propagation]] 先计算预测和 loss，backpropagation 再沿计算图反方向应用链式法则，把输出误差分配到每一层参数上。它不负责更新参数，真正的 update rule 属于 optimizer；它负责计算 gradient。

## 核心边界 / Objective / Assumption

设第 $l$ 层参数为 $W^{[l]}\in\mathbb{R}^{n_{l-1}\times n_l}$、$b^{[l]}\in\mathbb{R}^{n_l}$，前向传播得到 $Z^{[l]}$ 和 $A^{[l]}$。训练 objective 是 cost $J$；backpropagation 计算 $\frac{\partial J}{\partial W^{[l]}}$ 和 $\frac{\partial J}{\partial b^{[l]}}$；optimizer 再用 learning rate 等 hyperparameter 更新参数。当前笔记说明反向传播从右向左一次计算所有偏导，完整矩阵公式需要人工补充。

## 模型假设 / 局限

backpropagation 适用于由可微运算组成的计算图。若模型包含不可微步骤，需要 surrogate 或特殊处理。它能高效计算训练梯度，但不能保证 optimization 一定找到全局最优，也不保证 generalization。梯度检查在当前笔记中依据不足，需要人工补充。

## 在 Machine Learning 中的位置

它位于 [[neural-network]] 训练链条中：forward pass 得到 prediction 和 loss，backpropagation 得到 gradient，[[optimization]] 或 [[gradient-descent]] 更新参数。它是从手工线性模型训练走向深度学习训练的关键机制。

## 重要公式 / 算法

- 公式 / 算法名称：Reverse-mode Gradient Computation
- 解决的问题：一次反向遍历计算所有参数偏导。
- 核心含义：从 loss 出发，沿计算图从右向左传播导数；具体链式法则矩阵公式需要人工补充。
- 相关概念链接：[[forward-propagation]]、[[gradient-descent]]

- 公式 / 算法名称：Gradient for Parameters
- 解决的问题：为 optimizer 提供参数更新方向。
- 核心含义：计算 $\nabla_{W^{[l]}}J$、$\nabla_{b^{[l]}}J$；shape 应分别与 $W^{[l]}$、$b^{[l]}$ 一致。
- 相关概念链接：[[optimization]]

- 公式 / 算法名称：Autograd Implementation
- 解决的问题：由框架自动完成反向传播。
- 核心含义：index.md 提到 TensorFlow `fit` 利用反向传播，`GradientTape` 可用于自动微分。
- 相关概念链接：[[tensorflow]]

## 容易混淆点

- backpropagation vs gradient descent：前者算梯度，后者用梯度更新参数。
- forward propagation vs backpropagation：前者算预测，后者算偏导。
- gradient vs update rule：gradient 是方向信息，update rule 是参数变化公式。
- optimization vs generalization：梯度正确不代表模型泛化一定好。

## 相关概念

- [[neural-network]]
- [[forward-propagation]]
- [[gradient-descent]]
- [[optimization]]
- [[loss-function]]

## 跨课程连接

- CS61A：链式法则可类比函数组合的反向求导。
- CS61B：计算图中的依赖关系可看作有向图上的反向遍历。
- CSAPP：反向传播需要保存中间激活，内存布局、cache 和矩阵乘法性能会影响训练。
- UMich DL：对应 autograd、tensor shape、model.backward、optimizer.step 的核心机制。
