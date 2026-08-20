![[Pasted image 20260805163257.png|302]]
**History**：是observation, actions, rewards的序列
$$H_t=O_1,R_1,A_1,...,A_{t-1},O_t,R_t$$

**State**：用于决定下一步的动作的信息
$$S_t=f(H_t)$$

**Information State** (Markov State)：包含了过去的**有效**信息。一个状态为Markov状态，当且仅当
$$
\Pr[S_{t+1}\mid S_t]=\Pr[S_{t+1}\mid S_1,...,S_t]
$$
显然，$H_t$是Markov的。一般我们定义环境状态$S_t^e$是Markov的

**Policy**：记为$\pi(a\mid s)=\Pr[A_t=a\mid S_t=s]$，表示在状态为$s$的情况下采取动作$a$的概率

**Value Function**：记为$v_\pi(s)$，表示对**未来**奖励的期望

**Model**：一般分为两个
- Transitions：$\mathcal P_{ss'}^a=\Pr[S'=s'\mid S=s,A=a]$ 预测下一个state
- Rewards：$\mathcal R_s^a=\mathbb E[R\mid S=s,A=a]$ 预测接下来的reward

#强化学习 #Markov