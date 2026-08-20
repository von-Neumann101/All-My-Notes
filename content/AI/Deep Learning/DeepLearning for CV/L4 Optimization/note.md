## Optimization
1. 随机搜索（bad）
2. 梯度下降：
1.数值梯度
进行微小扰动以后计算梯度（对任意的Loss function有效）
![[Pasted image 20260313081505.png|520]]
但是这会非常慢（对于大型矩阵），一般只用于检查`torch.autograd.gradcheck()`
2.解析梯度
## 梯度下降
```py
w = initialize_weights()
for t in range(iters):
	dw = compute_grad(loss_fn, data, w)
	w -= learning_rate * dw
```
1. 权重的初始化方法：随机值的具体分布非常重要
2. iters：简单地，固定一个次数
3. 学习率：在梯度放下迈出的步长
### Batch Gradient Descent
$$\nabla_W L(W)=\frac{1}{N}\sum_{i=1}^{N}\nabla_W L_i(x_i,y_i,W)+\lambda\,\nabla_W R(W)$$
意味着需要对全部的训练集样本求和，以求得几百万布中的一小步来下降
### Stochastic Gradient Descent
我们只取一部分进行梯度下降
```py
w = initialize_weights()
for t in range(iters):
	minibatch = sample_date(data, batch_size)
	dw = compute_grad(loss_fn, minibatch, w)
	w -= learning_rate * dw
```
对于其他的算法来说，取样方法是一个很重要的超参数，但是对于图像分类，事实证明，影响不大
$$L(W)=\mathbb{E}_{(x,y)\sim p_{\mathrm{data}}}\!\left[L(x,y,W)\right]+\lambda R(W)\approx \frac{1}{N}\sum_{i=1}^{N}L(x_i,y_i,W)+\lambda R(W)$$
#### Problem
1. SGD的Loss Function有着较大的条件数，即对应黑塞矩阵数值不稳定
$$\frac{1}{\kappa(A)}\frac{\|\delta b\|}{\|b\|}\le\frac{\|\delta x\|}{\|x\|}\le\kappa(A)\frac{\|\delta b\|}{\|b\|}$$ 
假设我们在这种地方：某个方向很陡，某个方向很平
![[Pasted image 20260313091230.png|567]]
学习率过大会来回震荡，学习率过小会收敛极慢
2. SGD容易陷入局部极小值或鞍部
![[Pasted image 20260313091556.png|529]]
3. 虽然一开始下降快，但是越接近最值点，会在周边徘徊（noise占比更大了）
### 带惯性SGD
$$\begin{align}
v_{t+1} &= \rho v_t - \nabla f(x_t),\\
x_{t+1} &= x_t + \alpha v_{t+1}.
\end{align}$$
下降的梯度包含了原始梯度和过去的“新梯度$v$”，有了这种惯性，可以把随机性固定
不是像人一步步走，而是像**小球滚下山**，不会在局部极值以及鞍部停住
```py
v = 0
for t in range(iters):
	dw = compute_grad(w)
	v = rho * v - learning_rate * dw
	w += v
```
![[Pasted image 20260313092453.png]]

#### Nesterov Momentum
$$\begin{align}
v_{t+1} &= \rho v_t - \alpha \nabla f\!\left(x_t + \rho v_t\right),\\
x_{t+1} &= x_t + v_{t+1}.
\end{align}$$
按照$v$继续走，然后想象新位置的Gradient，再用想象的Gradient和$v$相加，得到真实步![[Pasted image 20260313093112.png|199]]
```py
v = 0
for t in range(iters):
	dw = compute_grad(w)
	v = rho * v - learning_rate * dw
	w += v
```
等价的
### AdaGrad
自适应梯度下降
$$
\begin{align}

g_t &= \nabla f(w_t),\\

s_t &= s_{t-1} + g_t^2,\qquad s_0=0,\\

w_{t+1} &= w_t - \eta\,\frac{g_t}{\sqrt{s_t}+\varepsilon}

