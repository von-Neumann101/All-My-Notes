---
type: concept
course: Machine Learning
priority: B
status: draft
aliases: []
related: []
---

# Q Learning

## 一句话定义

Q-learning 是学习状态-动作价值函数 $Q(s,a)$ 的强化学习方法。它解决的是如何估计在某个状态采取某个动作后，长期能获得多少回报。

## 核心思想

如果知道每个动作的 $Q(s,a)$，policy 就可以选择价值最大的动作。Bellman equation 把当前奖励和后继状态的最优未来价值连接起来，使模型可以用一步经验逐步逼近长期价值。

## 核心边界 / Objective / Assumption

输入是状态 $s$ 和动作 $a$，输出是标量 $Q(s,a)$。若动作空间大小为 $|\mathcal A|$，DQN 可输入状态向量 $s\in\mathbb{R}^d$，输出 $Q(s,\cdot)\in\mathbb{R}^{|\mathcal A|}$。训练 target 是 $y=R(s)+\gamma\max_{a'}Q(s',a')$。objective 通常是让 $Q_{new}(s,a)\approx y$；具体 squared TD loss 公式需要人工补充。

## 模型假设 / 局限

Q-learning 适合能定义状态、动作、奖励和后继状态的任务。DQN 适合离散动作空间；连续动作空间通常需要其他方法，具体需要人工补充。它对探索策略、replay buffer、target 更新和超参数敏感，不保证训练稳定。

## 在 Machine Learning 中的位置

它是 [[reinforcement-learning]] 中从 return 到可训练函数近似的桥梁。笔记中 DQN 把 $Q$ 当作神经网络近似，用 tuple $(s,a,R(s),s')$ 构造训练样本，再用 [[optimization]] 训练。

## 重要公式 / 算法

- 公式 / 算法名称：Q-function
- 解决的问题：衡量状态动作对的长期价值。
- 核心含义：$Q(s,a)=G_t$ if start in $s$, take $a$, then behave optimally；准确说是 $Q^*$ 的描述。
- 相关概念链接：[[return]]

- 公式 / 算法名称：Bellman Equation
- 解决的问题：用当前奖励和未来价值递归定义 $Q$。
- 核心含义：$Q(s,a)=R(s)+\gamma\max_{a'}Q(s',a')$；随机环境中用期望。
- 相关概念链接：[[reinforcement-learning]]

- 公式 / 算法名称：DQN Target
- 解决的问题：构造神经网络训练目标。
- 核心含义：$x=(s,a)$，$y=R(s)+\gamma\max_{a'}Q(s',a')$；训练 $Q_{new}(s,a)\approx y$。
- 相关概念链接：[[neural-network]]、[[optimization]]

## 容易混淆点

- Q-function vs policy：Q 衡量价值，policy 根据 Q 选动作。
- reward vs Q-value：reward 是当前反馈，Q-value 包含未来回报。
- exploration vs exploitation：epsilon-greedy 在随机探索和最大 Q 动作之间权衡。
- Q-learning vs DQN：DQN 用神经网络近似 Q，tabular 更新公式需要人工补充。

## 相关概念

- [[reinforcement-learning]]
- [[policy]]
- [[return]]
- [[neural-network]]
- [[optimization]]

## 跨课程连接

- CS61A：Bellman 形式是递归价值定义，policy 是状态到动作的函数。
- CS61B：状态空间、动作转移和 replay buffer 都可联系图与队列/缓冲区数据结构。
- CSAPP：DQN 训练循环、buffer 采样和神经网络推理受内存布局和性能影响。
- UMich DL：连接 DQN、target network、autograd、optimizer 和 batch tensor shape。
