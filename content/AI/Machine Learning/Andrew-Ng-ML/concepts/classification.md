---
type: concept
course: Machine Learning
priority: A
status: draft
aliases: []
related: []
---

# Classification

## 一句话定义

classification 是从输入特征预测离散类别的监督学习任务。它解决的是输出不是连续数值，而是有限类别标签时如何建模、训练和评估。

## 核心思想

分类模型通常先输出 score 或概率，再根据阈值或最大概率得到类别。它需要与回归不同的 [[loss-function]]，因为类别错误不是连续数值误差，二分类、多分类和多标签分类也需要不同输出形式。

## 核心边界 / Objective / Assumption

无单一固定 model form，重点在任务目标和输出空间。二分类中 $y\in\{0,1\}^m$，模型可输出 $\hat y\in(0,1)^m$；多分类中 $y\in\{1,\dots,K\}^m$，模型可输出 logits 或 probabilities，shape 可写为 $Z\in\mathbb{R}^{m\times K}$。训练目标是最小化适合类别输出的 loss，例如 logistic loss 或 softmax loss。

## 模型假设 / 局限

classification 适合标签来自有限类别的任务。不适合目标本身是连续数量的任务，此时通常用 [[linear-regression]] 或其他回归模型。类别极不平衡时，accuracy 可能误导，需要 precision、recall 或 F1；如果类别之间不是互斥关系，应该使用多标签分类而不是 softmax 多分类。

## 在 Machine Learning 中的位置

分类从 [[supervised-learning]] 分支出来，先连接 [[logistic-regression]] 和 [[decision-boundary]]，再连接 neural network、softmax、多标签分类和 skewed data set 的评估指标。它是从线性回归走向神经网络分类任务的中间层。

## 重要公式 / 算法

- 公式 / 算法名称：Binary Classification with Sigmoid
- 解决的问题：预测二分类中 $y=1$ 的概率。
- 核心含义：$\hat y=g(w^\top x+b)$，$y\in\{0,1\}$，阈值常取 $0.5$。
- 相关概念链接：[[logistic-regression]]、[[decision-boundary]]

- 公式 / 算法名称：Softmax Classification
- 解决的问题：把多个类别 score 转成概率分布。
- 核心含义：index.md 给出 $a_i=\frac{e^{z_i}}{\sum e^{z_k}}=P(y=i|x)$；$i$ 是类别索引。
- 相关概念链接：[[softmax]]、[[loss-function]]

- 公式 / 算法名称：Precision / Recall
- 解决的问题：评估类别不平衡任务。
- 核心含义：index.md 讨论 precision、recall 和 F1-score；精确定义需要人工补充。
- 相关概念链接：[[precision-recall]]

## 容易混淆点

- regression vs classification：前者预测连续值，后者预测类别。
- binary vs multiclass：二分类两个类别，多分类多个互斥类别。
- multiclass vs multilabel：多分类选一个，多标签可同时选多个。
- probability vs label：概率输出还需要阈值或 argmax 变成标签。

## 相关概念

- [[supervised-learning]]
- [[logistic-regression]]
- [[decision-boundary]]
- [[loss-function]]
- [[precision-recall]]

## 跨课程连接

- CS61A：类别判断可对应谓词函数和条件分支。
- CS61B：类别标签、样本集合和 confusion matrix 都需要明确数据组织。
- CSAPP：批量分类推理受内存布局、cache、向量化和浮点数稳定性影响。
- UMich DL：图像分类、多标签输出、softmax、cross entropy 和 tensor shape。
