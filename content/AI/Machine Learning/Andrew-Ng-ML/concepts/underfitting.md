---
type: concept
course: Machine Learning
priority: A
status: draft
aliases: []
related: []
---

# Underfitting

## 一句话定义

underfitting 是模型连训练集本身都拟合不好的现象，通常对应 high bias。它解决的是如何判断模型表达能力、特征表示或训练目标过弱，导致学习不到数据中的主要规律。

## 核心思想

优化只能在给定模型空间内寻找参数。如果模型太简单、特征不足、正则化过强或训练不充分，即使 [[gradient-descent]] 正常下降，最终也可能停在一个训练误差仍然很高的解。underfitting 的关键不是泛化失败，而是模型在训练集上已经表现不好。

## 核心边界 / Objective / Assumption

设训练集 $X_{train}\in\mathbb{R}^{m\times n}$、标签 $y_{train}\in\mathbb{R}^m$ 或 $y_{train}\in\{0,1\}^m$，模型为 $f_\theta(x)$。训练 objective 是最小化 $J_{train}(\theta)$。若 $J_{train}$ 相对基准性能仍然高，且 dev/test error 也高，通常说明 high bias 或 underfitting。它不是特定 model form，而是对模型容量和训练结果的诊断。

## 模型假设 / 局限

underfitting 适用于监督学习中的模型诊断，尤其是 [[linear-regression]]、[[logistic-regression]] 和 [[neural-network]]。它不适合用来解释训练集很好但 dev/test 很差的情况，那通常是 [[overfitting]]。如果是模型太简单，可增加特征、多项式特征或更大网络；如果是优化没收敛，应调整 learning rate、训练轮数或 optimizer。index.md 标明 underfitting 未被笔记系统展开，例子需要人工补充。

## 在 Machine Learning 中的位置

它位于 [[bias-variance]] 诊断框架中，和 [[overfitting]] 成对出现。先通过 [[train-dev-test-split]] 区分训练误差和泛化误差，再决定是提升模型容量、改善特征，还是处理 variance 和 regularization。

## 重要公式 / 算法

- 公式 / 算法名称：High Bias Diagnosis
- 解决的问题：判断模型是否连训练集都拟合不好。
- 核心含义：若 $J_{train}$ 明显高于可接受基准，且 $J_{cv}$ 也高，说明模型可能 high bias；$J_{train}$ 在训练集上计算，$J_{cv}$ 在 dev 集上计算。
- 相关概念链接：[[bias-variance]]、[[train-dev-test-split]]

- 公式 / 算法名称：Capacity Increase
- 解决的问题：增强模型可表达的函数空间。
- 核心含义：可增加特征、多项式特征或更大 neural network；具体选择依赖任务和数据，标准例子需要人工补充。
- 相关概念链接：[[neural-network]]、[[feature-scaling]]

## 容易混淆点

- underfitting vs overfitting：前者训练集也差，后者训练集好但泛化差。
- high bias vs high variance：high bias 说明模型能力不足，high variance 说明对训练集过度敏感。
- optimization failure vs underfitting：训练没收敛可能表现相似，但原因是 optimizer 或学习率，不一定是模型容量。
- regularization vs underfitting：正则化过强可能导致 underfitting。

## 相关概念

- [[overfitting]]
- [[bias-variance]]
- [[train-dev-test-split]]
- [[regularization]]
- [[neural-network]]

## 跨课程连接

- CS61A：可类比抽象过粗，函数族无法表达目标行为。
- CS61B：数据表示或算法选择过弱时，即使数据组织正确也无法捕捉结构。
- CSAPP：内存、计算资源或延迟限制可能迫使模型容量过小。
- UMich DL：对应 high bias、model capacity、larger network 和 training diagnostics。
