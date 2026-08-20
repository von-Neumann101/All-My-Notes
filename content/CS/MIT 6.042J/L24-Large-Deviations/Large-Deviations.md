（上一节课的录像到后面就没有了，以下来源于Notes——并且省略了相当一部分的高中内容）
**定义**：条件期望定义为
$$
\mathbb{E}[X\mid A]  
=  \sum_{\omega\in A} X(\omega){\Pr(\omega\mid A)}=\sum_{\omega\in A} X(\omega)\frac{\Pr(\{\omega\} \cap A)}{\Pr(A)}=
\sum_{\omega\in A} X(\omega)\frac{\Pr(\omega)}{\Pr(A)}
$$
**定理**：如果$A_1,A_2,...,A_n$是样本空间的一个划分，且$P(A_i)>0$，那么
$$
\mathbb{E}[X]
=
\sum_{i=1}^{n} \mathbb{E}[X\mid A_i]\Pr(A_i)
$$
**定理**：如果随机变量$R_1,R_2,...,R_n$相互独立，那么有：
$$
\mathrm{Var}[\sum R_i]=\sum\mathrm{Var}[R_i]
$$

**Markov 定理**：$R$是一个非负随机变量（负数的情况可以通过换元变成非负的），那么
$$
\forall x>0,\ \Pr(R\ge x)\le\frac{\mathbb E[R]}{x}
$$
*推论*：非负随机变量大于$c$倍的其期望的概率上界为$c^{-1}$
*推论*：如果$R\le u$，那么$\forall x<u,\ \Pr(R\le x)\le\frac{u-\mathbb E[R]}{u-x}$
>Proof.
>$$\mathbb{E}[R]=\mathbb{E}[R\mid R\ge x]\Pr(R\ge x)+\mathbb{E}[R\mid R< x]\Pr(R< x)$$
>第一项：$\mathbb E[R\mid R\ge x]\ge x$
>第二项非负
>Q.E.D.

**Chebyshev 定理**：$\forall x>0,R$，都有
$$
\Pr(|R-\mathbb E[R]|\ge x)\le\frac{\mathrm{Var}(R)}{x^2}
$$
*推论*：$\Pr(|R-\mathbb E[R]|\ge c\sigma(R))\le\frac{1}{c^2}$
随机变量偏离均值的程度受到方差的限制
>Proof.
>使用 Markov 定理 证明

**定理**：对于任意随机变量：
$$
\Pr(R-\mathbb E[R]\ge c\sigma(R))\le\frac{1}{c^2+1}\qquad\Pr(R-\mathbb E[R]\le- c\sigma(R))\le\frac{1}{c^2+1}
$$
注意：不能同时取等
**定理**（Chernoff 界）： 令$T_1,T_2,...,T_n$为任意**互相独立**的随机变量，满足$\forall i,0\le T_i\le 1$（可以通过归一化满足），令$T=\sum T_i$，那么对于任意的$c>1$，都有：
$$
\Pr(T\ge c\mathbb E[T])\le e^{-z\mathbb E[T]}\qquad z=c\ln c+1-c
$$
Chernoff 界 给出了一个非常紧的上界，远远优于Markov和Chebyshev给出的界
#Chernoff界 #切比雪夫不等式 #不等式 #独立性
#Markov不等式