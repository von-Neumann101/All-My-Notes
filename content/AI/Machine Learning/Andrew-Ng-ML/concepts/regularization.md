---
type: concept
course: Machine Learning
priority: A
status: draft
aliases: []
related: []
---

# Regularization

## 一句话定义

regularization 是在训练目标中加入对模型复杂度的惩罚。它解决的是模型过度拟合训练集、参数过大、泛化能力变差的问题。

## 核心思想

只最小化训练误差会鼓励模型尽可能贴合训练样本，包括噪声。regularization 把“预测错误小”和“参数不要过大”放进同一个 [[cost-function]]，让模型在拟合能力和泛化能力之间折中。

## 核心边界 / Objective / Assumption

以 L2 regularization 为例，$X\in\mathbb{R}^{m\times n}$，$w\in\mathbb{R}^n$，$b\in\mathbb{R}$。objective 变为原 cost 加 penalty：$\frac{\lambda}{2m}\sum_{j=1}^{n}w_j^2$。$\lambda$ 是 hyperparameter，控制惩罚强度；通常不正则化 $b$。optimization 会最小化这个新 objective，但 generalization 仍需要 dev/test 验证。

## 模型假设 / 局限

regularization 适用于高方差、过拟合或参数过大的模型。若模型本身欠拟合，过强 regularization 会进一步增加 bias。它不能替代数据质量、合适特征和合理模型结构；若 L2 不够，L1、dropout、early stopping 等方法需要人工补充。

## 在 Machine Learning 中的位置

它连接 [[overfitting]]、[[cost-function]]、[[gradient-descent]] 和 [[bias-variance]]。在线性回归、逻辑回归和神经网络中都可使用，是从训练误差走向泛化能力的关键概念。

## 重要公式 / 算法

- 公式 / 算法名称：L2 Regularized Cost
- 解决的问题：惩罚过大的权重。
- 核心含义：$J_{reg}(w,b)=J(w,b)+\frac{\lambda}{2m}\sum_{j=1}^{n}w_j^2$；$m$ 是样本数，$n$ 是特征数，$\lambda$ 是正则化强度。
- 相关概念链接：[[cost-function]]、[[overfitting]]

- 公式 / 算法名称：Weight Decay View
- 解决的问题：理解正则化对梯度更新的影响。
- 核心含义：index.md 给出 $w_{new}=(1-\alpha\frac{\lambda}{m})w-\alpha\cdots$，表示每次更新会缩小旧权重。
- 相关概念链接：[[gradient-descent]]

- 公式 / 算法名称：Model Selection for Lambda
- 解决的问题：选择正则化强度。
- 核心含义：index.md 提到在 dev 集上选择使 $J_{cv}$ 较小的 $\lambda$。
- 相关概念链接：[[train-dev-test-split]]

## 容易混淆点

- regularization vs normalization：前者惩罚参数，后者变换输入特征。
- regularization vs feature selection：前者缩小权重，后者选择或删除特征。
- low training cost vs good generalization：正则化关注新数据表现，不只看训练误差。
- lambda vs learning rate：$\lambda$ 控制惩罚强度，$\alpha$ 控制更新步长。

## 相关概念

- [[cost-function]]
- [[gradient-descent]]
- [[overfitting]]
- [[bias-variance]]
- [[train-dev-test-split]]

## 跨课程连接

- CS61A：regularization 可看作在目标函数中组合一个惩罚项。
- CS61B：模型复杂度、特征数量和数据规模会影响过拟合风险。
- CSAPP：更大模型和更多参数带来内存、cache 和矩阵计算成本。
- UMich DL：对应 weight decay、optimizer 中的 regularization、generalization 和 dev set 调参。
