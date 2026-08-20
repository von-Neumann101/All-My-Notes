---
type: concept
course: Machine Learning
priority: A
status: draft
aliases: []
related: []
---

# Cost Function

## 一句话定义

cost function 是衡量模型在整个训练集上表现的整体目标函数。它解决的是如何把多个样本的预测错误汇总成一个可优化目标。

## 核心思想

单个样本的错误由 [[loss-function]] 衡量，但训练需要一个整体方向。cost function 通常把多个 loss 求和或平均，并可加入 [[regularization]] 项，形成 [[gradient-descent]] 要最小化的 objective。

## 核心边界 / Objective / Assumption

在线性回归中，设 $X \in \mathbb{R}^{m \times n}$，$w \in \mathbb{R}^n$，$b \in \mathbb{R}$，$y \in \mathbb{R}^m$，$\hat y=Xw+b\mathbf{1}$。cost function 是 objective，用于训练优化；gradient 是 objective 对参数的偏导；update rule 使用 gradient 改变参数；learning rate 是 hyperparameter。优化目标变小不等于泛化一定变好。

## 模型假设 / 局限

cost function 适用于可定义训练目标的模型。若 cost 与真正关心的任务指标不一致，模型可能优化了错误目标；若 cost 只在训练集上变小，也可能产生 [[overfitting]]。泛化能力需要 dev/test split、regularization 和误差分析补充判断。

## 在 Machine Learning 中的位置

在线性回归中，它汇总平方误差；在逻辑回归和神经网络中，它承接分类 loss；在 K-means 和推荐系统中，也有对应的失真函数或评分误差目标。因此它连接模型、loss、optimization 和 generalization。

## 重要公式 / 算法

- 公式 / 算法名称：Mean Squared Error Cost
- 解决的问题：衡量线性回归在训练集上的整体误差。
- 核心含义：$J(w,b)=\frac{1}{2m}\sum_{i=1}^{m}(f_{w,b}(x^{(i)})-y^{(i)})^2$；$m$ 是样本数，$x^{(i)}$ 是第 $i$ 个样本，$y^{(i)}$ 是标签。
- 相关概念链接：[[linear-regression]]、[[loss-function]]

- 公式 / 算法名称：Vectorized MSE
- 解决的问题：批量表达整体误差。
- 核心含义：$\hat y=Xw+b\mathbf{1}$，$J$ 汇总 $\hat y-y \in \mathbb{R}^m$ 的误差；具体向量化公式需要人工补充。
- 相关概念链接：[[optimization]]

- 公式 / 算法名称：Regularized Cost Function
- 解决的问题：在拟合数据的同时限制权重过大。
- 核心含义：$J(w,b)$ 可加入 $\frac{\lambda}{2m}\sum_{j=1}^{n}w_j^2$；$\lambda$ 是正则化超参数。
- 相关概念链接：[[regularization]]、[[overfitting]]

## 容易混淆点

- cost function vs loss function：loss 偏单样本，cost 偏训练集整体。
- objective vs gradient：objective 是要优化的函数，gradient 是它对参数的变化率。
- optimization vs generalization：训练目标下降不保证新数据表现变好。
- cost function vs evaluation metric：cost 用于训练，metric 可用于评估。

## 相关概念

- [[loss-function]]
- [[gradient-descent]]
- [[linear-regression]]
- [[regularization]]
- [[optimization]]

## 跨课程连接

- CS61A：cost 是把任务抽象为可计算函数。
- CS61B：cost 计算涉及对批量样本聚合，依赖数据组织和复杂度。
- CSAPP：大规模 cost 计算受浮点误差、内存布局、cache 和向量化影响。
- UMich DL：loss/cost 是 autograd 和 optimizer 的直接输入。
