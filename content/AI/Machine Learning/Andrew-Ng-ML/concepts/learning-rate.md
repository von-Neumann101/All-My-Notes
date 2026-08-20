---
type: concept
course: Machine Learning
priority: B
status: draft
aliases: []
related: []
---

# Learning Rate

## 一句话定义

learning rate 是控制每次参数更新步长的优化超参数。它解决的是梯度方向确定后，参数一次应该移动多远的问题。

## 核心思想

[[gradient-descent]] 的 gradient 只告诉我们方向和局部变化率，learning rate $\alpha$ 决定实际更新幅度。太大可能越过较好区域甚至发散，太小会训练很慢。它是 optimization 的参数，不是模型学出的 parameter。

## 核心边界 / Objective / Assumption

设 objective 为 $J(\theta)$，gradient 为 $\nabla_\theta J$，update rule 为 $\theta\leftarrow\theta-\alpha\nabla_\theta J$。$\theta$ 和 $\nabla_\theta J$ shape 相同；$\alpha\in\mathbb{R}$ 是 hyperparameter。learning rate 影响 optimization 过程，但不直接定义 generalization。

## 模型假设 / 局限

learning rate 适用于迭代优化方法。固定 $\alpha$ 在简单模型中可用，但复杂神经网络常需要 Adam 或学习率调度；当前笔记只说明 Adam 自动调整 $\alpha$，详细公式需要人工补充。学习率调好了也不能解决错误模型、坏特征或过拟合。

## 在 Machine Learning 中的位置

learning rate 位于 [[gradient-descent]] 的 update rule 中，是 [[optimization]] 的核心超参数。它也连接学习曲线：如果 cost 增加，可能是代码错误或学习率不合适。

## 重要公式 / 算法

- 公式 / 算法名称：Gradient Descent Step
- 解决的问题：控制参数更新幅度。
- 核心含义：$w_{new}=w-\alpha\frac{\partial J}{\partial w}$；$\alpha$ 越大，单步移动越大。
- 相关概念链接：[[gradient-descent]]

- 公式 / 算法名称：Vector Update
- 解决的问题：多参数同步更新。
- 核心含义：$\theta\leftarrow\theta-\alpha\nabla_\theta J$；$\theta,\nabla_\theta J$ shape 一致。
- 相关概念链接：[[optimization]]

- 公式 / 算法名称：Adam Learning Rate Adaptation
- 解决的问题：自动调整优化步长相关行为。
- 核心含义：index.md 提到 Adam 可针对 $\alpha$ 自动调整；具体动量和二阶矩公式需要人工补充。
- 相关概念链接：[[optimization]]

## 容易混淆点

- learning rate vs gradient：learning rate 是人为设定，gradient 来自 objective。
- learning rate vs parameter：$\alpha$ 是 hyperparameter，不是训练数据学出的参数。
- small learning rate vs good generalization：小步长可能稳定训练，但不保证泛化。
- Adam vs gradient descent：Adam 是更复杂 optimizer，不是 loss function。

## 相关概念

- [[gradient-descent]]
- [[optimization]]
- [[cost-function]]
- [[backpropagation]]

## 跨课程连接

- CS61A：对应迭代改进中的步长控制。
- CS61B：影响训练迭代次数和整体算法成本。
- CSAPP：学习率过小会增加训练轮数，放大计算和内存访问成本。
- UMich DL：对应 optimizer hyperparameter、learning rate schedule、Adam 和 training dynamics。
