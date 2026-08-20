---
type: concept
course: Machine Learning
priority: C
status: draft
aliases: []
related: []
---

# Decision Tree

## 一句话定义

decision tree 是用一系列 if-else 式特征划分完成预测的模型。它解决的是如何在结构化表格数据上构造可解释的分段决策规则。

## 核心思想

树的每个内部节点选择一个特征划分样本，让子节点更“纯”。分类树用 entropy 和 information gain 选择划分；回归树把目标从减少熵换成减少方差。单棵树容易对数据微小变化敏感，因此笔记继续引出随机森林和 XGBoost。

## 核心边界 / Objective / Assumption

输入 $x\in\mathbb{R}^n$ 或混合类别特征，output 可以是类别 $\hat y$ 或连续预测。model form 是一棵树：内部节点是特征测试，叶节点给出类别或数值。训练 objective 不是梯度下降，而是递归选择划分，使 information gain 最大或节点方差下降最大。树的参数可理解为划分特征、阈值和叶节点预测。

## 模型假设 / 局限

decision tree 适合结构化表格数据，训练和推理较快，小树易解释。它不适合直接处理图像、音频等非结构化数据；笔记明确把这类任务更多交给 [[neural-network]]。单棵树 variance 高，常转向 random forest 或 XGBoost。XGBoost 的数学细节当前笔记未展开，需要人工补充。

## 在 Machine Learning 中的位置

它是监督学习中不同于线性模型和神经网络的一条分支。它连接 [[classification]]、[[overfitting]] 和模型选择，也说明不是所有模型都依赖 [[gradient-descent]]。

## 重要公式 / 算法

- 公式 / 算法名称：Entropy
- 解决的问题：衡量分类节点的不确定性。
- 核心含义：$H(p_1)=-p_1\log_2(p_1)-p_0\log_2(p_0)$，$p_1$ 是正类比例，$p_0=1-p_1$。
- 相关概念链接：[[classification]]

- 公式 / 算法名称：Information Gain
- 解决的问题：选择最能降低不确定性的划分。
- 核心含义：$IG=H(p_1^{root})-[w^{left}H(p_1^{left})+w^{right}H(p_1^{right})]$；$w$ 是左右分支样本比例。
- 相关概念链接：[[cost-function]]

- 公式 / 算法名称：Random Forest
- 解决的问题：降低单棵树对数据扰动的敏感性。
- 核心含义：有放回抽样训练多棵树，再投票；笔记提到 $B$ 可取 64 到 128，并可随机选择特征子集。
- 相关概念链接：[[overfitting]]

## 容易混淆点

- decision tree vs neural network：树适合表格数据且可解释，神经网络更适合非结构化数据和迁移学习。
- entropy vs information gain：entropy 衡量节点不确定性，information gain 衡量划分带来的下降。
- classification tree vs regression tree：前者减少熵，后者减少方差。
- random forest vs XGBoost：前者主要用 bagging，后者是 boosted trees；细节需要人工补充。

## 相关概念

- [[classification]]
- [[overfitting]]
- [[bias-variance]]
- [[feature-engineering]]

## 跨课程连接

- CS61A：树模型对应嵌套条件判断和递归划分。
- CS61B：直接连接树结构、递归遍历、集合划分和投票。
- CSAPP：树推理分支多，性能受分支预测、内存布局和 cache 行为影响。
- UMich DL：可作为神经网络在表格数据上的对照模型。
