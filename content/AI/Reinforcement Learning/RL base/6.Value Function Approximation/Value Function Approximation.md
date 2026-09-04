# Introduction
现实世界的**状态空间维度极高，或者是连续的**：
- Backgammon: 1020 states 
- Computer Go: 10170 states 
- Helicopter: continuous state space (infinite)

之前我们计算的$V(s),\ Q(s,a)$都是需要记录每一个$s,\ (s,a)$对应的价值函数值的。应用到上面的状态空间内存会爆炸。解法是：
$$
\begin{align}
\hat v(s,\textbf{w})\approx v_\pi(s)\\
\hat q(s,a,\textbf{w})\approx q_\pi(s,a)
\end{align}
$$
使用神经网络或者支持向量机等（参数为$\textbf{w}$），在所有的状态（即使没有见过）上**拟合真实的value function**
## Types of Value Function Approximation
和Bellman方程比较类似：
![[Pasted image 20260826121812.png|592]]
第一个只是第三个的边缘化
# Incremental Methods
## Gradient Descent
![[Pasted image 20260902094841.png]]
### Value Function Approximation
目标：找到一个好的参数 $\mathbf { w }$ 使得拟合value和实际value的均方误差最小
$$
J ( \mathbf { w } ) = \mathbb { E } _ { \pi } \left[ ( v _ { \pi } ( S ) - \hat { v } ( S, \mathbf { w } ) ) ^ { 2 } \right]
$$
使用梯度下降：
$$
\begin{aligned}
\Delta \mathbf { w } &= - \frac { 1 } { 2 } \alpha \nabla _ { \mathbf { w } } J ( \mathbf { w } ) \\
&= \alpha \mathbb { E } _ { \pi } \left[ ( v _ { \pi } ( S ) - \hat { v } ( S, \mathbf { w } ) ) \nabla _ { \mathbf { w } } \hat { v } ( S, \mathbf { w } ) \right]
\end{aligned}
$$
为了处理这里的期望，我们使用SGD：（期望意义下等价）
$$
\Delta \mathbf { w } = \alpha ( v _ { \pi } ( S ) - \hat { v } ( S, \mathbf { w } ) ) \nabla _ { \mathbf { w } } \hat { v } ( S, \mathbf { w } )
$$
你可能觉得这里的$v_\pi$非常奇怪，因为这并非监督学习。这里只是做一个记号的占位，具体后面会说
## Linear Function Approximation
### Feature Vectors
feature vector：
$$
\mathbf{x}(S)= \begin{pmatrix} x_1(S)\\ \vdots\\ x_n(S) \end{pmatrix}
$$
### Linear Value Function Approximation
最简单的可微分值近似方法是线性近似：（深度学习里很基础的东西，这里不过多说明）
$$
\begin{align}
\hat { v } ( S, \mathbf { w } ) = \mathbf { x } ( S ) ^ { \top } \mathbf { w } = \sum _ { j = 1 } ^ { n } \mathbf { x } _ { j } ( S ) \mathbf { w } _ { j }\\
J ( \mathbf { w } ) = \mathbb { E } _ { \pi } \left[ ( v _ { \pi } ( S ) - \mathbf { x } ( S ) ^ { \top } \mathbf { w } ) ^ { 2 } \right]\\
\Delta \mathbf { w } = \alpha ( v _ { \pi } ( S ) - \hat { v } ( S, \mathbf { w } ) ) \mathbf { x } ( S )
\end{align}
$$
### Table Lookup Features
之前的表格取value法是线性近似的的一个特例：
$$
\mathbf{x}^{\text{table}}(S)= \begin{pmatrix} \mathbf{1}(S=s_1)\\ \vdots\\ \mathbf{1}(S=s_n) \end{pmatrix}
$$
取值可以看做点积（因为table向量只有一个分量为1，其余都为0）
$$
\hat{v}(S,\mathbf{w}) = \begin{pmatrix} \mathbf{1}(S=s_1)\\ \vdots\\ \mathbf{1}(S=s_n) \end{pmatrix} \cdot \begin{pmatrix} w_1\\ \vdots\\ w_n \end{pmatrix}
$$
## Incremental Prediction Algorithms
RL里只有reward，没有监督信号。也就是说，在实际的运行中，我们只能通过采样（Agent观察到的数据/世界）来获得信息（准确来说是$v_\pi$的估计）：
- MC：$\Delta \mathbf { w } = \alpha ( G _ { t } - \hat { v } ( S _ { t },\mathbf{ w } ) ) \nabla _ { \mathbf { w } } \hat { v } ( S _ { t }, \mathbf { w} )$——使用$G_t$作为$v_\pi$的无偏估计
- TD(0)：$\Delta \mathbf { w } = \alpha ( R _ { t + 1 } + \gamma \hat { v } ( S _ { t + 1 }, \mathbf { w } )- \hat { v } ( S _ { t }, \mathbf { w } ) ) \nabla _ { \mathbf { w } } \hat { v } ( S _ { t }, \mathbf { w} )$
- TD(λ)：$\Delta \mathbf { w } = \alpha ( G _ { t } ^ { \lambda } - \hat { v } ( S_ { t }, \mathbf { w } ) ) \nabla _ { \mathbf { w } } \hat { v } ( S _ { t },\mathbf { w } )$
### Monte-Carlo with Value Function Approximation
这里回顾一下MC的知识：我们从$S_1$开始，**一直走到Terminal**，然后获得一个$G_t$，……
$$
\langle S _ { 1 }, G _ { 1 } \rangle, \langle S _ { 2 }, G _ { 2 } \rangle,..., \langle S _ { T }, G _ { T } \rangle
$$
获得了$\langle S,G\rangle$序列，就可以用来训练模型了：（以Linear举例）
$$
\begin{aligned}
\Delta \mathbf { w } &= \alpha ( G _ { t } - \hat { v } ( S _ { t }, \mathbf { w } ) ) \nabla _ { \mathbf { w } } \hat { v } ( S _ { t }, \mathbf { w } ) \\
&= \alpha ( G _ { t } - \hat { v } ( S _ { t }, \mathbf { w } ) ) \mathbf { x } ( S _ { t } )
\end{aligned}
$$
### TD Learning with Value Function Approximation
同上，构建训练数据：
$$
\langle S _ { 1 }, R _ { 2 } + \gamma \hat { v } ( S _ { 2 }, \mathbf { w } ) \rangle, \langle S _ { 2 }, R _ { 3 } + \gamma \hat { v } ( S _ { 3 }, \mathbf { w } ) \rangle,..., \langle S _ { T - 1 }, R _ { T } \rangle
$$
训练：（以Linear举例）
$$
\Delta \mathbf { w } = \alpha ( R + \gamma \hat { v } ( S ^ { \prime }, \mathbf { w } ) - \hat { v } ( S, \mathbf { w } ) ) \nabla _ { \mathbf { w } } \hat { v } ( S, \mathbf { w } ) \, = \alpha \delta \mathbf { x } ( S )
$$
注意，虽然TD(0)是有偏估计，但是其**最终收敛到接近全局最优解**
### TD(λ) with Value Function Approximation
构建训练数据略，依旧训练：
Forward视角：
$$
\begin{aligned}
\Delta \mathbf { w } &= \alpha ( G _ { t } ^ { \lambda } - \hat { v } ( S _ { t }, \mathbf { w } ) ) \nabla _ { \mathbf { w } } \hat { v } ( S _ { t }, \mathbf { w } ) \\
&= \alpha ( G _ { t } ^ { \lambda } - \hat { v } ( S _ { t }, \mathbf { w } ) ) \mathbf { x } ( S _ { t } )
\end{aligned}
$$
Backward视角：
$$
\begin{aligned}
\delta _ { t } &= R _ { t + 1 } + \gamma \hat { v } ( S _ { t + 1 }, \mathbf { w } ) - \hat { v } ( S _ { t }, \mathbf { w } ) \\
E _ { t } &= \gamma \lambda E _ { t - 1 } + \mathbf { x } ( S _ { t } ) \\
\Delta { \bf w } &= \alpha \delta _ { t } E _ { t }
\end{aligned}
$$
### 值得注意的一点
以TD(0)代表整个TD家族：进行Function Approximation的时候，MC和TD都把$v_\pi$换成了自己的target
注意TD(0)，我们把target换成了当前对未来的估计，损失函数可以写为：
$$
L ( w ) = \frac { 1 } { 2 } \left( R_{t+1}+\gamma \hat v(S',w)  - \hat { v } ( S, w ) \right) ^ { 2 }
$$
然而在公式中，我们写的却是：
$$
\Delta \mathbf { w } = \alpha ( R + \gamma \hat { v } ( S ^ { \prime }, \mathbf { w } ) - \hat { v } ( S, \mathbf { w } ) ) \nabla _ { \mathbf { w } } \hat { v } ( S, \mathbf { w } ) 
$$
这并不符合求导法则，因为$\hat v(S',\mathbf w)$依赖$\mathbf w$，但是我们却只对$\hat v(S,\mathbf w)$求梯度——这叫做semi-gradient，我们故意不把$\hat { v } ( S ^ { \prime }, \mathbf { w } )$加入梯度

原因如下：
我们可以把这个看做**监督学习**。在监督学习中，一般有一个Label，而学习的目标就是**让模型的输出更接近Label**，一般是最小化$y-\hat y_w$的均方误差。使用梯度下降更新参数，会让$\hat y_w$更加接近$y$。**但是，Label不会更接近$\hat y_w$（参数初始情况下为高斯噪声）**，这是很简单的道理。
但是到TD这里（MC没有这个问题，因为$G_t$显然是观察值）由于**所谓的Label是由模型自己算出来的**，从数学角度来说，我们需要让梯度包含这一部分。但是实际上，TD的Label本身不应该参与梯度（他是一个Fix Point）
从意义的角度来理解，如果让Label参与梯度，那么$\hat v(S',w)$会被拉向一个错误的$\hat v(S,w)$
## Incremental Control Algorithms
![[Pasted image 20260903121340.png|481]]
每更新一次神经网络，就用贪心策略行动，然后估计一个Q。循环往复……

和Prediction一样。不过既然是Control，我们就需要包含Action，所以我们使用的是$(S,a)$二元组
$$\mathbf{x}(S,A) = \begin{pmatrix} x_1(S,A)\\ \vdots\\ x_n(S,A) \end{pmatrix}$$

![[Pasted image 20260903162208.png|629]]
## Example: Montain Car
使用Linear Sarsa：
![[Pasted image 20260903162709.png|686]]
这里的状态空间是二维的
### Study of λ: Should We Bootstrap? 
![[Pasted image 20260903163728.png|674]]
λ决定了自举的程度，越大自举的程度越低（极限是MC）
## Convergence
### Baird’s Counterexample
这里使用SARSA等TD方法，会出现问题：
![[Pasted image 20260903164251.png|626]]
![[Pasted image 20260903164312.png|581]]
所以TD不一定收敛，这取决于我们**Bootstrap的程度**
### Convergence of Prediction Algorithms
目前只考虑Prediction 算法的收敛
$$
\begin{array}{c|c|c|c|c} \text{On/Off-Policy} & \text{Algorithm} & \text{Table Lookup} & \text{Linear} & \text{Non-Linear} \\ \hline {\text{On-Policy}} & \text{MC} & \checkmark & \checkmark & \checkmark \\ & \text{TD}(0) & \checkmark & \checkmark & \times \\ & \text{TD}(\lambda)& \checkmark & \checkmark & \times \\ \hline {\text{Off-Policy}} & \text{MC} & \checkmark & \checkmark & \checkmark \\ & \text{TD}(0) & \checkmark & \times & \times \\ & \text{TD}(\lambda)& \checkmark & \times & \times \\ \hline \end{array}
$$
### Convergence of Control Algorithms
$$
\begin{array}{c|c|c|c} \text{Algorithm} & \text{Table Lookup} & \text{Linear} & \text{Non-Linear} \\ \hline \text{Monte-Carlo Control} & \checkmark & (\checkmark) & \times \\ \text{Sarsa} & \checkmark & (\checkmark) & \times \\ \text{Q-learning} & \checkmark & \times & \times \\ \textcolor{red}{\text{Gradient Q-learning}} & \checkmark & \checkmark & \times \\ \hline \end{array}
$$
$(\checkmark)$表示在最优值周围震荡，而无法收敛到最优值

这一块辩证的看，毕竟这是老教材了。目前有了新的方法