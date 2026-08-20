---
type: concept
course: Machine Learning
priority: B
status: draft
aliases: []
related: []
---

# Normalization

## 一句话定义

normalization 是把数据的尺度、中心或基准值调整到更适合建模的表示方式。它解决的是数值范围不一致、中心偏移或推荐系统评分基准不同导致优化和预测不稳定的问题。

## 核心思想

同一个模型在不同特征尺度下会看到完全不同的 cost landscape：大尺度特征会主导梯度，小尺度特征更新变慢。normalization 不改变监督学习的标签，也不直接增加模型表达能力，而是改变输入或评分的数值表示，让 [[gradient-descent]]、PCA 或推荐系统预测更容易工作。

## 核心边界 / Objective / Assumption

无单一固定 model form，重点在数据变换。对特征矩阵 $X\in\mathbb{R}^{m\times n}$，$m$ 是样本数，$n$ 是特征数，normalization 通常按列处理 $X_{:,j}$，保持 shape 不变但改变数值分布。对推荐系统，评分矩阵 $Y\in\mathbb{R}^{n_m\times n_u}$ 可以按 item 均值 $\mu_i$ 做均值归一化。它不是 objective，也不是 parameter update rule。

## 模型假设 / 局限

normalization 适合数值特征尺度差异明显、使用梯度优化、PCA 或距离度量的场景。它不适合替代 [[regularization]]：前者变换数据，后者惩罚参数。若问题来自过拟合，应转向 regularization、更多数据或模型选择；若来自特征语义错误，应做 feature engineering。normalization、standardization、feature scaling 的命名边界需要人工补充。

## 在 Machine Learning 中的位置

它位于训练前的数据表示阶段，连接 [[feature-scaling]]、[[gradient-descent]] 和 [[principal-component-analysis]]。在推荐系统中，它连接 [[recommender-system]] 与 [[collaborative-filtering]]，用于修正新用户评分全为 0 时的异常预测。

## 重要公式 / 算法

- 公式 / 算法名称：Mean Normalization
- 解决的问题：让特征围绕均值居中。
- 核心含义：$x_j'=\frac{x_j-\bar{x}_j}{max_j-min_j}$，$x_j$ 是第 $j$ 个特征值，$\bar{x}_j$ 是该列均值。
- 相关概念链接：[[feature-scaling]]

- 公式 / 算法名称：Z-score Normalization
- 解决的问题：用标准差统一特征尺度。
- 核心含义：$x_j'=\frac{x_j-\bar{x}_j}{\sigma_j}$，$\sigma_j$ 是第 $j$ 列标准差。
- 相关概念链接：[[gradient-descent]]

- 公式 / 算法名称：Recommender Mean Normalization
- 解决的问题：修正评分矩阵中不同 item 的评分基准。
- 核心含义：对 item $i$ 减去均值 $\mu_i$，预测时再加回 $\mu_i$；具体矩阵形式需要人工补充。
- 相关概念链接：[[recommender-system]]

## 容易混淆点

- normalization vs regularization：normalization 改变数据尺度，regularization 惩罚参数。
- normalization vs feature scaling：feature scaling 是 normalization 在输入特征上的具体用法。
- normalization vs standardization：术语边界需要人工补充。
- optimization vs generalization：normalization 可改善训练稳定性，但不保证泛化误差下降。

## 相关概念

- [[feature-scaling]]
- [[gradient-descent]]
- [[regularization]]
- [[principal-component-analysis]]
- [[recommender-system]]

## 跨课程连接

- CS61A：可看作对输入数据应用变换函数，保持接口不变但改变内部数值。
- CS61B：批量样本按列统计均值、最大值、最小值和标准差，依赖清晰的数据组织。
- CSAPP：数值范围、浮点精度、cache 和向量化会影响大矩阵 normalization 的稳定性和性能。
- UMich DL：对应 input normalization、tensor shape 保持不变、batch normalization 的前置概念。
