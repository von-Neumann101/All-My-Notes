# Stirling's Formula
在 $n \to \infty$ 时有
$$
n! = \sqrt { 2 \pi n } \left( \frac { n } { e } \right) ^ { n } \left( 1 + \frac { 1 } { 1 2 n } + \frac { 1 } { 2 8 8 n ^ { 2 } } + O \left( \frac { 1 } { n ^ { 3 } } \right) \right)
$$
# Asymptotic Notation
$O$给出了一个渐进上界：
如果$\lim_{x\to \infty}|\frac{f(x)}{g(x)}|<\infty$，那么$f(x)=O(g(x))$。定性地说，$f(x)$的增长速度不如$g(x)$
> [!NOTE] 注意
> 在写渐进式的时候注意常数
>$$H_n\sim \ln n + \gamma$$
>那么我们可以把 $\gamma$ 改为任意常数而渐进关系不变
>所以应该写为
>$$H_n - \ln n\sim  \gamma$$

$\Omega$给出了一个渐进下界：
$$f(x)=O(g(x))\Longleftrightarrow f(x)=\Omega(f(x))$$
$\Theta$界给出了一个精确的渐进：
$$f(x)=O(g(x))\land f(x)=\Omega(f(x))\Longleftrightarrow f(x)=\Theta(g(x))$$
此外还有记号$o$和$\omega$
严格小于：
$$
f(x)=o(g(x))\Longrightarrow \lim_{x\to \infty}|\frac{f(x)}{g(x)}|=0
$$
严格大于：
$$
f(x)=\omega(g(x))\Longrightarrow \lim_{x\to \infty}|\frac{f(x)}{g(x)}|=\infty
$$
**注意一个很严重的错误**
设$f(n)=\sum_{i=1}^n i$，那么$f(n)=O(n)$
>Proof.
>对n归纳，不变量$P(n)$：“对于任意一个$n$，$f(n)=O(n)$”
>$P(n)\to P(n+1)$：
>$f(n+1)=f(n)+(n+1)=O(n)+O(n)=O(n)$
>Q.E.D.

这里错误的原因在于，不变量**取定了**一个$n$，这就导致了$f(n)$实际上是$f(n_0)$——一个标量，只是$f(x)$在$x=n$处的取值，而渐进符号要求的是$n\to\infty$——是一个过程
#渐进分析