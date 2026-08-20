---
type: concept
course: Machine Learning
priority: A
status: draft
aliases: []
related: []
---

# Forward Propagation

## 一句话定义

forward propagation 是神经网络从输入逐层计算到输出预测的过程。它解决的是给定模型参数后，如何执行推理并得到 $\hat y$。

## 核心思想

神经网络的每一层接收上一层输出，先做线性变换，再套激活函数。这个过程只计算预测，不更新参数；训练还需要 [[loss-function]]、[[backpropagation]] 和 [[gradient-descent]]。

## 核心边界 / Objective / Assumption

设输入批量 $A^{[0]}=X\in\mathbb{R}^{m\times n_0}$，第 $l$ 层输出 $A^{[l]}\in\mathbb{R}^{m\times n_l}$。常见约定为 $Z^{[l]}=A^{[l-1]}W^{[l]}+b^{[l]}$，$W^{[l]}\in\mathbb{R}^{n_{l-1}\times n_l}$，$b^{[l]}\in\mathbb{R}^{n_l}$，$A^{[l]}=g(Z^{[l]})$。index.md 已有矩阵乘法和激活值依据，完整标准符号需要人工补充。

## 模型假设 / 局限

forward propagation 适用于已定义结构和参数的神经网络或线性层堆叠。它本身不学习参数，不判断泛化，也不保证模型好；若输出错误，需要通过 loss 和反向传播训练参数。若所有层都是 linear activation，多层前向传播仍等价于一个线性模型。

## 在 Machine Learning 中的位置

它位于 [[neural-network]] 的推理部分，是 [[backpropagation]] 的前提。先 forward 得到预测和 loss，再 backward 计算梯度，最后 optimizer 更新参数。它也连接矩阵化实现和 CSAPP 层面的性能问题。

## 重要公式 / 算法

- 公式 / 算法名称：Layer Forward Computation
- 解决的问题：计算单层输出。
- 核心含义：$Z^{[l]}=A^{[l-1]}W^{[l]}+b^{[l]}$，$A^{[l]}=g(Z^{[l]})$；shape 如上。
- 相关概念链接：[[neural-network]]、[[activation-function]]

- 公式 / 算法名称：Output Activation Choice
- 解决的问题：让输出符合任务形式。
- 核心含义：二分类常用 sigmoid，回归可用 linear 或 ReLU，多分类用 softmax；来自 index.md。
- 相关概念链接：[[classification]]、[[loss-function]]

- 公式 / 算法名称：Vectorized Forward Pass
- 解决的问题：避免逐样本循环，提高计算效率。
- 核心含义：用矩阵乘法一次处理 $m$ 个样本，$X\in\mathbb{R}^{m\times n}$。
- 相关概念链接：[[vectorization]]

## 容易混淆点

- forward propagation vs backpropagation：前者算预测，后者算梯度。
- inference vs training：推理只需要 forward，训练还需要 loss 和参数更新。
- activation vs layer output：激活函数 $g$ 作用在 $Z$ 上，输出 $A$。
- linear activation vs no nonlinearity：隐藏层全线性会退化为线性模型。

## 相关概念

- [[neural-network]]
- [[activation-function]]
- [[backpropagation]]
- [[loss-function]]
- [[vectorization]]

## 跨课程连接

- CS61A：forward pass 是函数组合的求值过程。
- CS61B：层间依赖可看作有向计算图上的数据流。
- CSAPP：矩阵乘法性能受内存布局、cache、SIMD/向量化和批大小影响。
- UMich DL：对应 tensor shape、model.forward、autograd graph construction 和 inference。