\end{align}$$
```py
grad_squared = 0
for t in range(iters):
	dw = compute_grad(w)
	grad_squared += dw ** 2
	w -= learning_rate *dw / (grad_squared.sqrt() + 1e-7)
```
`grad_squared`跟踪历史梯度的平方和
类似于负反馈调节，在快的时候抑制梯度，在慢的时候增强梯度
但是如果迭代时间过长，最后会等价导致学习率过小的效果
### RMSProp(Advanced Ada)
$$\begin{align}
g_t &= \nabla f(w_t),\\
s_t
&= \beta\,s_{t-1}
+ (1-\beta)\,g_t^2,\\
w_{t+1}
&= w_t-\eta\,\frac{g_t}{\sqrt{s_t}+\varepsilon}
\end{align}$$
```py
grad_squared = 0
for t in range(iters):
	dw = compute_grad(w)
	grad_squared = decay_rate * grad_squared + (1 - decay_rate) * dw * dw
	w -= learning_rate *dw / (grad_squared.sqrt() + 1e-7)
```
RMSProp相当于增加了一个选择，可以继续加也可以不变，会改变一些Ada的缺点
![[Pasted image 20260313112232.png|578]]
### Adam(almost): RMSProp + Momentum
$$\begin{align}
g_t &= \nabla f(w_t),\\
m_t &= \beta m_{t-1} + (1-\beta) g_t,\\
v_t &= \beta v_{t-1} + (1-\beta) g_t^2,\\
w_{t+1} &= w_t - \eta\,\frac{m_t}{\sqrt{v_t}+\varepsilon}
\end{align}$$
```py
moment1 = 0
moment2 = 0
for t in range(iters):
	dw = compute_grad(w)
	moment1 = beta * moment1 + (1 - beta) * dw
	moment2 = beta * moment2 + (1 - beta) * dw * dw
	w -= learning_rate * moment1 / (moment2.sqrt() + 1e-7)
```
$m_t$->惯性，$v_t$->负反馈
如果我们初始化$\beta=0.999$这会导致$v_1$极小（，进而导致大的负梯度
我们进而引入**Bias correction**：（仅仅为了解决一开始极小的问题）
$$\begin{align}
g_t &= \nabla f(w_t),\\
m_t &= \beta_1 m_{t-1} + (1-\beta_1) g_t,\\
v_t &= \beta_2 v_{t-1} + (1-\beta_2) g_t^2,\\
\hat m_t &= \frac{m_t}{1-\beta_1^{\,t}},\\
\hat v_t &= \frac{v_t}{1-\beta_2^{\,t}},\\
w_{t+1} &= w_t-\eta\,\frac{\hat m_t}{\sqrt{\hat v_t}+\varepsilon}
\end{align}$$
```py
moment1 = 0
moment2 = 0
for t in range(iters):
	dw = compute_grad(w)
	moment1 = beta1 * moment1 + (1 - beta1) * dw
	moment2 = beta2 * moment2 + (1 - beta2) * dw * dw
	unbias_moment1 = moment1 / (1 - beta1 ** t)
	unbias_moment2 = moment2 / (1 - beta2 ** t)
	w -= learning_rate * unbias_moment1 / (unbias_moment2.sqrt() + 1e-7)
```
**Adam是非常好的优化器**
一些有用的初始值：
$\beta_1=0.9 \quad \beta_2=0.999$以及学习率可取$10^{-3},5^{-4},10^{-4}$![[opt1.gif|481]]
![[opt2.gif|481]]
*即使如此，我们不应该认为这是真实训练时的行为，图片所给的为2D，这和高维训练时的行为大不相同（这只是很粗糙的直觉）*

目前介绍的都是一阶优化，实际上我们在做的是在一个高维流形上寻找一个线性超平面近似真实梯度
## 二阶优化
可以使用二阶优化，也即利用黑塞矩阵，直观点说就是步长是梯度和曲率的比值，曲率大的地方步子迈得小，反之亦然
![[Pasted image 20260313121201.png|477]]
![[Pasted image 20260313121220.png|317]]
现在具体来看二阶优化
$$\begin{align}
L(w)\approx{}\;&L(w_0)+(w-w_0)^{\top}\nabla_w L(w_0)+\frac{1}{2}(w-w_0)^{\top}H_wL(w_0)(w-w_0),\\[4pt]
w^{*}={}\;&w_0-H_wL(w_0)^{-1}\nabla_w L(w_0).
\end{align}$$
但是由于黑塞矩阵的空间复杂度为$O(n^2)$，同时我们需要求黑塞矩阵的逆，其时间复杂度是$O(n^3)$，一般只有在低维空间中使用二阶优化器（一般为L-BFGS）
#梯度下降 #优化器 







