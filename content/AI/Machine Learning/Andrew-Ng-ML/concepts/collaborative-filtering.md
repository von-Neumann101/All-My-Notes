---
type: concept
course: Machine Learning
priority: B
status: draft
aliases: []
related: []
---

# Collaborative Filtering

## 一句话定义

collaborative filtering 是从用户和 item 的交互或评分关系中同时学习用户偏好与 item 表示的推荐算法。它解决的是没有显式 item 特征时，如何只靠评分矩阵预测缺失偏好的问题。

## 核心思想

如果两个用户对很多 item 的评分相似，或两个 item 被相似用户喜欢，评分矩阵本身就包含潜在结构。协同过滤把这种结构参数化为用户向量和 item 向量，通过最小化已评分位置的预测误差学习二者，而不是人工指定每个 item 的特征。

## 核心边界 / Objective / Assumption

设用户数 $n_u$、物品数 $n_m$、潜在特征维度 $n$。评分矩阵 $Y\in\mathbb{R}^{n_m\times n_u}$，$r(i,j)=1$ 表示用户 $j$ 评价了 item $i$。model form 是 $\hat y^{(i,j)}=w^{(j)}\cdot x^{(i)}+b^{(j)}$，其中 $w^{(j)},x^{(i)}\in\mathbb{R}^n$，$b^{(j)}$ 是用户偏置。input 是已观测评分和 mask，parameter 是 $w,b,x$，output 是未评分 item 的预测分数。训练 objective 是在 $r(i,j)=1$ 的位置最小化 squared error，并加入 regularization。

## 模型假设 / 局限

它适合有足够历史交互的推荐场景。冷启动是核心局限：新用户或新 item 没有评分时，潜在向量难以学习。评分矩阵极稀疏、偏好快速变化或需要解释推荐理由时，也可能需要转向 content-based filtering、混合推荐或召回排序系统。矩阵分解视角和旋转不变性需要人工补充。

## 在 Machine Learning 中的位置

它属于推荐系统主线，连接 [[recommender-system]]、[[cost-function]]、[[regularization]] 和 [[normalization]]。与监督学习不同，它的训练数据不是普通 $(x,y)$ 样本，而是用户-item 二维关系中的已观测条目。

## 重要公式 / 算法

- 公式 / 算法名称：Collaborative Filtering Prediction
- 解决的问题：预测用户 $j$ 对 item $i$ 的评分。
- 核心含义：$\hat y^{(i,j)}=w^{(j)}\cdot x^{(i)}+b^{(j)}$；$w^{(j)}$ 是用户参数，$x^{(i)}$ 是 item 特征，二者 shape 都是 $\mathbb{R}^n$。
- 相关概念链接：[[recommender-system]]

- 公式 / 算法名称：Collaborative Filtering Cost
- 解决的问题：只在已评分位置学习用户和 item 表示。
- 核心含义：$J(w,b,x)=\frac12\sum_{(i,j):r(i,j)=1}(w^{(j)}\cdot x^{(i)}+b^{(j)}-y^{(i,j)})^2+\frac{\lambda}{2}\sum_j\sum_k(w_k^{(j)})^2+\frac{\lambda}{2}\sum_i\sum_k(x_k^{(i)})^2$。
- 相关概念链接：[[cost-function]]、[[regularization]]

- 公式 / 算法名称：Mean Normalization
- 解决的问题：避免新用户全 0 评分导致预测不合理。
- 核心含义：对 item 评分减去均值 $\mu_i$，预测时加回均值；完整矩阵形式需要人工补充。
- 相关概念链接：[[normalization]]

## 容易混淆点

- collaborative filtering vs content-based filtering：前者依赖评分关系，后者依赖用户和 item 本身特征。
- item feature vs user parameter：协同过滤中二者都可以被学习。
- missing rating vs zero rating：没有评分不等于评分为 0，需要用 $r(i,j)$ mask。
- regularization vs mean normalization：前者控制参数大小，后者调整评分基准。

## 相关概念

- [[recommender-system]]
- [[cost-function]]
- [[regularization]]
- [[normalization]]

## 跨课程连接

- CS61A：可看作从 `(user, item)` 到 rating 的二元函数映射。
- CS61B：评分矩阵稀疏，适合用稀疏结构、图关系、索引和检索组织数据。
- CSAPP：大规模矩阵计算受内存布局、cache、稀疏访问和向量化性能影响。
- UMich DL：连接 embedding、representation learning、two-tower model 和 ranking loss。
