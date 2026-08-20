---
type: concept
course: Machine Learning
priority: B
status: draft
aliases: []
related: []
---

# K Means

## 一句话定义

K-means 是把无标签样本按距离划分为 $K$ 个簇的聚类算法。它解决的是没有标签时，如何用数据本身的几何结构分组。

## 核心思想

K-means 交替做两件事：把每个样本分配给最近的聚类中心，再把每个中心更新为该簇样本均值。每一步都让失真函数不增，因此算法逐步收敛到一个局部结果。

## 核心边界 / Objective / Assumption

设 $X\in\mathbb{R}^{m\times n}$，第 $i$ 个样本 $x^{(i)}\in\mathbb{R}^n$，簇数为 $K$，中心 $\mu_k\in\mathbb{R}^n$，分配 $c^{(i)}\in\{1,\dots,K\}$。objective 是失真函数 $J(c,\mu)=\frac{1}{m}\sum_{i=1}^{m}\lVert x^{(i)}-\mu_{c^{(i)}}\rVert^2$。$K$ 是 hyperparameter。

## 模型假设 / 局限

K-means 适用于用欧氏距离能表达相似性的聚类任务。它不使用标签，不适合直接做分类；对初始中心敏感，可能收敛到局部最小；簇数 $K$ 需要人为选择。若簇形状复杂、密度差异大或距离度量不合适，需要考虑其他聚类方法，具体需要人工补充。

## 在 Machine Learning 中的位置

它是 [[unsupervised-learning]] 的核心例子，与 [[classification]] 的区别是没有标签。它也展示了 cost/objective 不只属于监督学习：无监督学习同样可以定义目标函数并迭代优化。

## 重要公式 / 算法

- 公式 / 算法名称：K-means Distortion Function
- 解决的问题：衡量样本到所属簇中心的距离平方。
- 核心含义：$J=\frac{1}{m}\sum_{i=1}^{m}\lVert x^{(i)}-\mu_{c^{(i)}}\rVert^2$；$m$ 是样本数，$\mu_{c^{(i)}}$ 是样本所属簇中心。
- 相关概念链接：[[cost-function]]

- 公式 / 算法名称：Assignment Step
- 解决的问题：确定每个样本属于哪个簇。
- 核心含义：固定中心，把样本分配给最近的 $\mu_k$。
- 相关概念链接：[[clustering]]

- 公式 / 算法名称：Centroid Update Step
- 解决的问题：更新簇中心。
- 核心含义：固定分配，把 $\mu_k$ 更新为该簇样本均值。
- 相关概念链接：[[optimization]]

## 容易混淆点

- K-means vs classification：K-means 无标签，classification 有标签。
- cluster center vs data point：中心是簇的代表位置，不一定是原始样本。
- K vs parameter：$K$ 是超参数，中心 $\mu_k$ 是算法学习出的量。
- global optimum vs local optimum：不同初始化可能得到不同结果。

## 相关概念

- [[unsupervised-learning]]
- [[clustering]]
- [[cost-function]]
- [[optimization]]

## 跨课程连接

- CS61A：算法是重复应用“分配-更新”的迭代改进。
- CS61B：需要存储样本、簇分配和中心，涉及批量数据处理和最近中心搜索复杂度。
- CSAPP：距离计算和中心更新是批量向量运算，受 cache、内存布局和 SIMD 影响。
- UMich DL：可作为无监督表示学习和 embedding 可视化的前置概念。
