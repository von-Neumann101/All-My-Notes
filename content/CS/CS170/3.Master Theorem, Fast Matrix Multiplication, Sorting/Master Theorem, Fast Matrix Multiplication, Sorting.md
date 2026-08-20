# 主定理
**分治**有如下形式：
$$
\begin{align}
&T(x)=\sum_{i=1}^na_iT(b_ix+\varepsilon_i(x))+g(x)\quad \forall x\ge x_0\\
&其中a_i>0,\ 0<b_i<1,\ n\in\mathbb Z,\ |\varepsilon_i(x)|\le O(\frac{x}{\log^2x}),\ \exists c\in\mathbb R,|g'(x)|\le x^c
\end{align}
$$
**Akra–Bazzi** 定理：
$$
找唯一的p\in\mathbb R满足\sum_{i=0}^ka_ib_i^p=1，那么T(x)=\Theta(x^p+x^p\int_1^x\frac{g(u)}{u^{p+1}}du)
$$
**主定理**：特殊地，当$n=1,\ \varepsilon_i(x)=0,\ g(x)=Cn^d$时
$$
\begin{equation}T(n)=
\left\{ \begin{aligned} 
&\Theta(x^d)  & \frac{a}{b^d}<1, \\ 
&\Theta(x^d\log x)&\frac{a}{b^d}=1,\\
&\Theta(n^{\log_ba})   &\frac{a}{b^d}>1.
\end{aligned} \right. 
\end{equation}
$$
使用递归树证明
# Matrix Multiplication
计算矩阵乘法$R=PQ, \text{其中} P,Q,R\in\mathbb R^{n\times n}$，$C$中的每一个元素$r_{ij}=\mathcal P_i\cdot\mathcal Q^j$
$(i,j)$一共$n^2$个，同时对于每一个$(i,j)$，要进行$n$次乘法。所以矩阵乘法的步数为$\Theta(n^3)$
和加法的下界一样，我们读取和输出的步数是$\Theta(n^2)$，我们要尽可能逼近这个下界。

我们考虑**分块矩阵**：
$$
P = \begin{bmatrix}
A & B\\
C & D
\end{bmatrix}
$$
$$
Q = \begin{bmatrix}
E & F\\
G & H
\end{bmatrix}
$$
其中矩阵$A,B,...,H\in \mathbb R^{\frac n2\times \frac n2}$
得到他们的乘积
$$
R=PQ=\begin{bmatrix}
AE+BG & AF+BH\\
CE+DG & CF+DH
\end{bmatrix}
$$
我们把一个矩阵乘法变为八个$\frac n2\times \frac n2$的矩阵乘法，然后我们需要把他们加起来。得到分治表达式
$$
T(n)=8T(n/2)+Cn^2\Longrightarrow T(n)=\Theta(n^3)
$$
然而效率并没有变好

**Strassen Algorithm**：
我们定义一共7个量（分块矩阵的记法和上面一样）
$$
\begin{align*}
p_1&=A(F-H)\\
p_2&=(A+B)H\\
p_3&=(C+D)E\\
&\ldots\\
p_7&=......
\end{align*}
$$
和[[Introduction, Integer Arithmetic#^66b2c2|卡拉楚巴算法]]一样，我们用这7个量表示了上面的4个矩阵乘法的和，于是我们改进了分治
$$
T(n)=7T(n)+Cn^2\Longrightarrow T(n)=\Theta(n^{2.804})
$$
目前最佳为$n^{2.3728596...}$
# Sort
## Merge Sort
[[L30 Merge Sort, Insertion Sort, and Quick Sort#Merge Sort|Merge Sort]]
$$
T(n)=2T(n/2)+Cn\Longrightarrow \Theta(n\log n)
$$
## 已知最快的排序
以$\Theta(n\log\log n)$复杂度可对$n$个元素进行排序。若可使用随机化算法，界可以优化到$\Theta(n\sqrt{\log\log n})$
## Quick Sort
[[L30 Merge Sort, Insertion Sort, and Quick Sort#Quick Sort|Quick Sort（基础）]]
[[L33 Quick Sort|Quick Sort（进阶）]]
pivot最好选择为中位数，如果每次都这样效率最高。我们可以先[[Arithmetic, Asymptotic , Master Theorem, Median Finding#Median of Medians|查找中位数]]，也可以随机选择一个数作为中位数的近似

#快速矩阵乘法 #分治 #排序 #选择 #主定理 #Strassen算法
