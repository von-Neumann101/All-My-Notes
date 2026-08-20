---
type: concept
course: Machine Learning
priority: C
status: draft
aliases: []
related: []
---

# Unsupervised Learning

## 一句话定义

unsupervised learning 是在没有标签或正确答案的情况下，从输入数据中寻找结构的学习范式。它解决的是无法给每个样本提供 $y$ 时，如何发现分组、低维表示、异常或潜在特征。

## 核心思想

监督学习学习 $x\to y$，无监督学习只有 $X$。模型不被告知“正确类别”，而是通过距离、方差、密度或交互结构定义目标。笔记中的主要例子包括 [[k-means]] 聚类、[[principal-component-analysis]] 降维、[[anomaly-detection]] 和推荐系统中的潜在表示学习。

## 核心边界 / Objective / Assumption

输入通常是 $X\in\mathbb{R}^{m\times n}$，没有标签向量 $y$。output 取决于任务：聚类输出簇编号 $c^{(i)}$，PCA 输出低维表示 $Z\in\mathbb{R}^{m\times k}$，异常检测输出密度 $p(x)$ 或异常标记。无单一固定 objective；每个算法要单独定义目标函数。

## 模型假设 / 局限

unsupervised learning 适合标签缺失但数据中存在结构的场景。它不适合直接替代监督分类：如果有可靠标签并且目标是预测类别，监督学习更直接。无监督结果的评估通常更困难，可能需要可视化、下游任务或人工判断。层次聚类、DBSCAN 和更系统的表示学习需要人工补充。

## 在 Machine Learning 中的位置

它在课程主线中位于监督学习和深度学习之后，扩展到“只给输入”的结构发现。它连接 [[clustering]]、[[k-means]]、[[principal-component-analysis]]、[[anomaly-detection]] 和 [[recommender-system]]。

## 重要公式 / 算法

- 公式 / 算法名称：K-means Objective
- 解决的问题：把样本分成距离中心较近的簇。
- 核心含义：$J=\frac{1}{m}\sum_i\lVert x^{(i)}-\mu_{c^{(i)}}\rVert^2$；$\mu$ 是中心，$c^{(i)}$ 是样本所属簇。
- 相关概念链接：[[k-means]]

- 公式 / 算法名称：PCA Projection
- 解决的问题：在保留主要信息的同时降维。
- 核心含义：笔记说明 PCA 寻找保留方差最多的低维主成分；通用矩阵公式需要人工补充。
- 相关概念链接：[[principal-component-analysis]]

- 公式 / 算法名称：Gaussian Density for Anomaly Detection
- 解决的问题：用低概率识别异常样本。
- 核心含义：$p(\vec{x})=\prod_i p(x_i;\mu_i,\sigma_i^2)$，若 $p(x_{test})<\epsilon$ 则判为异常。
- 相关概念链接：[[anomaly-detection]]

## 容易混淆点

- supervised learning vs unsupervised learning：前者有标签，后者没有标签。
- clustering vs classification：clustering 自行分组，classification 学习已知类别。
- PCA vs feature selection：PCA 构造新轴，feature selection 保留原始特征。
- anomaly detection vs classification：异常检测用低概率，可不依赖大量异常标签。

## 相关概念

- [[k-means]]
- [[principal-component-analysis]]
- [[anomaly-detection]]
- [[recommender-system]]
- [[feature-engineering]]

## 跨课程连接

- CS61A：体现从输入集合中抽象结构，而不是映射到给定标签。
- CS61B：聚类、降维和检索都依赖高维数据组织、距离计算和集合操作。
- CSAPP：大规模无标签数据处理受矩阵运算、内存布局和数值稳定性影响。
- UMich DL：连接 unsupervised representation learning、embedding 和 self-supervised 学习的前置概念。
