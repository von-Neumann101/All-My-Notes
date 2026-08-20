---
type: concept
course: Machine Learning
priority: C
status: draft
aliases: []
related: []
---

# Feature Engineering

## 一句话定义

feature engineering 是根据任务知识创建、选择或变换输入特征，让模型更容易学习目标关系。它解决的是原始输入表达不足，导致简单模型难以拟合或异常模式不明显的问题。

## 核心思想

模型看到的不是现实世界本身，而是特征表示。笔记中的房价例子说明，长和宽本身有用，但面积可能是更直接的预测信号；异常检测中，如果特征不能让异常呈现低概率，就需要变换或构造新特征。神经网络可以自动学习部分特征，但手工特征仍影响数据质量和诊断。

## 核心边界 / Objective / Assumption

设原始特征矩阵 $X\in\mathbb{R}^{m\times n}$，feature engineering 构造 $\Phi(X)\in\mathbb{R}^{m\times p}$，其中 $p$ 可以大于、小于或等于 $n$。标签 $y$ 不变，model form 和训练 objective 可保持不变，但输入表示改变。它不是 parameter update rule，而是建模前的表示设计。

## 模型假设 / 局限

feature engineering 适合结构化数据、线性模型、异常检测和错误分析驱动的项目。它不适合盲目增加特征：无关特征可能增加 variance，数据泄漏会让 dev/test 估计失真。若特征尺度变化很大，需要配合 [[feature-scaling]]；若手工特征难以设计，可转向 [[neural-network]] 或 [[transfer-learning]]。

## 在 Machine Learning 中的位置

它连接 [[linear-regression]]、[[decision-boundary]]、[[anomaly-detection]] 和 [[bias-variance]]。在课程主线中，它位于数据表示与模型优化之间：好的特征能让简单模型表达更合适，也能让异常检测的密度模型更有效。

## 重要公式 / 算法

- 公式 / 算法名称：Area Feature
- 解决的问题：把长宽组合成更直接的房屋面积信号。
- 核心含义：$x_{area}=x_{length}\cdot x_{width}$；新特征加入后 $X$ 的列数增加。
- 相关概念链接：[[linear-regression]]

- 公式 / 算法名称：Polynomial Features
- 解决的问题：让线性模型表达非线性关系。
- 核心含义：可加入 $x^2,x^3$ 等特征；高次项会放大尺度差异，因此需要 [[feature-scaling]]。
- 相关概念链接：[[decision-boundary]]

- 公式 / 算法名称：Feature Transform for Gaussianity
- 解决的问题：让异常检测特征更接近高斯分布。
- 核心含义：当前笔记只说明可通过变换让非高斯特征更接近高斯；具体变换需要人工补充。
- 相关概念链接：[[anomaly-detection]]

## 容易混淆点

- feature engineering vs feature scaling：前者创建或选择特征，后者调整数值尺度。
- feature engineering vs neural network：神经网络可学习表示，但不等于不需要理解输入特征。
- more features vs better features：更多特征可能增加过拟合风险。
- feature engineering vs data augmentation：前者改变表示，后者扩充样本。

## 相关概念

- [[linear-regression]]
- [[feature-scaling]]
- [[anomaly-detection]]
- [[decision-boundary]]
- [[neural-network]]

## 跨课程连接

- CS61A：把原始输入组合成更合适的函数抽象。
- CS61B：需要组织特征列、映射、缺失值和批量转换流程。
- CSAPP：大规模特征生成受内存布局、缓存和向量化影响。
- UMich DL：连接 representation learning、input pipeline 和 tabular feature design。
