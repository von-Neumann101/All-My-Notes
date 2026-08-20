---
type: concept
course: Machine Learning
priority: B
status: draft
aliases: []
related: []
---

# Reinforcement Learning

## 一句话定义

reinforcement learning 是让智能体在状态中选择动作，并通过奖励学习长期更好策略的框架。它解决的是有延迟回报的序列决策问题，而不是单步输入输出预测。

## 核心思想

监督学习依赖正确标签，强化学习依赖环境反馈的 reward。智能体不只关心当前一步奖励，还要最大化折扣后的长期 return，因此策略选择必须考虑当前动作对未来状态和奖励的影响。

## 核心边界 / Objective / Assumption

核心 model form 是 policy：$\pi:s\to a$。状态 $s$ 可是标量、离散状态或向量；例如月球着陆器状态可写为 $s\in\mathbb{R}^8$。动作 $a$ 来自动作空间，reward $R$ 是标量。训练 objective 是最大化 expected return：$G_t=\sum_{k=0}^{\infty}\gamma^kR_{t+k+1}$，其中 $\gamma\in[0,1]$ 是折扣因子。

## 模型假设 / 局限

强化学习适用于动作会影响未来状态、奖励有延迟的任务。它通常需要可交互环境、奖励函数和大量试错，对超参数敏感，训练成本可能很高。若存在大量带正确标签的独立样本，监督学习通常更直接。agent-environment loop 的标准图式需要人工补充。

## 在 Machine Learning 中的位置

它把课程主线从静态预测推进到序列决策。[[q-learning]]、Bellman equation、DQN、epsilon-greedy 和 replay buffer 都建立在状态、动作、奖励和 return 之上。

## 重要公式 / 算法

- 公式 / 算法名称：Policy
- 解决的问题：根据当前状态选择动作。
- 核心含义：$\pi:s\to a$；$s$ 是状态，$a$ 是动作。
- 相关概念链接：[[policy]]

- 公式 / 算法名称：Return
- 解决的问题：把未来奖励汇总成长期目标。
- 核心含义：$G_t=\sum_{k=0}^{\infty}\gamma^kR_{t+k+1}$；$\gamma$ 越小越不重视远期奖励。
- 相关概念链接：[[return]]

- 公式 / 算法名称：Markov Property
- 解决的问题：简化未来状态依赖。
- 核心含义：$P(X_{t+1}|X_t,\dots,X_0)=P(X_{t+1}|X_t)$；未来只依赖当前状态。
- 相关概念链接：[[q-learning]]

## 容易混淆点

- reward vs return：reward 是单步反馈，return 是折扣后的长期累计。
- policy vs value function：policy 选动作，value/Q 衡量长期价值。
- supervised learning vs reinforcement learning：前者有标签，后者通过环境奖励学习。
- optimization vs exploration：优化已有估计不等于充分探索环境。

## 相关概念

- [[q-learning]]
- [[policy]]
- [[return]]
- [[state-action-reward]]
- [[optimization]]

## 跨课程连接

- CS61A：策略函数、状态转移和递归价值定义都可用函数抽象表达。
- CS61B：状态空间可看作图，动作是边，搜索和动态规划思想相关。
- CSAPP：环境仿真、replay buffer 和训练循环会受到内存和性能限制。
- UMich DL：连接 deep RL、DQN、policy/value methods、tensorized environment batches。
