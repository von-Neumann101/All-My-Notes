---
type: concept
course: Machine Learning
priority: A
status: draft
aliases: []
related: []
---

# Optimization

## 一句话定义

optimization 是用算法寻找能让 objective 更小或更好的参数的过程。它解决的是从 [[cost-function]] 到可执行训练步骤之间的桥接问题。

## 核心思想

机器学习模型先定义 objective，再计算 gradient，最后按 update rule 改参数。[[gradient-descent]] 是最基础的优化方法，Adam、mini-batch 和自动微分是更实际的训练工具。optimization 关注训练目标怎么变好，但不等同于 generalization。

## 核心边界 / Objective / Assumption

以监督学习为例，$X\in\mathbb{R}^{m\times n}$、参数 $\theta$、objective $J(\theta)$。gradient 是 $\nabla_\theta J$，update rule 例如 $\theta\leftarrow \theta-\alpha\nabla_\theta J$，learning rate $\alpha$ 是 hyperparameter。优化目标下降说明训练过程在推进，但 dev/test 表现需要另外评估。

## 模型假设 / 局限

optimization 适用于 objective 可计算、梯度可得或可近似的模型。简单凸问题可能有稳定收敛性质；神经网络等复杂模型可能对学习率、初始化、batch size 和正则化敏感。若训练目标和真实任务指标不一致，优化再好也可能不是想要的模型。

## 在 Machine Learning 中的位置

它位于 [[cost-function]] 之后、模型训练过程之中。线性回归用梯度下降或 closed-form；逻辑回归和神经网络通常依赖迭代优化；强化学习中的 DQN 也用神经网络近似和优化 target。

## 重要公式 / 算法

- 公式 / 算法名称：Gradient Descent
- 解决的问题：沿负梯度方向降低 objective。
- 核心含义：$\theta\leftarrow\theta-\alpha\nabla_\theta J$；$\theta$ 是参数向量，$\alpha$ 是 learning rate。
- 相关概念链接：[[gradient-descent]]

- 公式 / 算法名称：Adam
- 解决的问题：自动调整学习率相关行为。
- 核心含义：index.md 只说明 Adam 自动调整 $\alpha$ 并在 TensorFlow compile 中可选；动量和二阶矩公式需要人工补充。
- 相关概念链接：[[learning-rate]]

- 公式 / 算法名称：Mini-batch
- 解决的问题：用数据子集近似全量梯度。
- 核心含义：index.md 在强化学习处说明 mini-batch 每次取数据子集训练，速度更快但更嘈杂。
- 相关概念链接：[[gradient-descent]]

## 容易混淆点

- objective vs gradient：objective 是目标函数，gradient 是它对参数的变化率。
- gradient vs update rule：gradient 给方向，update rule 决定如何改参数。
- optimization vs generalization：训练目标下降不保证新数据表现好。
- parameter vs hyperparameter：参数被训练更新，学习率等由人为选择。

## 相关概念

- [[cost-function]]
- [[gradient-descent]]
- [[backpropagation]]
- [[learning-rate]]
- [[regularization]]

## 跨课程连接

- CS61A：optimization 是迭代改进过程，每一步用当前状态生成更好的状态。
- CS61B：mini-batch 和大规模训练涉及数据组织、复杂度和批处理。
- CSAPP：训练速度受浮点误差、内存布局、cache、并行和向量化性能影响。
- UMich DL：对应 optimizer、autograd、learning rate schedule、batch size 和 tensor shape。
