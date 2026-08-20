---
type: concept
course: Machine Learning
priority: C
status: draft
aliases: []
related: []
---

# Return

## 一句话定义

return 是强化学习中从某个时刻开始累积未来奖励的长期目标。它解决的是单步 reward 不能表达序列决策长期好坏的问题。

## 核心思想

agent 的动作会影响未来状态，因此不能只看当前 reward。return 把未来奖励按折扣因子 $\gamma$ 汇总成一个标量，让 policy 和 Q-function 有共同的长期优化目标。笔记指出 $\gamma$ 表示对未来的重视程度，负奖励也会被折扣影响。

## 核心边界 / Objective / Assumption

在时刻 $t$，奖励序列为 $R_{t+1},R_{t+2},\dots$，return 定义为 $G_t=\sum_{k=0}^{\infty}\gamma^kR_{t+k+1}$，或终止时刻 $T$ 前的有限和。$G_t\in\mathbb{R}$ 是标量，$\gamma\in[0,1]$ 是 hyperparameter。强化学习的 objective 通常是最大化 expected return，而不是最小化单样本 loss。

## 模型假设 / 局限

return 适合有时间顺序和延迟奖励的任务。若每个样本独立且有正确标签，监督学习不需要 return。return 的质量依赖 reward 设计和 $\gamma$ 选择；reward 设计错误会让 agent 优化错误行为。state value function $V(s)$ 与 return 的严格关系需要人工补充。

## 在 Machine Learning 中的位置

它是 [[reinforcement-learning]] 的目标核心，连接 [[state-action-reward]]、[[policy]] 和 [[q-learning]]。Q-function 可理解为从某状态采取某动作后、按后续最优行为得到的长期 return。

## 重要公式 / 算法

- 公式 / 算法名称：Infinite-horizon Discounted Return
- 解决的问题：把无限未来奖励压缩成一个可比较的目标。
- 核心含义：$G_t=\sum_{k=0}^{\infty}\gamma^kR_{t+k+1}$；$R$ 是单步奖励，$\gamma$ 越小越不重视远期奖励。
- 相关概念链接：[[reinforcement-learning]]

- 公式 / 算法名称：Finite-horizon Return
- 解决的问题：处理有终止时刻的 episode。
- 核心含义：$G_t=\sum_{k=0}^{T-t-1}\gamma^kR_{t+k+1}$；$T$ 是终止时刻。
- 相关概念链接：[[state-action-reward]]

## 容易混淆点

- reward vs return：reward 是单步反馈，return 是折扣后的未来累计。
- return vs value function：return 是实际或目标累计量，value function 是对 return 的估计。
- return vs loss：return 在 RL 中通常要最大化，loss 在监督学习中通常要最小化。
- gamma vs learning rate：$\gamma$ 折扣未来奖励，$\alpha$ 控制参数更新步长。

## 相关概念

- [[reinforcement-learning]]
- [[state-action-reward]]
- [[policy]]
- [[q-learning]]

## 跨课程连接

- CS61A：return 是递归累计量，可用函数和递归定义表达。
- CS61B：episode 可看作状态路径，return 是路径上 reward 的加权聚合。
- CSAPP：长 episode 仿真和 reward 累计受数值精度与循环性能影响。
- UMich DL：连接 value estimation、policy optimization、DQN target 和 rollout。
