---
type: concept
course: Machine Learning
priority: C
status: draft
aliases: []
related: []
---

# Precision Recall

## 一句话定义

precision 和 recall 是类别不平衡分类任务中的评估指标。它们解决的是 accuracy 在 skewed data set 上可能被多数类掩盖、无法说明正类预测质量的问题。

## 核心思想

当正类很少时，模型一直输出负类也可能得到很高 accuracy，但这种模型没有实际价值。precision 关注“被模型判为正的样本有多少真的为正”，recall 关注“所有真实正样本中有多少被找出来”。两者通常需要权衡，F1-score 用调和平均让较小的一方影响更大。

## 核心边界 / Objective / Assumption

设二分类标签 $y\in\{0,1\}^m$，模型输出概率 $\hat p\in[0,1]^m$，经过阈值得到预测标签 $\hat y\in\{0,1\}^m$。precision/recall 是 evaluation metric，不是 differentiable training objective，也不是参数更新规则。它们依赖 positive class 的定义和分类阈值。

## 模型假设 / 局限

precision/recall 适合正负类不平衡、正类更关键的任务，例如疾病诊断、异常检测或检索结果筛选。它不适合单独描述多分类模型的全部表现；多分类和多标签下的 micro/macro averaging 当前笔记没有覆盖，需要人工补充。若需要直接训练模型，仍要用 cross entropy 等 [[loss-function]]。

## 在 Machine Learning 中的位置

它位于 [[classification]] 的评估阶段，常与 [[logistic-regression]]、[[decision-boundary]] 和阈值选择一起使用。它也连接 [[anomaly-detection]]，因为异常样本通常稀少，单看 accuracy 容易误导。

## 重要公式 / 算法

- 公式 / 算法名称：Precision
- 解决的问题：衡量正类预测的可靠性。
- 核心含义：$Precision=\frac{TP}{TP+FP}$；$TP$ 是真正例，$FP$ 是假正例。
- 相关概念链接：[[classification]]

- 公式 / 算法名称：Recall
- 解决的问题：衡量真实正类被找回的比例。
- 核心含义：$Recall=\frac{TP}{TP+FN}$；$FN$ 是假负例。
- 相关概念链接：[[classification]]

- 公式 / 算法名称：F1-score
- 解决的问题：用一个数平衡 precision 和 recall。
- 核心含义：$F1=\frac{2PR}{P+R}$，其中 $P$ 是 precision，$R$ 是 recall；笔记强调它偏向较小的一方。
- 相关概念链接：[[loss-function]]

## 容易混淆点

- precision vs recall：前者看预测为正的集合，后者看真实为正的集合。
- precision/recall vs accuracy：accuracy 容易被多数类主导。
- threshold vs model parameter：阈值通常是调参选择，不是训练学出的权重。
- metric vs loss：precision/recall 用于评估，loss 用于训练优化。

## 相关概念

- [[classification]]
- [[decision-boundary]]
- [[logistic-regression]]
- [[anomaly-detection]]
- [[loss-function]]

## 跨课程连接

- CS61A：可以看作对预测结果集合应用谓词和计数函数。
- CS61B：需要维护 confusion matrix 中的 TP、FP、FN，并按数据集批量统计。
- CSAPP：大规模评估时计数、批处理和内存访问会影响指标计算性能。
- UMich DL：对应分类评估、threshold tuning、imbalanced dataset 和 validation loop。
