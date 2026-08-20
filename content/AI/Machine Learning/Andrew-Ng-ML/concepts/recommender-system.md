---
type: concept
course: Machine Learning
priority: B
status: draft
aliases: []
related: []
---

# Recommender System

## 一句话定义

recommender system 是根据用户、物品和交互数据预测偏好并排序候选物品的系统。它解决的是如何从稀疏评分或行为中推荐用户可能感兴趣的 item。

## 核心思想

推荐系统把“用户是否喜欢某个物品”转成一个预测问题。协同过滤从用户-item 评分表中同时学习用户参数和物品特征；内容过滤则用用户和物品本身特征生成向量，再用相似度或点积排序。

## 核心边界 / Objective / Assumption

设物品数 $n_m$、用户数 $n_u$、特征维度 $n$。评分矩阵可写为 $Y\in\mathbb{R}^{n_m\times n_u}$，$r(i,j)=1$ 表示用户 $j$ 评价了物品 $i$。协同过滤 model form：$\hat y^{(i,j)}=w^{(j)}\cdot x^{(i)}+b^{(j)}$，其中 $x^{(i)},w^{(j)}\in\mathbb{R}^n$。训练目标是在已评分位置最小化预测评分和真实评分差距，并加入正则化。

## 模型假设 / 局限

协同过滤适合有足够用户-item 交互的场景。它有冷启动问题：新用户或新物品缺少评分时很难学习表示。内容过滤可利用用户和物品特征缓解信息不足，但大规模候选集需要检索与排序分阶段处理。线上指标、召回策略和负采样需要人工补充。

## 在 Machine Learning 中的位置

推荐系统把 [[cost-function]]、[[regularization]]、向量相似度和 [[neural-network]] 连接到实际系统。它也展示了无监督/弱监督表示学习思想：item 特征可以是模型从评分几何结构中学到的潜在向量。

## 重要公式 / 算法

- 公式 / 算法名称：Collaborative Filtering Cost
- 解决的问题：从评分数据学习用户参数和物品特征。
- 核心含义：$J=\frac12\sum_{(i,j):r(i,j)=1}(w^{(j)}\cdot x^{(i)}+b^{(j)}-y^{(i,j)})^2+\text{regularization}$；只在已评分位置求和。
- 相关概念链接：[[collaborative-filtering]]、[[cost-function]]

- 公式 / 算法名称：Mean Normalization
- 解决的问题：避免新用户无评分时所有预测接近 0。
- 核心含义：对每个 item 减去均值 $\mu_i$，预测时加回 $\mu_i$。
- 相关概念链接：[[normalization]]

- 公式 / 算法名称：Content-based Dot Product
- 解决的问题：用用户向量和物品向量预测匹配程度。
- 核心含义：$\hat y^{(i,j)}=v_u^{(j)}\cdot v_m^{(i)}$；两向量维度必须一致。
- 相关概念链接：[[neural-network]]

## 容易混淆点

- collaborative filtering vs content-based filtering：前者依赖评分关系，后者依赖用户和物品特征。
- rating prediction vs ranking：预测评分不等于最终推荐排序系统。
- item feature vs learned embedding：协同过滤中的特征可能不可解释。
- cold start vs overfitting：冷启动是缺少交互数据，不是模型过拟合。

## 相关概念

- [[collaborative-filtering]]
- [[cost-function]]
- [[regularization]]
- [[neural-network]]
- [[normalization]]

## 跨课程连接

- CS61A：推荐可看作从 `(user_id, item_id)` 到评分或排序分数的函数。
- CS61B：稀疏矩阵、哈希索引、图关系、检索和排序是核心数据组织问题。
- CSAPP：大规模候选召回、预计算、向量点积和 cache 布局影响服务性能。
- UMich DL：连接 embedding、two-tower model、ranking loss 和 tensor shape。
