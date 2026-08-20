---
type: map
course: Machine Learning
status: draft
scope: concepts
aliases:
  - Machine Learning Concept Graph
---

# Machine Learning Knowledge Graph

## 主入口

这张图谱以 [[supervised-learning]] 为入口，沿着“模型 -> loss/cost -> optimization -> generalization”展开，再分支到 [[neural-network]]、[[unsupervised-learning]]、[[recommender-system]] 和 [[reinforcement-learning]]。

## 监督学习主干

- [[supervised-learning]] -> [[linear-regression]]
- [[linear-regression]] -> [[loss-function]]
- [[loss-function]] -> [[cost-function]]
- [[cost-function]] -> [[gradient-descent]]
- [[gradient-descent]] -> [[optimization]]
- [[optimization]] -> [[learning-rate]]

## 数据表示与优化稳定性

- [[linear-regression]] -> [[feature-scaling]]
- [[feature-scaling]] -> [[normalization]]
- [[feature-engineering]] -> [[linear-regression]]
- [[feature-engineering]] -> [[decision-boundary]]
- [[normalization]] -> [[principal-component-analysis]]
- [[normalization]] -> [[recommender-system]]

## 分类路径

- [[classification]] -> [[logistic-regression]]
- [[logistic-regression]] -> [[decision-boundary]]
- [[classification]] -> [[precision-recall]]
- [[classification]] -> [[softmax]]
- [[softmax]] -> [[loss-function]]
- [[decision-tree]] -> [[classification]]

## 泛化诊断

- [[train-dev-test-split]] -> [[bias-variance]]
- [[bias-variance]] -> [[overfitting]]
- [[bias-variance]] -> [[underfitting]]
- [[overfitting]] -> [[regularization]]
- [[overfitting]] -> [[data-augmentation]]
- [[transfer-learning]] -> [[overfitting]]
- [[regularization]] -> [[cost-function]]

## 神经网络路径

- [[neural-network]] -> [[forward-propagation]]
- [[forward-propagation]] -> [[activation-function]]
- [[forward-propagation]] -> [[loss-function]]
- [[loss-function]] -> [[backpropagation]]
- [[backpropagation]] -> [[gradient-descent]]
- [[backpropagation]] -> [[gradient-checking]]
- [[neural-network]] -> [[transfer-learning]]
- [[neural-network]] -> [[softmax]]

## 无监督学习路径

- [[unsupervised-learning]] -> [[k-means]]
- [[unsupervised-learning]] -> [[principal-component-analysis]]
- [[unsupervised-learning]] -> [[anomaly-detection]]
- [[unsupervised-learning]] -> [[recommender-system]]
- [[k-means]] -> [[cost-function]]
- [[principal-component-analysis]] -> [[normalization]]
- [[anomaly-detection]] -> [[feature-engineering]]

## 推荐系统路径

- [[recommender-system]] -> [[collaborative-filtering]]
- [[collaborative-filtering]] -> [[cost-function]]
- [[collaborative-filtering]] -> [[regularization]]
- [[collaborative-filtering]] -> [[normalization]]
- [[recommender-system]] -> [[neural-network]]

## 强化学习路径

- [[reinforcement-learning]] -> [[state-action-reward]]
- [[state-action-reward]] -> [[return]]
- [[return]] -> [[policy]]
- [[policy]] -> [[q-learning]]
- [[q-learning]] -> [[neural-network]]
- [[q-learning]] -> [[optimization]]

## 关键桥接节点

### [[cost-function]]

- 连接 [[linear-regression]]、[[loss-function]]、[[gradient-descent]]、[[regularization]]、[[k-means]]、[[collaborative-filtering]]
- 作用：把不同任务中的“模型好坏”变成可优化目标。

### [[optimization]]

- 连接 [[gradient-descent]]、[[learning-rate]]、[[backpropagation]]、[[q-learning]]
- 作用：把目标函数或 Bellman target 变成参数更新过程。

### [[bias-variance]]

- 连接 [[train-dev-test-split]]、[[overfitting]]、[[underfitting]]、[[regularization]]
- 作用：把训练结果转化为下一步工程决策。

### [[neural-network]]

- 连接 [[activation-function]]、[[forward-propagation]]、[[backpropagation]]、[[softmax]]、[[transfer-learning]]、[[q-learning]]
- 作用：把线性模型扩展为可学习中间表示的函数组合。

### [[unsupervised-learning]]

- 连接 [[k-means]]、[[principal-component-analysis]]、[[anomaly-detection]]、[[recommender-system]]
- 作用：统一“无标签结构发现”的几类任务。

### [[reinforcement-learning]]

- 连接 [[state-action-reward]]、[[return]]、[[policy]]、[[q-learning]]
- 作用：把静态预测扩展为序列决策和长期回报最大化。

## 复盘路线

1. [[supervised-learning]] -> [[linear-regression]] -> [[loss-function]] -> [[cost-function]] -> [[gradient-descent]]
2. [[feature-scaling]] -> [[normalization]] -> [[optimization]] -> [[learning-rate]]
3. [[classification]] -> [[logistic-regression]] -> [[decision-boundary]] -> [[precision-recall]] -> [[softmax]]
4. [[train-dev-test-split]] -> [[bias-variance]] -> [[overfitting]] -> [[underfitting]] -> [[regularization]]
5. [[neural-network]] -> [[forward-propagation]] -> [[activation-function]] -> [[backpropagation]] -> [[gradient-checking]]
6. [[unsupervised-learning]] -> [[k-means]] -> [[principal-component-analysis]] -> [[anomaly-detection]] -> [[recommender-system]]
7. [[reinforcement-learning]] -> [[state-action-reward]] -> [[return]] -> [[policy]] -> [[q-learning]]
