Model-Free 的价值在于——未知的环境&过于庞大的已知环境。
Model-Free Control 分为：
- On-Policy：不断地学习按**自己策略采样**的数据，并更新**这个策略**
- Off-Policy：不断地学习按**其他策略采样**的数据，并更新**自己的策略**
# On-Policy Monte-Carlo Control
## Generalised Policy Iteration
继续使用MC——上一讲的prediction和greedy policy
但是greedy policy是需要model的：
$$
\pi(s)=\operatorname* { argmax }_{a\in\cal A}(\mathcal R_s^a+\mathcal P_{ss'}^aV(s') )
$$
我们不知道状态转移概率

于是我们使用动作价值函数：（本质上是**把状态转移概率压到Q里面**了，但是我们需要多记录一个变量——Action）
$$
\pi(s)=\operatorname* { argmax }_{a\in\cal A} Q(s,a)
$$
> [!NOTE] 一些提示
> 算法需要保存一张表，记录了若干二元组$(s,a)$和其价值$Q(s,a)$
> 我们之前说我们把状态转移概率压到$Q$里，这是因为模型无法知道潜在的状态转移概率，**只能多次的从这个状态做某个动作，并计算value，最终由大数定理来保证我们的平均值是近似Model的真实期望的**

![[Pasted image 20260817123114.png|386]]
## Exploration
### ε-Greedy Exploration
由于Model-Free，加上算法本身误差，以及一个并不合适的$\pi$，如果使用贪心策略，很可能**无法到达一些很好的未探索区域**，我们使用一种简单的方法来增加好奇心：
一共$m$种动作，有$1-\varepsilon$的概率使用贪心策略，有$\varepsilon$的概率随机移动
$$
\pi'(a\mid s)=
\begin{cases} \frac{\varepsilon}m+1-\varepsilon, & \text{if } a^*=\underset{a\in A}{\arg\max}\ Q_*(s,a)\\ \frac{\varepsilon}m, & \text{otherwise} \end{cases}
$$
### Monte-Carlo Control
![[Pasted image 20260817162617.png|446]]
如果按照之前的那种更新，我们需要Evaluate多次才能使得$V(s)$收敛到$v_\pi(s)$。实际上我们不需要跑完所有的episode再用他来训练，我们可以每跑一个episode就用来训练，这样我们可以获得更好的evaluate

但是，我们的策略不能始终是“具有探索性”的，因为**Bellman Optimal Equation是确定的，不应该存在随机的探索策略**。所以我们的策略必须是GLIE
## GLIE
$\varepsilon$-greedy需要满足Greedy in the limit with infinite exploration：
- 所有的$(s,a)$二元组都要被无限次访问，$\lim_{k\to \infty}N_k(s,a)=\infty$
- 最终的策略是贪心的，$\lim_{k\to\infty}\pi_k(a\mid s)=\mathbf1[a=\operatorname*{argmax}_{a'\in\mathcal A}Q_k(s,a')]$

也就是我们要求Agent能探索到所有的状态，并且最终是满足Bellman Optimal Equation
**Example**：当$\varepsilon_k=\frac1k$时，$\varepsilon$-greedy是GLIE
### GLIE Monte-Carlo Control
对于第 $k$ 次迭代：
1. 采样第$k$个episode：$\{S_1,A_1.R_2,...,S_T\}\sim\pi$
2. 更新：$$
   \begin{aligned}
   &N(S_t,A_t)\longleftarrow N(S_t,A_t)+1\\
   &Q(S_t,A_t)\longleftarrow Q(S_t,A_t)+\frac1{N(S_t,A_t)}(G_t-Q(S_t,A_t))\\
   &\varepsilon\longleftarrow\frac1k\\
   &\pi\longleftarrow\varepsilon\text{-greedy}(Q)
   \end{aligned}$$
这会收敛到最优的Q
> [!NOTE] $Q$的初值
> 对于这个算法来说，$Q$是如何初始化的并不重要，因为当第一次探索到某个$(s,a)$的时候，更新过去的式子等于$G_t$，但是对于TD来说并非如此，因为没有计算均值，而是以一个恒定的常数更新
# On-Policy Temporal-Difference Learning
## SARSA($\lambda$)
![[Pasted image 20260817171138.png|117]]
我们有了一个$(s,a)$二元组，然后我们从环境采样，得到奖励 $R$ 和后继状态 $S'$，接着采样策略$\pi$得到动作$A'$
$$
Q ( S, A ) \gets Q ( S, A ) + \alpha \left( R + \gamma Q ( S ^ { \prime }, A ^ { \prime } ) - Q ( S, A ) \right)
$$
### Sarsa Algorithm for On-Policy Control 
![[Pasted image 20260819095549.png|578]]
第四行的意思是：根据当前的$Q$，构造一个选择动作的策略$\pi$（比如ε-Greedy）
### Convergence of SARSA
SARSA收敛到最优动作价值函数$Q ( s, a ) \to q _ { * } ( s, a )$，需要满足以下条件：
- 策略 $\pi _ { t } ( a | s )$ 是GLIE的
- 步长序列 $\alpha _ { t }$ 是Robbins-Monro的，即：$$
\begin{aligned}
\sum \alpha _ { t } &= \infty \\
\sum \alpha _ { t } ^ { 2 } &< \infty
\end{aligned}
$$
### Windy Gridworld Example
![[Pasted image 20260819102539.png|482]]
从S出发去G，只能上下左右移动。横轴表示进入该列时，纵坐标增加的单位长度

