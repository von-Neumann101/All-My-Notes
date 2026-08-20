---
type: concept
course: Machine Learning
priority: A
status: draft
aliases: []
related: []
---

# Linear Regression

## 一句话定义

线性回归用输入特征的加权和预测连续数值。它解决的是监督学习中最基础的回归问题，例如用房屋特征预测价格。

## 核心思想

线性回归假设目标值可以由特征的线性组合近似。训练时不是直接调整每个预测，而是学习参数 $w,b$，让整体 [[cost-function]] 变小；这使它成为理解模型、损失、优化和泛化的最小完整例子。

## 核心边界 / Objective / Assumption

单样本形式：$f_{w,b}(x)=wx+b=\hat y$。多特征形式：$f_{\boldsymbol w,b}(\boldsymbol x)=\boldsymbol w^\top \boldsymbol x+b$。批量 shape convention：$X \in \mathbb{R}^{m \times n}$，$w \in \mathbb{R}^n$，$y \in \mathbb{R}^m$，$b \in \mathbb{R}$，prediction $=Xw+b\mathbf{1}$。输入是特征 $X$，参数是 $w,b$，输出是连续预测 $\hat y$。训练目标通常是最小化均方误差 cost，以获得最佳的$w$ 和 $b$。

## 模型假设 / 局限

线性回归适用于连续值预测，且线性关系足够表达主要规律的任务。它不适合直接输出分类概率，分类通常转向 [[logistic-regression]]；如果关系明显非线性，可考虑特征工程、多项式特征或 [[neural-network]]。它对特征尺度敏感，通常需要 [[feature-scaling]]。

## 在 Machine Learning 中的位置

线性回归位于 [[supervised-learning]] 之后，是连接 [[loss-function]]、[[cost-function]] 和 [[gradient-descent]] 的第一个模型。它也为逻辑回归中的线性部分和神经网络中的线性层打基础。

## 重要公式 / 算法

- 公式 / 算法名称：Linear Regression Hypothesis
- 解决的问题：用特征预测连续目标。
- 核心含义：$f_{\boldsymbol w,b}(\boldsymbol x)=\boldsymbol w^\top \boldsymbol x+b$；$\boldsymbol x,w \in \mathbb{R}^n$，$b$ 是标量，输出 $\hat y$ 是标量。
- 相关概念链接：[[supervised-learning]]、[[cost-function]]

- 公式 / 算法名称：批量预测
- 解决的问题：一次计算全部样本预测。
- 核心含义：$\hat y=Xw+b\mathbf{1}$；$X \in \mathbb{R}^{m \times n}$，$\hat y,y \in \mathbb{R}^m$。
- 相关概念链接：[[feature-scaling]]、[[optimization]]

- 公式 / 算法名称：Closed-form vs Iterative Solution
- 解决的问题：选择如何求解参数。
- 核心含义：原笔记给出正规方程 $A^TA\hat{x}=A^TB$，它是 closed-form 思路，不需要迭代，但受矩阵可逆性、维度和数值稳定性影响；[[gradient-descent]] 是 iterative solution，更通用，适合大规模数据或复杂模型。
- 相关概念链接：[[gradient-descent]]、[[optimization]]

## 容易混淆点

- linear regression vs logistic regression：前者输出连续值，后者输出分类概率。
- feature vs parameter：特征是输入，参数是模型学习的 $w,b$。
- closed-form vs gradient descent：前者直接解方程，后者迭代更新。
- feature scaling vs regularization：前者改变输入尺度，后者惩罚参数大小。

## 相关概念

- [[supervised-learning]]
- [[cost-function]]
- [[loss-function]]
- [[gradient-descent]]
- [[feature-scaling]]

## 跨课程连接

- CS61A：$f(x)=wx+b$ 是函数抽象的最小模型。
- CS61B：$X \in \mathbb{R}^{m \times n}$ 涉及批量样本存储、矩阵数据组织和复杂度。
- CSAPP：批量预测依赖矩阵乘法、浮点误差、内存布局、cache 和向量化性能。
- UMich DL：线性层、tensor shape、矩阵化实现和 optimizer 都以这个模型为基础。
