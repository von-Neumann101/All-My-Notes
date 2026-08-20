---
type: concept
course: Machine Learning
priority: C
status: draft
aliases: []
related: []
---

# State Action Reward

## 一句话定义

state、action、reward 是强化学习描述环境交互的三个基本对象。它们解决的是如何把序列决策问题拆成“当前处境、可选行为、环境反馈”。

## 核心思想

监督学习样本通常是 $(x,y)$，强化学习经验更像 $(s,a,R,s')$。agent 在 state $s$ 下选择 action $a$，环境返回 reward 并转移到后继 state $s'$。这些 tuple 构成 Q-learning 和 DQN 的训练材料。

## 核心边界 / Objective / Assumption

状态 $s$ 可以是离散编号或向量；笔记中的月球着陆器状态可写作 $s\in\mathbb{R}^8$，包含位置、速度、角度和腿部接触等信息。动作 $a\in\mathcal A$，月球着陆器示例有四个离散 action。reward $R$ 是标量反馈，笔记常写作 $R(s)$。单步 tuple 可写为 $(s^{(k)},a^{(k)},R(s^{(k)}),s'^{(k)})$。

## 模型假设 / 局限

这组概念适用于动作会改变后续状态的任务。若数据样本彼此独立且标签已知，不需要构造成 state-action-reward。它通常假设当前 state 足够描述决策所需信息，Markov property 的完整建模需要人工补充。reward 稀疏、延迟或设计错误都会让学习困难。

## 在 Machine Learning 中的位置

它是 [[reinforcement-learning]] 的输入语言，向上连接 [[return]] 和 [[policy]]，向下连接 DQN 的 replay tuple。[[q-learning]] 使用 $s,a,R,s'$ 构造 Bellman target。

## 重要公式 / 算法

- 公式 / 算法名称：Experience Tuple
- 解决的问题：记录一次环境交互。
- 核心含义：$(s,a,R,s')$；$s$ 是当前状态，$a$ 是动作，$R$ 是奖励，$s'$ 是后继状态。
- 相关概念链接：[[q-learning]]

- 公式 / 算法名称：Bellman Target Inputs
- 解决的问题：从交互数据构造 Q-learning 训练目标。
- 核心含义：$y=R(s)+\gamma\max_{a'}Q(s',a')$；需要当前 reward 和后继状态 $s'$。
- 相关概念链接：[[return]]

- 公式 / 算法名称：Markov Property
- 解决的问题：简化未来状态依赖。
- 核心含义：$P(X_{t+1}|X_t,\dots,X_0)=P(X_{t+1}|X_t)$；笔记有定义，但完整 MDP 框架需要人工补充。
- 相关概念链接：[[reinforcement-learning]]

## 容易混淆点

- state vs observation：当前笔记未系统区分，需人工补充。
- action vs policy：action 是单次选择，policy 是选择动作的规则。
- reward vs return：reward 是单步反馈，return 是长期累计。
- state-action tuple vs supervised sample：tuple 中的 target 依赖 Bellman 更新，不是直接给定标签。

## 相关概念

- [[reinforcement-learning]]
- [[return]]
- [[policy]]
- [[q-learning]]

## 跨课程连接

- CS61A：状态转移和动作选择可用函数抽象描述。
- CS61B：状态空间可以组织为图，action 是边，tuple 可存入 replay buffer。
- CSAPP：仿真环境、buffer 存储和批量采样受内存与性能影响。
- UMich DL：连接 DQN replay buffer、batch tensor shape 和 environment rollout。
