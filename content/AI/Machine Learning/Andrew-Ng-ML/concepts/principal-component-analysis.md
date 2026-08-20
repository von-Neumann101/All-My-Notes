---
type: concept
course: Machine Learning
priority: B
status: draft
aliases: []
related: []
---

# Principal Component Analysis

## 一句话定义

PCA 是通过寻找保留最大方差的低维方向来压缩数据的降维方法。它解决的是如何在尽量少损失信息的情况下减少特征维度，常用于可视化。

## 核心思想

高维数据可能有冗余维度。PCA 寻找新的坐标轴，让样本投影到这些轴上后尽量分散，也等价于尽量减小重构误差。它不是拟合标签，而是在无标签数据中寻找压缩信息的方向。

## 核心边界 / Objective / Assumption

设 $X\in\mathbb{R}^{m\times n}$，$m$ 是样本数，$n$ 是原始特征数。PCA 选择 $k<n$ 个主成分，把样本投影到低维表示 $Z\in\mathbb{R}^{m\times k}$，再可从 $Z$ 近似重构原数据。当前笔记说明需要先归一化，使均值在原点；通用矩阵公式、协方差矩阵和 SVD 需要人工补充。

## 模型假设 / 局限

PCA 适合数据主要变化方向能由线性子空间表示的降维任务。它不使用标签，不适合直接做监督预测；它也不同于 feature selection，因为它创建新轴而不是直接选择原始特征。若目标是分类性能而非可视化或压缩，需要验证降维后是否损失关键信息。

## 在 Machine Learning 中的位置

PCA 属于 [[unsupervised-learning]] 和 dimensionality reduction。它与 [[feature-scaling]] 相关，因为笔记要求先归一化；它与 [[linear-regression]] 容易混淆，但 PCA 找的是保留信息的投影方向，不是预测 $y$ 的拟合线。

## 重要公式 / 算法

- 公式 / 算法名称：Principal Component Direction
- 解决的问题：寻找保留信息最多的低维方向。
- 核心含义：选择使投影方差最大的轴；具体协方差矩阵和特征向量公式需要人工补充。
- 相关概念链接：[[unsupervised-learning]]

- 公式 / 算法名称：Projection
- 解决的问题：把高维样本压缩到低维。
- 核心含义：将 $x^{(i)}\in\mathbb{R}^n$ 投影到 $k$ 个主成分上，得到低维表示；矩阵形式需要人工补充。
- 相关概念链接：[[dimensionality-reduction]]

- 公式 / 算法名称：Reconstruction
- 解决的问题：从低维表示近似还原原数据。
- 核心含义：index.md 提到投影长度乘以主成分单位向量可重构，误差来自原点到主成分的距离。
- 相关概念链接：[[feature-scaling]]

## 容易混淆点

- PCA vs linear regression：PCA 不预测标签，linear regression 预测 $y$。
- PCA vs feature selection：PCA 创建新轴，feature selection 保留原始特征。
- projection vs reconstruction：投影是压缩，重构是从压缩表示近似还原。
- visualization vs prediction：PCA 常用于可视化，不保证监督任务性能更好。

## 相关概念

- [[unsupervised-learning]]
- [[feature-scaling]]
- [[dimensionality-reduction]]
- [[linear-regression]]

## 跨课程连接

- CS61A：可联系抽象和信息压缩，把复杂输入映射到低维表示。
- CS61B：高维样本矩阵需要合适的数据组织和批量处理。
- CSAPP：PCA 涉及矩阵运算、浮点误差、内存布局和数值稳定性。
- UMich DL：连接 representation、embedding 可视化、tensor shape 和矩阵化实现。
