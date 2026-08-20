---
type: concept
course: Machine Learning
priority: A
status: draft
aliases: []
related: []
---

# Feature Scaling

## 一句话定义

feature scaling 是把不同特征调整到相近数值范围的数据预处理方法。它解决的是特征尺度差异过大导致 [[gradient-descent]] 收敛慢或路径不稳定的问题。

## 核心思想

在线性模型中，若一个特征范围是 $300$ 到 $2000$，另一个是 $0$ 到 $5$，相同参数变化会对 [[cost-function]] 产生很不均衡的影响，使等高线变得狭长。feature scaling 不改变监督学习任务本身，而是改变输入表示，让 optimization 更容易进行。

## 核心边界 / Objective / Assumption

设 $X \in \mathbb{R}^{m \times n}$，$m$ 是样本数，$n$ 是特征数，$X_{:,j}$ 是第 $j$ 个特征列。feature scaling 作用在输入 $X$ 上，不直接改变标签 $y$、模型参数 $w$ 或训练目标 $J$。无单一固定 invariant，重点在于让各列特征的尺度更接近，使梯度更新更稳定。

## 模型假设 / 局限

feature scaling 适合使用梯度下降训练、且特征数值尺度差异明显的模型，例如 [[linear-regression]]、[[logistic-regression]] 和神经网络输入。它不能解决模型表达能力不足、标签错误或过拟合；过拟合通常转向 [[regularization]]、更多数据或模型选择。对树模型是否必须缩放，需要人工补充。

## 在 Machine Learning 中的位置

它位于模型训练前，是 [[linear-regression]] 和 [[gradient-descent]] 之间的工程性连接点。先把输入表示处理好，再定义 loss/cost 并优化参数。它也为深度学习中的 input normalization 和 tensor preprocessing 打基础。

## 重要公式 / 算法

- 公式 / 算法名称：Max Scaling
- 解决的问题：把特征缩到相对范围内。
- 核心含义：$x_j'=\frac{x_j}{max_j}$；$x_j$ 是某个样本的第 $j$ 个特征，$max_j$ 是该特征列最大参考值。
- 相关概念链接：[[normalization]]

- 公式 / 算法名称：Mean Normalization
- 解决的问题：让特征围绕均值居中。
- 核心含义：$x_j'=\frac{x_j-\bar{x}_j}{max_j-min_j}$；$\bar{x}_j$ 是第 $j$ 列均值。
- 相关概念链接：[[feature-scaling]]

- 公式 / 算法名称：Z-score Normalization
- 解决的问题：用标准差统一特征尺度。
- 核心含义：$x_j'=\frac{x_j-\bar{x}_j}{\sigma_j}$；$\sigma_j$ 是第 $j$ 列标准差。
- 相关概念链接：[[gradient-descent]]

## 容易混淆点

- feature scaling vs regularization：前者变换输入，后者惩罚参数。
- normalization vs standardization：命名边界需要人工补充。
- feature scaling vs feature engineering：前者调整尺度，后者创建或选择特征。
- optimization vs generalization：缩放通常改善训练过程，不保证新数据误差一定下降。

## 相关概念

- [[linear-regression]]
- [[gradient-descent]]
- [[normalization]]
- [[regularization]]

## 跨课程连接

- CS61A：可看作对输入数据应用变换函数。
- CS61B：需要按列处理批量样本，涉及数组、表结构和预处理管道。
- CSAPP：缩放后的浮点范围会影响数值稳定性，批量变换受内存布局、cache 和向量化影响。
- UMich DL：对应 input normalization、tensor shape 保持不变但数值分布改变。
