---
type: concept
course: Machine Learning
priority: A
status: draft
aliases: []
related: []
---

# Overfitting

## 一句话定义

overfitting 是模型过度适应训练数据，导致训练集表现好但新数据表现差。它解决的是如何识别和处理模型“记住训练集细节而没有学到可泛化规律”的问题。

## 核心思想

训练目标下降只说明模型更贴合训练集，不保证 [[generalization]]。当模型容量过大、数据太少或特征太复杂时，模型可能把噪声也当作规律学习。overfitting 的核心不是训练失败，而是训练得太贴近训练集，导致 dev/test error 偏高。

## 核心边界 / Objective / Assumption

设训练集 $X_{train}\in\mathbb{R}^{m_{train}\times n}$，dev/test 集分别是 $X_{dev}$、$X_{test}$；模型 $f_\theta$ 在训练集上最小化 $J_{train}$。overfitting 通常表现为 $J_{train}$ 低，但 $J_{cv}$ 或 $J_{test}$ 明显更高。这里 objective 是训练 cost，generalization 需要用独立数据估计。

## 模型假设 / 局限

overfitting 适用于讨论有训练数据和未见数据差距的监督学习模型。它不等同于模型训练错误，也不一定能只靠继续优化解决。常见处理是增加数据、减少无关特征、使用 [[regularization]]、调整模型复杂度或重新做 train/dev/test 诊断。若问题是模型太简单，则通常转向 [[underfitting]] 或 high bias 处理。

## 在 Machine Learning 中的位置

overfitting 位于 [[cost-function]] 和 [[bias-variance]] 之后，是从 optimization 走向 generalization 的关键问题。它解释了为什么只看训练集 cost 不够，也为 [[regularization]]、数据增强和模型选择提供动机。

## 重要公式 / 算法

- 公式 / 算法名称：Train vs Dev Error Gap
- 解决的问题：判断模型是否可能过拟合。
- 核心含义：若 $J_{train}$ 很低而 $J_{cv}$ 明显高，说明模型可能高方差；$J_{train}$、$J_{cv}$ 分别在训练集和 dev 集计算。
- 相关概念链接：[[bias-variance]]、[[train-dev-test-split]]

- 公式 / 算法名称：L2 Regularization
- 解决的问题：限制权重过大以缓解过拟合。
- 核心含义：$J_{reg}=J+\frac{\lambda}{2m}\sum_{j=1}^{n}w_j^2$；$\lambda$ 是正则化强度，$m$ 是样本数，$n$ 是特征数。
- 相关概念链接：[[regularization]]

## 容易混淆点

- overfitting vs underfitting：前者训练集好但泛化差，后者训练集本身也拟合不好。
- training cost vs generalization：训练 cost 低不等于新数据误差低。
- regularization vs feature scaling：正则化控制复杂度，特征缩放改善优化条件。
- more optimization vs better model：继续降低训练误差可能加重过拟合。

## 相关概念

- [[regularization]]
- [[bias-variance]]
- [[train-dev-test-split]]
- [[cost-function]]
- [[underfitting]]

## 跨课程连接

- CS61A：可类比规则过度适配少数样例，抽象没有抓住一般规律。
- CS61B：数据规模、特征数量和模型复杂度会影响过拟合风险。
- CSAPP：更大模型和更多特征会增加内存、cache 和计算成本。
- UMich DL：对应 generalization、weight decay、data augmentation 和 validation set 诊断。
