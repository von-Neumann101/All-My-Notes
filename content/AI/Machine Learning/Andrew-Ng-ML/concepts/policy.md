---
type: concept
course: Machine Learning
priority: B
status: draft
aliases: []
related: []
---

# Policy

## 一句话定义

policy 是强化学习中从状态到动作的决策规则。它解决的是 agent 在当前状态下应该选择哪个动作，才能让长期 return 尽可能大。

## 核心思想

[[reinforcement-learning]] 的最终产物不是单个预测值，而是一套行动策略。value function 或 Q-function 评估动作好坏，policy 负责真正选择动作。若 $Q(s,a)$ 已知，一个直接策略就是选择 Q 值最大的动作；训练时还需要探索，避免只利用当前不可靠估计。

## 核心边界 / Objective / Assumption

核心 model form 是 $\pi:s\to a$。输入 $s$ 是状态，可是离散编号或向量 $s\in\mathbb{R}^d$；输出 $a$ 来自动作空间 $\mathcal A$。确定性 policy 输出一个动作，随机 policy 输出动作分布，后者的标准定义需要人工补充。训练 objective 是最大化 expected return $G_t=\sum_{k=0}^{\infty}\gamma^kR_{t+k+1}$，而不是最小化单样本 loss。

## 模型假设 / 局限

policy 适合序列决策任务，其中动作会影响后续状态和 reward。若任务只是独立样本分类或回归，通常不需要 policy，而应使用监督学习模型。基于 Q 的 policy 依赖 $Q(s,a)$ 估计质量；若 Q 不准，贪心动作也可能很差。连续动作空间、随机策略和 policy gradient 的细节当前笔记不足，需要人工补充。

## 在 Machine Learning 中的位置

policy 位于强化学习主线的核心：state/action/reward 定义环境交互，return 定义长期目标，[[q-learning]] 或其他方法估计价值，policy 把价值估计转成行动。它和 [[optimization]] 的边界是，optimization 更新参数，policy 执行动作选择。

## 重要公式 / 算法

- 公式 / 算法名称：Policy Mapping
- 解决的问题：把状态映射为动作。
- 核心含义：$\pi:s\to a$；$s$ 是当前状态，$a$ 是被选择的动作。
- 相关概念链接：[[reinforcement-learning]]

- 公式 / 算法名称：Greedy Policy from Q
- 解决的问题：根据 Q-function 选择当前估计最优动作。
- 核心含义：$a=\arg\max_a Q(s,a)$；$Q(s,a)$ 是状态动作价值。
- 相关概念链接：[[q-learning]]

- 公式 / 算法名称：Epsilon-greedy Policy
- 解决的问题：在利用当前最优动作和随机探索之间权衡。
- 核心含义：以 $1-\epsilon$ 的概率选择当前最优动作，以 $\epsilon$ 的概率随机选择动作；$\epsilon$ 是 exploration rate。
- 相关概念链接：[[optimization]]

## 容易混淆点

- policy vs value function：policy 选择动作，value/Q-function 评估状态或动作的长期价值。
- reward vs return：policy 的目标是长期 return，不只是当前 reward。
- greedy vs epsilon-greedy：greedy 只利用当前估计，epsilon-greedy 保留探索。
- parameter vs hyperparameter：policy 参数可被学习，$\epsilon$ 通常是人为设定或调度的超参数。

## 相关概念

- [[reinforcement-learning]]
- [[q-learning]]
- [[return]]
- [[state-action-reward]]
- [[optimization]]

## 跨课程连接

- CS61A：policy 可看作状态输入到动作输出的函数，并用条件选择表达。
- CS61B：状态空间可以组织为图，policy 是在每个节点选择下一条边的规则。
- CSAPP：policy 执行、环境仿真和推理循环会受到延迟、内存和并行性能影响。
- UMich DL：是 policy learning、actor-critic、DQN action selection 和 tensorized rollout 的前置概念。
