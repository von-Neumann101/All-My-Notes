# Introduction
当今的去噪扩散模型学习的是**预测噪声，或者被噪声污染的量**。
根据流形假设，**自然数据应该位于低维流形上**，而噪声污染的数据则不是。根据这一假设，最好直接**预测干净数据**，这能让容量不足(under-capacity)的模型能在高维的空间有效运行
> [!NOTE] "under-capacity"
> 例如一张$16\times16$的RGB图片，展平后$16\times16\times3=768$维，如果模型的hidden dimension有$384$维，那么模型实际上在做：
> $$\mathbb R^{768}\mapsto\mathbb R^{384}\mapsto\mathbb R^{768}$$
> 从直觉上说，768个方向具有的随机度，中间只保留384维的表示。这就叫做"under-capacity"

本文回归了一种朴素的想法——直接预测低维流形的自然图片，而非预测加了多少噪声，以及如何把噪声移动到自然照片
![[Pasted image 20260810210947.png|576]]


模型的行为主要由loss管理，输出到底是什么“关系不大”
![[Pasted image 20260810211225.png|700]]
从数学上讲，当我们给定这三个量中任意一个量时，另外两个量都**是可求的**。但是由于他们所在的空间不同，**使用计算机表示时难度差别极大**。

本文发现了直接生成自然图像的模型可以是under-capacity的，并探究到底是$x-\text{loss}$导致的，还是$x-\text{pred}$导致的
# Prediction Space and Loss Space
## Prediction Space
网络的输出可以定义在任何空间中——$v,\ x,\ \varepsilon$
在数学上，这三个空间是等价的。比如当给定$x$的时候：
$$
\begin{cases} x_\theta = \operatorname{net}_\theta \\ z_t = t x_\theta + (1-t)\epsilon_\theta \\ v_\theta = x_\theta - \epsilon_\theta \end{cases}
$$
这只是一个线性方程组，非常容易求解——对于其他两个空间也是一样的
## Loss Space
以$x-\text{pred}$的$v-\text{loss}$进行组合为例：
$$
\begin{align}
&v_\theta=\frac{x_\theta-z_t}{1-t}\\
&\cal L=\mathbb E||v_\theta(z_t,t)-v||^2=\mathbb E\frac{1}{(1-t)^2}||x_\theta(z_t,t)-x||^2
\end{align}
$$
实际上，这是$x-\text{loss}$的重新加权形式

我们组合三种pred和三种loss得到的9种公式，没有任何两种在数学上等价
## Generator Space
最终我们把$x-\text{pred}$等，变成$v$，然后使用ODE演化：
![[Pasted image 20260810215349.png|654]]
模型是一个5层 ReLU MLP，具有256维的隐藏单元
### Toy Experiment
实际的数据为$\hat x\in\mathbb R^d$，而模型实际看到的是$x=P\hat x\in\mathbb R^D,\quad d<D$（此处$d=2$）
矩阵$P\in\mathbb R^{D\times d}$负责将低维数据$\hat x$映射到一个高维空间。为了保证数据在映射后**不出现本质性变化**，所以要求$P$是正定的——$||x||=||\hat x||$且$||P\hat x_1-P\hat x_2||=||\hat x_1-\hat x_2||$

这么做是为了人为制造一个流形假设：**所有的真实数据 $x$ 可以被 $P$ 的前 $2$ 列张成，即使他实际处在一个 $D$ 维空间中**
# “Just Image Transformers” for Diffusion
由上面的实验可以得出一个结论——一个简单的ViT仅使用$x-\text{pred}$就能做得很好
## JiT
![[Pasted image 20260811170714.png|424]]

这篇论文的重点几乎结束了
# Summary
当观测/patch 维度很高、而网络存在信息瓶颈（hidden width 小于数据维度）时，直接做 x-prediction 比 ϵ-prediction 或 v-prediction 更容易，因为自然数据 x 在流形假设下具有较低的 intrinsic dimension，而 ϵ 和 v 包含高维、off-manifold 的噪声信息。