![[Pasted image 20260819102606.png|505]]
### n-step SARSA
和上节课一样，我们往后取真实的$n$步
![[Pasted image 20260819102843.png|539]]
### Forward View SARSA(λ)
和之前的一样，我们对所有step的SARSA加权：
![[Pasted image 20260819103850.png|672]]
### Backward View SARSA(λ)
和之前的一样，不过这里的资格迹是按照二元组$(s,a)$累加的
![[Pasted image 20260819103958.png|617]]
### SARSA(λ) Algorithm
![[Pasted image 20260819104720.png|591]]
### SARSA(λ) Gridworld Example 
![[Pasted image 20260819105145.png|667]]
把所有的value都初始化为0，除了终点为1

一开始模型会随机游走，直到遇到终点并获得1的奖励（对应图2），由于使用的是SARSA(λ)，轨迹经过的所有$(s,a)$都会被更新（如果是1-step SARSA(0)，我们必须撞到有更新的点，才能更新一个新的点）
# Off-Policy Learning
按照behavior policy $\mu(a\mid s)$采样，但是通过**评估** target policy $\pi(a\mid s)$以计算$v_\pi(s)$和$q_\pi(s,a)$
定义的说法有点绕，**Off-Policy实际上只是人为提供了episode（数据），然后计算目标的策略的$v_\pi,q_\pi$**
## Importance Sampling
变换期望：
$$
\begin{aligned}
\mathbb { E } _ { X \sim P } [ f ( X ) ] &= \sum P ( X ) f ( X ) \\
&= \sum Q ( X ) \frac { P ( X ) } { Q ( X ) } f ( X ) \\
&= \mathbb { E } _ { X \sim Q } \left[ \frac { P ( X ) } { Q ( X ) } f ( X ) \right]
\end{aligned}
$$
### Importance Sampling for Off-Policy MC
使用从$\mu$采样得到的数据的Return $G_t$来评估$\pi$（我们用$\mu$中$G_t$的缩放来近似$\pi$的$G_t$）
$$
G _ { t } ^ { \pi / \mu } = \frac { \pi ( A _ { t } | S _ { t } ) } { \mu ( A _ { t } | S _ { t } ) } \frac { \pi ( A _ { t + 1 } | S _ { t + 1 } ) } { \mu ( A _ { t + 1 } | S _ { t + 1 } ) } \dots \frac { \pi ( A _ { T } | S _ { T } ) } { \mu ( A _ { T } | S _ { T } ) } G _ { t }
$$
自然，我们也使用近似的回报来更新
$$
V ( S _ { t } ) \gets V ( S _ { t } ) + \alpha \left( G _ { t } ^ { \pi / \mu } - V ( S _ { t } ) \right)
$$
由于$\dfrac\pi\mu$非常大，所以结果的方差极大
### Importance Sampling for Off-Policy TD
由于大量的权重乘在一起会非常大，我们就考虑只对一步进行近似，也就是TD：
$$
V ( S _ { t } ) \gets V ( S _ { t } ) + 
\alpha \left( \frac { \pi ( A _ { t } | S _ { t } ) } { \mu ( A _ { t } | S _ { t } ) } \left( R _ { t + 1 } + \gamma V ( S _ { t + 1 } ) \right) - V ( S _ { t } ) \right)
$$
## Q-Learning
这是不用Importance Sampling的Off-Policy Learning的方法：
1. 从behavior policy里采样：$A_{t+1}\sim\mu(\cdot\mid S_{t+1})$，作为下一步动作
2. 从target policy里才有：$A'\sim\pi(\cdot\mid S_{t+1})$，是本来应该做的动作
3. 更新：$$Q ( S _ { t }, A _ { t } ) \gets Q ( S _ { t }, A _ { t } ) + \alpha\left( R _ { t + 1 } + \gamma Q ( S _ { t + 1 }, A ^ { \prime } ) - Q ( S_ { t }, A _ { t } ) \right)$$
### Off-Policy Control with Q-Learning
注意Bellman最优方程：
$$
q _ { * } ( s, a ) = \mathbb { E } \left[ R _ { t + 1 } + \gamma \operatorname* { m a x } _ { a ^ { \prime } } q _ { * } ( S _ { t + 1 }, a ^ { \prime } ) \mid S _ { t } = s, A _ { t } = a \right]
$$
由于是Model-Free，我们将期望换为Sampling。同时，我们使用Greedy target policy：
$$
\begin{aligned}
&R _ { t + 1 } + \gamma Q ( S _ { t + 1 }, A ^ { \prime } )\\
= &R _ { t + 1 } + \gamma Q ( S _ { t + 1 }, \underset { a ^ { \prime } } { \mathrm { a r g m a x } } ~ Q ( S _ { t + 1 }, a ^ { \prime } ) ) \\
= &R _ { t + 1 } + \gamma\operatorname* { m a x } _ { a ^ { \prime } }  Q ( S _ { t + 1 }, a ^ { \prime } )
\end{aligned}
$$
由此可以看出这是符合Bellman Equation的

伪代码：
![[Pasted image 20260819181408.png|605]]
# Summary
![[Pasted image 20260819181511.png|689]]

