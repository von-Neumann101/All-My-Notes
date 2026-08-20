---
type: concept
course: Machine Learning
priority: A
status: draft
aliases: []
related: []
---

# Bias Variance

## 一句话定义

bias-variance 是用训练误差、dev 误差和基准水平诊断模型问题的框架。它解决的是模型表现差时，应判断是模型太简单、过拟合，还是数据或目标本身受限。

## 核心思想

只知道模型错了不够，还要知道错在哪里。high bias 表示模型连训练集都拟合不好；high variance 表示模型拟合训练集不错，但泛化到 dev/test 明显变差。这个框架直接决定下一步是增大模型、加特征，还是增加数据、正则化或减少特征。

## 核心边界 / Objective / Assumption

设 $J_{train}$ 在训练集上计算，$J_{cv}$ 在 dev 集上计算，$J_{test}$ 在测试集上计算。$X_{train}\in\mathbb{R}^{m_{train}\times n}$，$X_{dev}\in\mathbb{R}^{m_{dev}\times n}$，特征维度应一致。bias-variance 是诊断框架，不是训练 objective。完整 bias-variance decomposition 的数学公式需要人工补充。

## 模型假设 / 局限

该框架适用于已经有合理 train/dev/test 划分的监督学习任务。若数据划分有泄漏、dev 集不代表真实分布，诊断会失真。它不直接给出唯一解，只给出行动方向：high bias 常考虑更复杂模型或更多特征；high variance 常考虑更多数据、正则化或减少特征。

## 在 Machine Learning 中的位置

它位于 [[train-dev-test-split]] 之后，用于解释 [[overfitting]]、[[underfitting]] 和 [[regularization]]。它把 optimization 的结果转化为工程决策：下一步该改模型、改数据，还是改正则化。

## 重要公式 / 算法

- 公式 / 算法名称：Error Comparison Diagnosis
- 解决的问题：判断模型偏差或方差问题。
- 核心含义：$J_{train}$ 高通常提示 high bias；$J_{cv}\gg J_{train}$ 通常提示 high variance。
- 相关概念链接：[[overfitting]]、[[underfitting]]

- 公式 / 算法名称：Lambda Selection
- 解决的问题：选择正则化强度。
- 核心含义：index.md 提到在 dev 集上比较不同 $\lambda$，选择使 $J_{cv}$ 较小的模型。
- 相关概念链接：[[regularization]]

- 公式 / 算法名称：Learning Curve
- 解决的问题：观察误差随数据量变化。
- 核心含义：用于教学中理解训练误差和 dev 误差趋势；具体公式需要人工补充。
- 相关概念链接：[[train-dev-test-split]]

## 容易混淆点

- bias vs variance：bias 看训练集是否拟合好，variance 看训练和 dev/test 差距。
- high variance vs overfitting：二者高度相关，但 high variance 是诊断语言。
- high bias vs underfitting：二者相关，但 high bias 更强调误差来源。
- optimization vs diagnosis：梯度下降更新参数，bias-variance 判断下一步策略。

## 相关概念

- [[overfitting]]
- [[underfitting]]
- [[regularization]]
- [[train-dev-test-split]]
- [[generalization]]

## 跨课程连接

- CS61A：可类比抽象层级不合适，太粗导致 bias，太贴样例导致 variance。
- CS61B：数据规模、特征组织和模型复杂度影响诊断结果。
- CSAPP：模型容量和实验规模受计算资源、内存和性能约束。
- UMich DL：对应 validation diagnostics、model capacity、regularization 和 learning curves。
