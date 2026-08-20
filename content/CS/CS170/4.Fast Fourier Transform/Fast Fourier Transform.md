# 快速傅里叶变换
用于**计算离散傅里叶变换**的快速**算法**（快速计算多项式乘积）
目标：有两个多项式$A(x)=\sum_{i=0}^{n-1}a_ix^i,\ B(x)=\sum_{i=0}^{n-1}b_ix^i$，给定其系数，分别为$\mathcal A,\ \mathcal B$，求出多项式$C(x)=(A\cdot B)(x)=c_0+c_1x+...+c_Nx^{N-1},N=2n-1$的系数$c_k$，柯西乘积得到$c_k=\sum_{i=0}^ka_ib_{k-i}$
为保持记法简洁，我们把$A(x),B(x)$扩为$N$项多项式（扩展的项的系数为0）
## FFT & Integer Multiplication
给定$n$位整数$a,b$
$$
\begin{align}
a=\sum_{i=0}^{n-1}a_i10^i=A(10)\\
b=\sum_{i=0}^{n-1}b_i10^i=B(10)\\
a_i,b_i\in[0,9]\cap \mathbb Z_+
\end{align}
$$
所以整数的乘法只是多项式乘法的一个特例，但是**值得注意的是**$a\times b$的结果并不是$A(10)\times B(10)$的数码，这是由进位导致的（不过$c_k\le 81n$）
## Algorithm for poly Multiplication
**Alg 1**：直接算柯西乘积
**分析**：规定加法为$O(1)$，乘法的总步数$1+2+...+n$，所以算法总步数为$O(n^2)$

**Alg 2**：Karatsuba Algorithm
$$
A(x)=a_0+a_1x+...+a_{N/2}x^{N/2}+...+a_{N-1}x^{N-1}=A_l(x)+x^{N/2}A_h
(x)
$$
对$B(x)$也是同理，后面过程和卡拉楚巴算法一模一样了
**分析**：一共有$n$位，所以时间复杂度为$O(N^{\log_23})$

**Alg 3**：
$$
\begin{align}
&\text 1.\hat a \longleftarrow \text{FFT}(a)\\
&\text 2.\hat b\longleftarrow \text{FFT}(b)\\
&\text 3.\text{for i=0 to N-1: }\hat c\longleftarrow \hat a\hat b\\
&\text 4.c\longleftarrow F^{-1}\hat c\\
&\text 5.\text{return }c
\end{align}
$$
**补充**：
**DFT**（离散傅里叶变换）：**DFT**是一个范德蒙**矩阵**$F$，满足
- $x_i=\omega^i,\quad w是n次单位根$
- $F_{ij}=\omega^{ij}$

**复数**：
- 如果$z\in\mathbb C$，那么$z$可以表示为$z=x+\sqrt{-1}\cdot y=r\exp(\sqrt{-1}\cdot\theta)$

**FFT**：
计算$A(x_0),A(x_1),...,A(x_{N-1})$
重写多项式为：
$$
\begin{align}
A(x)&=a_0+a_2x^2+a_4(x^2)^2+...+a_{N-2}(x^{\frac{N-2}{2}})^2+x(a_1+a_3x^2+...+a_{N-1}(x^{\frac{N-2}2})^2)\\
&=A_{\text{even}}(x^2)+xA_{\text{odd}}(x^2)
\end{align}
$$
如果我们任意取点的话，我们仍然需要计算$N$个点，进而造成$O(N^2)$的复杂度。
正是**由于DFT是在复平面的单位圆上均匀取点**的，$N$次单位根平方后的**取值集合是原来的子集，且其大小恰好为原来一半**。也就是说，我们把一个$A(x)$的计算量拆为两个减半计算量的子计算：
$$
T(n)=2T(n/2)+O(n)\Longrightarrow T(n)=O(n\log n)
$$

**分析**：$\deg(C)<N$表明了如果已知$C(x_0),C(x_1),...,C(x_{N-1})$，就可以唯一确定一个$C(x)$. 注意到$C(x_j)=A(x_j)\times B(x_j)$. 但如果**随机选点**求出$C(x)$上的$n$个点，时间复杂度仍是$O(n^2)$。我们考虑DFT
FFT的作用是以$O(n\log n)$的时间复杂计算$\text{FFT}(x)=Fx$
这里$c\longleftarrow F^{-1}\hat c$是逆FFT，也可以用$O(n\log n)$计算出来——$F^{-1}=\frac1N\bar F(逐项共轭)$

> [!NOTE] 为什么用单位根而非一对相反数
> 我们可以这么选点$a,b,-a,-b$，这样经过平方以后可以得到$a^2,b^2,a^2,b^2$，可以使得问题减半。
> 那么为什么还要用单位根呢？因为我们再往后看一步，当我们对$a^2,b^2$再平方的时候，取值的集合并没有减半，也就是说下一步就不满足分治的表达式了
> 这只有单位根才能满足这个条件——每次平方取值集合都能减半
# 记号说明
多项式$P(x)=\sum_{i=0}^{n-1}p_ix^i$**的傅里叶变换为**$P_1,P_2,...,P_n$，也可以记为$(p_0,p_1,...,p_{n-1})$的傅里叶变换为$(P_1,P_2,...,P_n)$

#快速傅里叶变换 #DFT #FFT #多项式乘法
