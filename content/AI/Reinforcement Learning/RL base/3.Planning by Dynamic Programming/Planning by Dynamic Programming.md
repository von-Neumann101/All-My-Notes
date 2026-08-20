# Introduction
Dynamic 指的是具有序列结构或时间结构的问题，Programming 指的是策略（某种需要被优化的东西）
动态规划可以将问题拆解为子问题，通过**解决子问题并将之合并**以得到问题的解法
## Requirements for DP
DP能够解决的问题满足下面的两个性质：
- 最优子结构（必要）：问题分为的**子问题的最优解会描述如何获得问题的最优解**
- 重叠子问题（可无）：子问题的解法会被反复使用（这和效率有关）

MDP就符合上面的两个条件——**Bellman Equation**就描述了一种子问题的分解，并且价值函数存储了子问题的解法（某个状态的最优价值）
## Planning by DP
DP可以：
- prediction：给定一个MDP和策略$\pi$或者一个MRP，DP可以输出任**何状态的价值函数**$v_\pi(s)$
- control：给定一个MDP，输出最优价值函数$v_*$和最优策略$\pi_*$
# Policy Evaluation
## Iterative Policy Evaluation
**问题**：*评估* 一个给定的策略
解法：迭代贝尔曼期望方程
$v_1\to v_2\to\cdots\to v_\pi$（这里的$v$是一个向量，表示MDP所有状态的价值）
使用**同步backup**：对于每次迭代$k+1$，对于每个状态$s\in\mathcal S$，用$v_k(s')$更新$v_{k+1}(s)$
初始的$v_1$为0，最终$v_k$会收敛到$v_\pi$

![[Pasted image 20260807142133.png|326]]
$$
v _ { k + 1 } ( s ) = \sum _ { a \in \mathcal { A } } \pi ( a | s ) \left( \mathcal { R } _ { s } ^ { a } + \gamma \sum _ { s ^ { \prime } \in \mathcal { S } } \mathcal { P } _ { s s ^ { \prime } } ^ { a } v _ { k } ( s ^ { \prime } ) \right)
$$
注意，每一个State都会在一次迭代中作为根节点（顺序没有规定）
### Example: Small Gridworld
![[Pasted image 20260807143419.png|396]]
规则：导致超过边界的动作不会改变State（不会收到奖励），到达灰色块时停止。$\gamma=1$
**Policy**：
$$\pi(n\mid \cdot)=\pi(e\mid \cdot)=\pi(s\mid \cdot)=\pi(w\mid \cdot)=0.25$$

**过程**：
![[Pasted image 20260807151845.png|476]]

![[Pasted image 20260807151854.png|468]]
右边那个grid只是一个贪心策略（其实可以忽略右边的图，这是给下面那一节用的），我们这里进行仅仅是对随机策略$\pi$的$v_\pi$估计
## Improve a Policy
给定一个策略$\pi$，先Evaluate Policy（使用贝尔曼期望方程）：
$$v_\pi(s)=\mathbb E[R_{t+1}+\gamma R_{t+2}+...\mid S_t=s]$$
然后只需要以贪心策略更新$\pi$即可：
$$
\pi'=\text{greedy}(v_\pi)
$$
无论初始的$v_0,\pi_0$是什么，Policy Iteration的过程**总会使得初始策略$\pi_0$收敛到最佳策略$\pi_*$**，同时也会得到最优价值函数$v_*(s)$
### Example: Car Rental
**规则**：
![[Pasted image 20260807155838.png|564]]

**Policy Iteration**：
![[Pasted image 20260807165252.png|575]]
这里横坐标是第二个位置的车数，纵坐标是第一个位置的车数。图中的数字是调给位置2的车数
### Policy Improvement
证明贪心策略：
$$
\pi ^ { \prime } ( s ) = \underset { a \in \mathcal { A } } { \operatorname { a r g m a x } } \; q _ { \pi } ( s, a )
$$
是最优的

由于
$$
q _ { \pi } ( s, \pi ^ { \prime } ( s ) ) = \operatorname* { m a x } _ { a \in \mathcal { A } } q _ { \pi } ( s, a ) \geq q _ { \pi } ( s, \pi ( s ) ) = v _ { \pi } ( s )
$$
所以
$$
\begin{aligned}
v _ { \pi } ( s ) &\leq q _ { \pi } ( s, \pi ^ { \prime } ( s ) ) = \mathbb { E } _ { \pi ^ { \prime } } \left[ R _ { t + 1 } + \gamma v _ { \pi } ( S _ { t + 1 } ) \mid S _ { t } = s \right] \\
&\leq \mathbb { E } _ { \pi ^ { \prime } } \left[ R _ { t + 1 } + \gamma q _ { \pi } ( S _ { t + 1 }, \pi ^ { \prime } ( S _ { t + 1 } ) ) \mid S _ { t } = s \right] \\
&\leq \mathbb { E } _ { \pi ^ { \prime } } \left[ R _ { t + 1 } + \gamma R _ { t + 2 } + \gamma ^ { 2 } q _ { \pi } ( S _ { t + 2 }, \pi ^ { \prime } ( S _ { t + 2 } ) ) \mid S _ { t } = s \right] \\
&\leq \mathbb { E } _ { \pi ^ { \prime } } \left[ R _ { t + 1 } + \gamma R _ { t + 2 } +... \ | \ S _ { t } = s \right] = v _ { \pi ^ { \prime } } ( s )
\end{aligned}
$$
这里$\mathbb E_{\pi'}$指的是**当前的Action**采样于$\pi'$，那么为什么最后的式子成立呢？
> 因为每次我们都会把$v_\pi$放缩为$q_\pi(s,\pi'(s))$，而这一步需要我们把当前State的Action替换为$\pi'(s)$。可以看到$S_{t+1}$的Action被替换为了$\pi'(S_{t+1})$，我们无限地进行下去，就得到了**在未来的每一步都做$\pi'(s)$的Action**的价值——这即是$v_{\pi'}(s)$

如果贪心策略停止，那么最终
$$v_\pi(s)=q_\pi(s,\pi(s))=\operatorname* { m a x } _ { a \in \mathcal { A } }\ q_\pi(s,a)=q_\pi(s,\pi'(s))\Rightarrow v_\pi(s)=\operatorname* { m a x } _ { a \in \mathcal { A } }\ q_\pi(s,a)\ (\text{Bellman Optimal Equation})$$
### Modified Policy Iteration
一般来说，并不需要运行的到无穷次才能得到Optimal Policy，在之前的Grid World中，4次Bellman Expectation Equation的迭代所得到的$v_4$就**足够给出最佳的Policy**。**我们不必到无限次，等到$v_0$收敛到$v_\pi$才使用Greedy**，也就是
$$\pi'=\text{greedy}(v_k)\quad 1<k<\infty$$

或者，当value function的变化小于$\epsilon$时停止iteration
# Value Iteration
## 优化原理
一个最优策略可以被划分为两部分
- 最优的第一个动作
- 紧接着从后继状态进行最优策略

最优子结构描述了：**一个策略从 s 开始是最优的，当且仅当沿着这个策略可能到达的所有后续状态 s′ 上，它之后的策略也都是最优的**
## Deterministic Value Iteration
**Alg**：
- **如果子问题已知，即$v_*(s')$已知（有人说了从某个状态开始的最佳价值）**
- 那么$v_*(s)\longleftarrow \operatorname* { m a x } _ { a \in \mathcal { A } }[\mathcal R_s^a+\gamma\sum_{s'\in \mathcal S}\mathcal P_{ss'}^av_*(s')]$
### Example: Shortest Path
![[Pasted image 20260808113701.png|536]]
$v_1$可以是任意初始化，无论任何的初始化，最终一定会收敛
## Value Iteration in MDPs
**问题**：找最优策略$\pi_*$
**Alg**：每一次迭代，对于所有的states，从$v_k(s')$更新$v_{k+1}(s)$
$$
v _ { k + 1 } ( s ) = \operatorname* { m a x } _ { a \in \mathcal { A } } \; \left( \mathcal { R } _ { s } ^ { a } + \gamma \sum _ { s ^ { \prime } \in \mathcal { S } } \mathcal { P } _ { s s ^ { \prime } } ^ { a } v _ { k } ( s ^ { \prime } ) \right)
$$
### Practice
$\gamma=1$，撞墙的奖励$<0$
![[Pasted image 20260808140357.png|333]]
![[Pasted image 20260808143423.png|333]]
![[Pasted image 20260808143440.png|333]]
![[Pasted image 20260808143453.png|334]]
![[Pasted image 20260808143539.png|330]]
## Summary 
![[Pasted image 20260808143651.png]]
需要仔细地思考Policy Iteration和Value Iteration的直接的区别，事实上当$k=1$的时候，Modified Policy Iteration就是Value Iteration
# Extensions to Dynamic Programming
## In-Place DP
之前的$v_{k+1}(s)$需要$v_k(s')$来更新，我们可以直接在同一个$v$中更新
思考：抛开效率不谈，两种方法有什么不同，在什么情况下差别会很大？（事实上，他们的结果是一样的）
## Prioritised Sweeping
之前的算法中，我们并未要求更新的顺序，但是对于某些情况（比如奖励稀疏），随机顺序可能需要计算大量的0，这是对算力的浪费——真正影响最终value function是变化量大的状态价值

所以我们按照Bellman error来指导更新的顺序（使用优先队列来实现）
$$
\big|\operatorname* { m a x } _ { a \in \mathcal { A } }\big(\cal R_s^a+\gamma\sum_{s'\in\cal S}\cal P_{ss'}^av
\big(s\big)'\big)-v\big(s\big)\big|
$$
## Real-Time DP
让Agent自行探索环境，每个时间步获得$S_t,A_t,R_{t+1}$
$$
v  ( S_t ) = \operatorname* { m a x } _ { a \in \mathcal { A } } \; \left( \mathcal { R } _ { S_t } ^ { a } + \gamma \sum _ { s ^ { \prime } \in \mathcal { S } } \mathcal { P } _ { S_t s ^ { \prime } } ^ { a } v _ { k } ( s ^ { \prime } ) \right)
$$
也就是说，Agent走哪就更新哪（注意，这里仍然是MDP，Agent知道环境的所有信息，自然也知道$S_t$的所有后继及其信息）
## Full-Width Backup
我们注意到，之前的DP我们需要穷尽所有的可能性——每一个动作，每一个状态转移，这会导致维度灾难，大型问题几乎无法通过这种方法解决。
为了解决这个问题，我们使用Sample Backup，我们每次只采样一种动作，采样一种状态转移，这会极大地减少情况数
多次采样以后，我们可以近似出Full-Width Backup的结果
# 压缩映射
[[Reinforcement Learning/RL base/3.Planning by Dynamic Programming/lecture-3-planning-by-dynamic-programming-.pdf#page=35|lecture-3-planning-by-dynamic-programming-, 页面 35]]
