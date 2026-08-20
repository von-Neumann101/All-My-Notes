Model-Free即Agent无法完全了解环境如何运作——状态转移概率......
# Monte-Carlo Reinforcement Learning
MC 直接从经验中直接学习
## Policy Evaluation
**目标**：从按照$\pi$行动而产生的观察来学习$v_\pi$
$$S_1,A_1,R_2,...,S_k\sim\pi$$

在我们有了一系列的Reward以后，便可以计算$G_t$，进而计算$v_\pi(s)$，不过这里我们使用**经验均值来代替期望**
### First-Visit MC Policy Evaluation
每个回合中，我们只记录第一次到某状态得到的奖励
```text
N[n] <- 0 #每个状态访问的次数
S[n] <- 0 #每个状态的累计回报
V[n] <- 0 #每个状态的价值函数
while k < MAX_ITER do:
	is_terminal <- False
	visited[n] <- False
	while is_terminal do:
		s, G_t, is_terminal = experience();
		if visited[s] = False:
			N[s] <- N[s] + 1
			S[s] <- S[s] + G_t
			V[s] <- S(s) / N[s]
	visited[s] <- False
```
由大数定理，当`N(s)=inf`，那么`V(s)`收敛到$v_\pi(s)$

也就是说，我们每次运行一个episode就会产生一个$G_t$，由于$v(s)=\mathbb E[G_t\mid S_t=s]$连续，所以我们通过求均值来近似一个$v$
## Increment Mean
以下**只是一种数学上的重写**，本质和之前的方法没有区别（或者说是为了后续的公式进行一种等价变形）

对于序列$x_1,x_2,...,x_n,...$的均值可以写成如下的递推形式：
$$
\begin{aligned}
\mu _ { k } &= \frac { 1 } { k } \sum _ { j = 1 \atop { \prime } } ^ { k } x _ { j } \\
&= { \frac { 1 } { k } } \left( x _ { k } + \sum _ { j = 1 } ^ { k - 1 } x _ { j } \right) \\
&= \frac { 1 } { k } \left( x _ { k } + ( k - 1 ) \mu _ { k - 1 } \right) \\
&= \mu _ { k - 1 } + \frac { 1 } { k } \left( x _ { k } - \mu _ { k - 1 } \right)
\end{aligned}
$$
### Incremental Monte-Carlo Updates
加入记忆化，就不需要追踪价值的总和了：
$$
v(S_t)\longleftarrow v(S_t)+\alpha(G_t-v(S_t))
$$
$G_t$是实际的回报，我们通过他和我们的预估的价值函数的差值来更新我们的价值函数
# Temporal-Difference Learning
时序差分算法**不需要完整的episode**
## MC and TD
目标和MC一样，都是在给定策略下预测价值函数

我们先考虑$\text{TD}(0)$：
$$
v(S_t)\longleftarrow v(S_t)+\alpha\underbrace{(R_{t+1}+\gamma v(S_{t+1})-v(S_t))}_{\text{TD error: }\delta_t}
$$
和之前类似，MC中我们使用$G_t-v(S_t)$也就是真实值减去 ***当前*** 估计值来更新。但是在TD(0)中，我们对下一步进行估计，也就是往前一步估计$G_t$

比如在开车中，遇到一个即将发生车祸的场景，但是在最后一秒另一个车避开了：
- MC由于没有碰撞，他并不会受到一个大的负奖励
- TD由于很容易预测到接下来会碰撞，它会受到一个很大的负奖励
### Driving Home Example
![[Pasted image 20260814210409.png|574]]

![[Pasted image 20260814212353.png|567]]
代入$\alpha=1$，有如下公式：
$$
\begin{align}
\text{MC:}&\ v(S_t)\longleftarrow G_t
\\
\text{TD}(0):&\ v(S_t)\longleftarrow R_{t+1}+\gamma v(S_{t+1})
\end{align}
$$
这里我们不从RL的角度来看，而是从MC和TD两种方法的角度来看：
- MC：由于运行完一个episode以后，得到了真实的结果。我们能直接把所有状态的预测时间都变为真实时间
- TD：由于TD不需要运行整个episode，我们只需要往前一步。以`leaving office`的更新举例：我们向前一步，得知了`leaving`的耗时，然后我们预测接下来还有`35`分钟走，所以更新其为`40`（注意，我们是知道每个状态的value的）
## Advantages and Disadvantages of MC vs. TD
TD可以**一步一步学习**，也即不用知道最终的结果。但是MC就必须要知道结果才能学习——所以TD可以用在无终点（连续）环境，而MC只能用在有终点环境

