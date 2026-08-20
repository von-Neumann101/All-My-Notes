---
type: concept
course: Machine Learning
priority: A
status: draft
aliases: []
related: []
---

# Train Dev Test Split

## 一句话定义

train-dev-test split 是把数据划分为训练、调参和最终评估三部分的协议。它解决的是如何避免用测试集做模型选择，从而得到更可信的泛化误差估计。

## 核心思想

训练集用于拟合参数，dev 集用于选择模型或超参数，测试集只用于最后估计泛化表现。若用测试集反复选模型，测试误差会被调参过程污染，变成过于乐观的估计。

## 核心边界 / Objective / Assumption

设总数据 $X\in\mathbb{R}^{m\times n}$，划分为 $X_{train}$、$X_{dev}$、$X_{test}$，三者特征维度都是 $n$。参数 $w,b$ 或 $\theta$ 在训练集上学习；超参数如多项式次数 $d$、正则化强度 $\lambda$ 在 dev 集上选择；$J_{test}$ 用于最终评估。它不是模型，也不是 optimization algorithm。

## 模型假设 / 局限

该协议适用于有足够数据、需要评估泛化能力的监督学习任务。若数据很少，划分会增加估计噪声；若 train/dev/test 来自不同分布，结果可能误导。异常检测中已知异常很少时，笔记提到可能删去测试集并把剩余异常放到 dev，但这会带来无法最终测试的风险。

## 在 Machine Learning 中的位置

它是 [[bias-variance]]、[[regularization]] 和模型选择的前提。没有独立 dev/test，就很难判断 [[overfitting]]，也无法可靠比较不同模型或超参数。

## 重要公式 / 算法

- 公式 / 算法名称：60/20/20 Split
- 解决的问题：给训练、模型选择和测试分别保留数据。
- 核心含义：index.md 给出训练集 60%、dev 集 20%、测试集 20% 的示例比例。
- 相关概念链接：[[bias-variance]]

- 公式 / 算法名称：Model Selection Protocol
- 解决的问题：避免测试集泄漏。
- 核心含义：先用训练集拟合 $J_{train}$，再用 dev 集选择模型使 $J_{cv}$ 合适，最后用测试集估计 $J_{test}$。
- 相关概念链接：[[regularization]]、[[overfitting]]

## 容易混淆点

- dev set vs test set：dev 用于选择模型，test 用于最终估计。
- parameter vs hyperparameter：参数在训练集学，超参数用 dev 集选。
- low dev error vs final performance：最终仍需 test set 验证。
- train error vs test error：训练误差不代表泛化误差。

## 相关概念

- [[bias-variance]]
- [[overfitting]]
- [[regularization]]
- [[cost-function]]
- [[generalization]]

## 跨课程连接

- CS61A：类似把样例分成开发验证和最终检查，避免对测试样例过拟合。
- CS61B：数据划分涉及集合切分、随机抽样、数据组织和批处理。
- CSAPP：批量实验和性能测量也需要区分调参数据和最终测量数据。
- UMich DL：对应 validation set、test set、hyperparameter tuning 和 model selection。
