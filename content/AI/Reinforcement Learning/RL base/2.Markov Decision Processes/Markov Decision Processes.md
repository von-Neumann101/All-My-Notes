# Markov Processes
## 定义
**定义**：一个状态为Markov状态，当且仅当
$$
\Pr[S_{t+1}\mid S_t]=\Pr[S_{t+1}\mid S_1,...,S_t]
$$

**State Transition Matrix**：对于一个Markov状态 $s$ 与他的后继状态 $s'$ ，*状态转移概率* 为$\mathcal P_{ss'}=\Pr[S_{t+1}=s'\mid S_t=s]$，**状态转移矩阵**为
$$
\begin{bmatrix}
P_{11} & \cdots & P_{1n}\\
\vdots&&\vdots\\ 
P_{n1} & \cdots & P_{nn}
\end{bmatrix}
$$
其中矩阵每一行和为1（从一个状态去往全部可能的状态的概率之和）

**Markov Process**：
**Markov过程**（Markov链）是一个**无记忆随机过程**，被定义为一个二元组$\left<\mathcal S,\mathcal P\right>$，满足
- $\mathcal S$ 是一个（有限）**状态集合**
- $\mathcal P$ 是一个**状态转移矩阵**

整个过程/系统都可以被良定义
### Example
![[Pasted image 20260805171352.png|474]]
我们令$S_1=\text{Class 1}$
每一条箭头上的数字都是**状态转移概率**。每一个圆都是一个状态，其中Sleep节点（方形）就是最终状态，进入了这个状态整个过程就结束了
# Markov Reward Processes
## 定义
**Markov reward process**是具有values的Markov Chain，被定义为一个四元组$\left<\mathcal S,\mathcal P,\mathcal R,\gamma \right>$，满足
- $\mathcal S$ 是一个有限**状态集合**
- $\mathcal P$ 是一个**状态转移矩阵**
- $\mathcal R$ 是reward function
- $\gamma$ 是**discount factor**，$\gamma\in[0,1]$

**定义**：回报$G_t$是**随机变量**，被定义为：
$$
G_t=\sum_{k\in\mathbb N}\gamma^kR_{t+k+1}
$$
表示**从当前开始所有时间步**上的奖励总和
当然，$k$是可能有上限的，准确来说，$k$的上限是最大的步数

**定义**：MRP的状态价值函数$v(s)$被定义为：
$$
v(s) =\mathbb E[G_t\mid S_t=s]
$$
### Example
![[Pasted image 20260805172248.png|475]]
我们令$\gamma=\frac12$，计算出不同 $\mathcal S$ 的回报$G_1$
![[Pasted image 20260805172937.png]]
把无数个这样的$G_1$进行概率加权就得到了这个状态的状态价值函数

不同的 $\gamma$ 的例子

![[Pasted image 20260805174254.png|516]]
![[Pasted image 20260805174304.png|515]]
![[Pasted image 20260805174316.png|492]]
## Bellman Equation for MRPs
贝尔曼方程把状态价值函数描述为两个部分
$$
\begin{align}
v(s)&=\mathbb E[G_t\mid S_t=s]\\
&=\mathbb E[R_{t+1}+\gamma G_{t+1}\mid S_t=s]\\
&=\mathbb E[R_{t+1}\mid S_t=s]+\mathbb E\left\{\mathbb E[\gamma G_{t+1}\mid S_t=s]\right\}\\
&=\mathbb E[R_{t+1}+\gamma v(S_{t+1})\mid S_t=s]
\end{align}
$$
用树的关系来描述：
![[Pasted image 20260805175134.png|287]]
我们可以得到一个公式：
$$
v(s)=\mathcal R_s+\gamma\sum_{s'\in \mathcal S}\mathcal P_{ss'}v(s')
$$
求和式的意思就是对子节点的值进行概率加权求和（积分）

容易得到贝尔曼方程的矩阵形式
$$
\begin{bmatrix} v(1) \\ \vdots \\ v(n) \end{bmatrix} = \begin{bmatrix} \mathcal{R}_1 \\ \vdots \\ \mathcal{R}_n \end{bmatrix} + \gamma \begin{bmatrix} \mathcal{P}_{11} & \cdots & \mathcal{P}_{1n} \\ \vdots & \ddots & \vdots \\ \mathcal{P}_{n1} & \cdots & \mathcal{P}_{nn} \end{bmatrix} \begin{bmatrix} v(1) \\ \vdots \\ v(n) \end{bmatrix}
$$
### Example
![[Pasted image 20260805175811.png|476]]
# Markov Decision Processes
## 定义
**Markov decision process**是具有decisions的MRP，被定义为一个四元组$\left<\mathcal S,\mathcal A,\mathcal P,\mathcal R,\gamma \right>$，满足
- $\mathcal S$ 是一个有限**状态集合**
- $\mathcal A$ 是一个**有限动作集合**
- $\mathcal P$ 是一个**状态转移矩阵**——$\mathcal P_{ss'}^a=\Pr[S_{t+1}=s'\mid S_t=s,A_t=a]$
- $\mathcal R$ 是reward function——$\mathcal R_s^a=\mathbb E[R_{t+1}\mid S_t=s,A_t=a]$
- $\gamma$ 是discount factor，$\gamma\in[0,1]$
### Example
![[Pasted image 20260805202227.png|446]]
红色的字代表决策——这不涉及概率，这**只是模型做的决定**。而下面节点的三条路径的0.2, 0.4, 0.4是**状态转移概率**
# Policies
## 定义
**定义**：策略$\pi$是一个给定state关于action的**分布**
$$
\pi(a\mid s)=\Pr[A_t=a\mid S_t=s]
$$
- **Policy完全地定义了agent的行为**
- MDP的policies满足$A_t\sim\pi(\cdot\mid S_t),\forall t>0$
- 在给定一个策略时，MDP的**部分**是Markov Process和MRP
$$
\begin{align}
\cal P _ { s, s ^ { \prime } } ^ { \pi } &= \sum \pi ( a | s ) { \cal P } _ { s s ^ { \prime } } ^ { a} \\
\mathcal { R } _ { s } ^ { \pi } &= \sum \pi ( a | s ) \mathcal { R } _ { s } ^ { a }
\end{align}
$$

**定义**：MDP 的 state-value 函数$v_\pi(s)$
$$
v _ { \pi } ( s ) = \mathbb { E } _ { \pi } \left[ G _ { t } \ \middle | \ S _ { t } = s \right]
$$
表示从状态$s$开始，按照策略$\pi$获得的回报的期望

**定义**：MDP 的 action-value 函数$q_\pi(s,a)$
$$
q _ { \pi } ( s, a ) = \mathbb { E } _ { \pi } \left[ G _ { t } \ \middle | \ S _ { t } = s, A _ { t } = a \right]
$$
表示从状态$s$开始，采取动作$a$，然后按照策略$\pi$获得的回报的期望
### Example
![[Pasted image 20260807103635.png|549]]
## Bellman Expectation Equation
$$
v _ { \pi } ( s ) = \mathbb { E } _ { \pi } \left[ R _ { t + 1 } + \gamma v _ { \pi } ( S _ { t + 1 } ) \mid S _ { t } = s \right]
$$
$$
q _ { \pi } ( s, a ) = \mathbb { E } _ { \pi } \left[ R _ { t + 1 } + \gamma q _ { \pi } ( S _ { t + 1 }, A _ { t + 1 } ) \mid S _ { t } = s, A _ { t } = a \right]
$$

由于两种value function都是期望，如果我们穷尽所有action的情况就能总结$v_\pi$
$$
v _ { \pi } ( s ) = \sum _ { a \in \mathcal { A } } \pi ( a | s ) q _ { \pi } ( s, a )
$$

和之前Bellman Equation一样，我们可以利用树方法得到递推的公式。这里实心节点代表**动作**，空心节点代表**状态**：
- 一个动作会去往多种状态
![[Pasted image 20260807104159.png|266]]
注意$q_\pi$和$a_\pi$的定义，当$q_\pi$选择了一个确定的动作会到达一个$v_\pi$，所以：
$$
q _ { \pi } ( s, a ) = \mathcal { R } _ { s } ^ { a } + \gamma \sum _ { s ^ { \prime } \in \mathcal { S } } \mathcal { P } _ { s s ^ { \prime } } ^ { a } v _ { \pi } ( s ^ { \prime } )
$$
- 一个状态可能有多种动作
![[Pasted image 20260807110718.png|265]]
这个状态的价值就是在这个状态采取所有可能动作的价值的期望，所以：
$$
v _ { \pi } ( s ) = \sum _ { a \in \mathcal { A } } \pi ( a | s ) q _ { \pi } ( s, a )
$$
- 一个状态的多种动作到达多种状态：
![[Pasted image 20260807110955.png|308]]
我们得到一个$v_\pi$自己的递推：
$$
v _ { \pi } ( s ) = \sum _ { a \in \mathcal { A } } \pi ( a | s ) \left( \mathcal { R } _ { s } ^ { a } + \gamma \sum _ { s ^ { \prime } \in \mathcal { S } } \mathcal { P } _ { s s ^ { \prime } } ^ { a } v _ { \pi } ( s ^ { \prime } ) \right)
$$
- 一个动作去往多种状态，每个状态都可能采取多种动作：
![[Pasted image 20260807111050.png|313]]
我们得到一个$q_\pi$自己的递推：
$$
q _ { \pi } ( s, a ) = \mathcal { R } _ { s } ^ { a } + \gamma \sum _ { s ^ { \prime } \in \mathcal { S } } \mathcal { P } _ { s s ^ { \prime } } ^ { a } \sum _ { a ^ { \prime } \in \mathcal { A } } \pi ( a ^ { \prime } | s ^ { \prime } ) q _ { \pi } ( s ^ { \prime }, a ^ { \prime } )
$$
### Example
![[Pasted image 20260807111128.png|562]]
# Optimal Value Function
**定义**：
$$
v _ { * } ( s ) = \underset { \pi } { \mathrm { m a x } } ~ v _ { \pi } ( s )
$$
$$
q _ { * } ( s, a ) = \underset { \pi } { \mathrm { m a x } } \; q _ { \pi } ( s, a )
$$
# Optimal Policy
定义一个策略集上的偏序
$$
\forall s,\quad v_{\pi'}(s)\le v_{\pi}(s)\Rightarrow\pi'\preceq\pi
$$

**定理**：对于任意的MDP过程：
- 存在一个最优策略$\pi_*$. 使得$\forall \pi,\quad \pi\preceq\pi_*$
- $v_{\pi_*}(s)=v_*(s)$
- $q_{\pi_*}(s,a)=q_*(s,a)$

## Finding an Optimal Policy
在给定$q_*(s,a)$之后，便可以求得一个确定的Optimal Policy
$$
\pi_*(a|s)= \begin{cases} 1, & \text{if } a=\underset{a\in A}{\arg\max}\ q_*(s,a)\\ 0, & \text{otherwise} \end{cases}
$$
我们每次选定使得最优动作价值函数最大的动作，就是最好的策略。至于怎么“给定”$q_*$就是后话了
### Example
![[Pasted image 20260807113433.png|538]]
这里最好想想$q_*$是怎么算的
# Bellman Optimality Equation for $v_*$
推导几乎和之前的贝尔曼方程一样，但是这里要注意**最优的唯一性**。换句话说，也就是我们要按照上面寻找最优策略的路径来走

- ![[Pasted image 20260807114040.png|292]]
在某个状态，我们要采取能使得动作价值函数最大的动作，我们就能得到最大的状态价值函数（**无关动作**，所以我们要让动作能达到最大）
$$
v _ { * } ( s ) = \underset { a } { \operatorname* { m a x } } \ q _ { * } ( s, a )
$$
- ![[Pasted image 20260807114211.png|288]]
对于一个动作价值函数来说，采取一个动作可能会到不同的后继状态。只要后面的状态都按照最优策略来，就能得到这个动作的最优价值
$$
q _ { * } ( s, a ) = \mathcal { R } _ { s } ^ { a } + \gamma \sum _ { s ^ { \prime } \in \mathcal { S } } \mathcal { P } _ { s s ^ { \prime } } ^ { a } v _ { * } ( s ^ { \prime } )
$$
- ![[Pasted image 20260807114526.png|292]]
我们需要最大化，甚至比上面的更好理解（这里课件里的公式写的有问题，最大化$\mathcal R_s^a$的动作不一定能最大化后面的求和式）
$$
v _ { * } ( s ) = \underset { a } { \operatorname* { m a x } }\big[ \mathcal { R } _ { s } ^ { a } + \gamma \sum _ { s ^ { \prime } \in \mathcal { S } } \mathcal { P } _ { s s ^ { \prime } } ^ { a } v _ { * } ( s ^ { \prime } )\big]
$$
- ![[Pasted image 20260807115635.png|295]]
动作是可以人为选择的，这个和最优策略无关，就像每个状态都有自己的最优状态价值
$$
q _ { * } ( s, a ) = \mathcal { R } _ { s } ^ { a } + \gamma \sum _ { s ^ { \prime } \in \mathcal { S } } \mathcal { P } _ { s s ^ { \prime } } ^ { a } \underset { a ^ { \prime } } { \operatorname* { m a x } } \; q _ { * } ( s ^ { \prime }, a ^ { \prime } )
$$
## Example
![[Pasted image 20260807115807.png|544]]
每个圆圈里的数字就是最优状态价值
# Extensions to MDPs 
[[Reinforcement Learning/RL base/2.Markov Decision Processes/lecture-2-mdp.pdf#page=49|lecture-2-mdp, 页面 49]]
