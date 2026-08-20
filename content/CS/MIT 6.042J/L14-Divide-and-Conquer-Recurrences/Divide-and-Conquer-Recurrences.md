**分治**有如下形式：
$$
\begin{align}
&T(x)=\sum_{i=1}^na_iT(b_ix+\varepsilon_i(x))+g(x)\quad \forall x\ge x_0\\
&其中a_i>0,\ 0<b_i<1,\ n\in\mathbb Z,\ |\varepsilon_i(x)|\le O(\frac{x}{\log^2x}),\ \exists c\in\mathbb R,|g'(x)|\le x^c
\end{align}
$$
> [!NOTE] 分治/递归
> 分治是把一个大问题拆成若干个规模更小的子问题，分别解决，再合并结果。
> 递归则是描述问题和子结构的关系。

**Akra–Bazzi** 定理(1996)：
$$
找唯一的p\in\mathbb R满足\sum_{i=0}^ka_ib_i^p=1，那么T(x)=\Theta(x^p+x^p\int_1^x\frac{g(u)}{u^{p+1}}du)
$$
Example：
$T(x)=T(\frac{x}{2})+x-1$
$$
\begin{align}
&a_1=2,b_1=\frac{1}{2},n=1\\
&2(\frac{1}{2})^p=1\Rightarrow p =1\\
&T(x)=\Theta(x+x\int_1^x\frac{u-1}{u^2}du)=\Theta(x\ln x)
\end{align}
$$
定理：
$$
如果\exists t\ge 0,g(x)=\Theta(x^t)，且\sum_{i=0}^ka_ib_i^t<1，那么T(x)=\Theta(g(x))
$$
#Akra-Bazzi定理 #分治
