$$
\underbrace{P(\mathcal H|\text{Data})}_{后验}=\dfrac{\underbrace{P(\text{Data}|\mathcal H)}_{似然}\underbrace{P(\mathcal H)}_{先验}}{P(\text{Data})}
$$
三门问题也可以看做一种噪声信道通讯
# Noisy Channel
**可以在不可靠信道里实现可靠通信，只要使用合适的编码即可**

可以把列看为输入，行看为输出。
**二进制对称信道**：
$$
Q=\begin{bmatrix}
1-f & f\\
f& 1-f
\end{bmatrix}
$$
每一位有 $f$ 的概率翻转

**二进制擦除信道**：
$$
Q=\begin{bmatrix}
1-f & 0\\
f& f\\
0 &1-f
\end{bmatrix}
$$
每一位有 $f$ 的概率损坏，无法得知是0/1

**Z 信道**：
$$
Q=\begin{bmatrix}
1 & f\\
0& 1-f\\
\end{bmatrix}
$$
只有1有 $f$ 的概率变为0

**Example**：给定一个bent coin随机序列，对于二进制对称信道 $f=0.1$，若观察到输出 $y=1$，那么 $x$ 的分布是？即计算$P(x|y=1)$
贝叶斯公式

**互信息量**：传输了多少信息？

以二进制对称信道举例：
$$
I(X;Y)=H(Y)-H(Y|X)=H_2(0.18)-H_2(0.1)=0.21\text{bits}
$$
当然可以用另一个对称的公式，但是由于那个公式和信息的流向相反，所以需要使用贝叶斯公式。计算稍微麻烦一点
## Capacity of a Noisy Channel
**信道容量**：
$$
C(Q)=\operatorname*{max}_{p_x}I(X;Y)
$$
使得取到最大值的 $p_x^*$称为最优输入分布

**香农噪声信道编码定理**：在信息**传输速率**小于 $C$ 的前提下，可以以任意低的错误概率传送数据信息

**Example**：对于这样的信道，$a\to a,b\to b,c\to c,d\to d$，也就是：
$$
Q=I_4
$$
互信息量：
$$
I(X;Y)=H(Y)-H(Y|X)
$$
注意第二项——因为信道是确定的，所以给定 $X$ 以后 $Y$ 是完全不存在概率（确定）的，那么他便没有信息量，也即$H(Y|X)=0$
那么，使得$H(Y)$最大的输入分布是$p_x^*=\{\frac14,\frac14,\frac14,\frac14\}$。得到$C=2\text{bits}$
显然，这里给每个字符编一个2位的码即可实现可靠通信

**Example**：这既是双门问题，又是黑白卡纸问题
$$
Q=\begin{bmatrix}
1 &1/2 & 0\\
0&1/2&1
\end{bmatrix}
$$
假设$P_x=\{1/3,1/3,1/3\}$，求$I(X;Y)$