但是TD对初值非常敏感（因为他是自举式的算法）
### Bias/Variance Trade-off
#### Bias
- MC：Return $G_t=R_{t+1}+\gamma R_{t+1}+...+\gamma^{T-1}R_{T}$是$v_\pi(S_t)$的无偏估计（定义）
- TD：Target $R_{t+1}+\gamma v_\pi(S_{t+1})$由贝尔曼方程可得，是无偏估计。但是实际上$v_\pi$并非已知，而是TD自己估计出来的，这就会产生误差
#### Variance
由于TD估计的是$R_{t+1}+\gamma \hat v_\pi(S_{t+1})$，后面的 **“因为随机产生的Reward全部被压缩到一个估计的value中”**，导致方差很小

比如到了$S_{t+1}$以后
$$
G_t=
\left\{\begin{align}
  -100,50\%\\
  100,50\%
\end{align}\right.

$$
那么$v_\pi(S_{t+1})=\mathbb E[G_t]=0$
MC得到的$v_\pi$不是$+100$就是$-100$，每次都会巨幅抖动
true TD由于知道$v_\pi(S_{t+1})=0$，他会直接使用这个，随机的波动直接消失了
## Random Walk Example
使用随机策略走：
![[Pasted image 20260816084304.png]]
TD(0)：（标的数字代表迭代的次数）
![[Pasted image 20260816084224.png|488]]
### MC vs. TD
上述的例子，MC和TD的对比
![[Pasted image 20260816084554.png|490]]
## Batch MC and TD
当有无穷多episode时，MC和TD都收敛到$v_\pi(s)$。但是通常我们只有有限个episode，我们就要多次使用同一个episode
### Example: AB
![[Pasted image 20260816151626.png|592]]
- Monte-Carlo：
  $V(A)=0$，这是由于所有的episode只有一个$A$，而且从他出发得到的value的确为0
  $V(B)=\frac68$，直接运行MC，从B的价值就是求8次的均值，也就是$\frac68$
- Temporal-Difference：
  先看$V(B)$，由于TD(0)的target是$R_{t+1}+\gamma V(S_{t+1})$，而给出的episode中，B的下一步都是终点，所以每次更新$V(B)\longleftarrow V(B)+\alpha(R-V(B))$。最终我们运行无数次的Batch，TD必然收敛，也就是在每个batch运行后，结果应该不变。所以8个样本的TD error的和为0——易得$V(B)=\frac68$
  $V(A)=0+\gamma V(B)=\frac68$
  实际上，TD是在**拟合一个MDP**，就是图右的图
### Certainty Equivalence
**Monte-Carlo**：MC收敛到均方误差最小的解，即：
$$
\operatorname* { min } _ {V}\sum_{k=1}^K\sum_{t=1}^{T_k}(G_t^k-V(s_t^k))^2
$$
比如$V(A)=0$，对于A来说$G_t=0$，这显然是最小化均方误差的结果

**Temporal-Difference**：TD收敛到Markov模型的最大似然，即$\text{MDP }<\cal S,\cal A, \hat { \mathcal { P } },\hat { \mathcal { R } },\gamma>$：
$$
\begin{aligned}
\hat { \mathcal { P } } _ { s, s ^ { \prime } } ^ { a } &= \frac { 1 } { N ( s, a ) } \sum _ { k = 1 } ^ { K } \sum _ { t = 1 } ^ { T _ { k } } \mathbf { 1 } ( s _ { t } ^ { k }, a _ { t } ^ { k }, s _ { t + 1 } ^ { k } = s, a, s ^ { \prime } ) \\
\hat { \mathcal { R } } _ { s } ^ { a } &= \frac { 1 } { N ( s, a ) } \sum _ { k = 1 } ^ { K } \sum _ { t = 1 } ^ { T _ { k } } \mathbf { 1 } ( s _ { t } ^ { k }, a _ { t } ^ { k } = s, a ) r _ { t } ^ { k }
\end{aligned}
$$

因此我们能看出来**TD在Markov环境中更加有效，MC在非Markov环境中更有效**
## Unified View
- MC运行到底
![[Pasted image 20260816163319.png|628]]
- TD(0)往后一步
![[Pasted image 20260816163354.png|622]]
- DP考察所有可能情况
![[Pasted image 20260816163419.png|596]]

**总结**：
![[Pasted image 20260816163514.png|493]]
# $\text{TD}(\lambda)$
## $n$-Step TD
![[Pasted image 20260816163655.png|511]]
比如$n=2$
$$
{ G _ { t } ^ { ( 2 ) } = R _ { t + 1 } + \gamma R _ { t + 2 } + \gamma ^ { 2 } V ( S _ { t + 2 } ) }
$$

定义$n$-step return：
$$
G _ { t } ^ { ( n ) } = R _ { t + 1 } + \gamma R _ { t + 2 } +... + \gamma ^ { n - 1 } R _ { t + n } + \gamma ^ { n } V ( S _ { t + n } )
$$
我们有$n$-step TD：
$$
V ( S _ { t } ) \gets V ( S _ { t } ) + \alpha \left( G _ { t } ^ { ( n ) } - V ( S _ { t } ) \right)
$$
### Large Random Walk Example
![[Pasted image 20260816164630.png|543]]
这里接近MC，会产生大方差，而一开始运行的不多，所以RMS error会很大。
显然过大和过小的$n$都不是最优的，我们如何选择最优呢？
### Averaging $n$-Step Returns 
我们取多个$n$，然后计算回报的均值，比如$\frac12G_{t}^{(2)}+\frac12G_{t}^{(4)}$
但是我们有什么方法可以快速地从所有$n$-step的信息呢？
## Forward View of $\text{TD}(\lambda)$
使用$\lambda$加权所有步长的TD：
$$
G _ { t } ^ { \lambda } = ( 1 - \lambda ) \sum _ { n = 1 } ^ { \infty } \lambda ^ { n - 1 } G _ { t } ^ { ( n ) }
$$
进而使用新的return更新：
$$
V ( S _ { t } ) \gets V ( S _ { t } ) + \alpha \left( G _ { t } ^ { \lambda } - V ( S _ { t } ) \right)
$$
因为使用了对未来的采样来更新，所以他叫做Forward View

![[Pasted image 20260816170602.png|595]]
## Backward View of $\text{TD}(\lambda)$
### Eligibility Trace
一种启发性方法
![[Pasted image 20260816172004.png|588]]
一个状态的资格迹来源于过去的积累，类似于神经一样，多次小刺激等于大刺激，长时间不刺激兴奋逐渐归零
### Backward View TD(λ)
每一个状态维护一个资格迹，把资格迹加入更新：
$$
\begin{align}
&\delta _ { t } = R _ { t + 1 } + \gamma V ( S _ { t + 1 } ) - V ( S _ { t } )
\\
&V ( s ) \leftarrow V ( s ) + \alpha \delta _ { t } E _ { t } ( s )
\end{align}
$$
注意，我们是对每一个状态更新的，而且未来的迹一定为0。所以**按照之前状态的访问次数，把$\delta_t$传播到过去的状态的value**——这也是为什么它叫做Backward View
## Summary
$$
\sum _ { t = 1 } ^ { T } \alpha \delta _ { t } E _ { t } ( s ) = \sum _ { t = 1 } ^ { T } \alpha \left( G _ { t } ^ { \lambda } - V ( S _ { t } ) \right) \mathbf { 1 } ( S _ { t } = s )
$$
这也就告诉我们，所谓的Backward和Forward只不过是解释$\text{TD}(\lambda)$的两种视角，他们本质是一样的：
- **Forward**：一次性看未来，然后计算总的信息
- **Backward**：每次看到一个新的未来，就把信息传回去

![[Pasted image 20260816173513.png|689]]