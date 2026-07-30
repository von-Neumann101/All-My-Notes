# 理论
哑指标(dummy)：出现两次的指标
自由指标(free)：出现一次的指标
例如这个求和式：
$$
\begin{aligned} { A _ { i j } x _ { i } y _ { j } } & { { } = A _ { 1 1 } x _ { 1 } y _ { 1 } + A _ { 1 2 } x _ { 1 } y _ { 2 } + A _ { 1 3 } x _ { 1 } y _ { 3 } } \\ { } & { { } + A _ { 2 1 } x _ { 2 } y _ { 1 } + A _ { 2 2 } x _ { 2 } y _ { 2 } + A _ { 2 3 } x _ { 2 } y _ { 3 } } \\ { } & { { } + A _ { 3 1 } x _ { 3 } y _ { 1 } + A _ { 3 2 } x _ { 3 } y _ { 2 } + A _ { 3 3 } x _ { 3 } y _ { 3 } } \end{aligned}
$$
$i,j$都是哑指标

**Kronecker Delta符号**
$$
\delta _ { i j } = \left\{ \begin{array} { l l } { 1 } & { \mathrm { i f ~ } i = j } \\ { 0 } & { \mathrm { i f ~ } i \neq j } \\ \end{array} \right.
$$
注意一个性质：
$$
\partial _ { i } x _ { j } = \delta _ { i j }
$$
# Pytorch

$$
y _ { b k } = \sum _ { i, j } W _ { i j k } x _ { b i } x _ { b j }
$$
b虽然出现了两次，但是我们考虑到b的实际意义为batch size，我们确定其为自由指标
```python
torch.einsum("ijk,bi,bj->bk", W, x, x)
```
第一个参数为下标参数：原封不动填入数学式子的下标即可，注意`->bk`代表最后会保留b和k（自由指标）
后面传入的参数和第一个参数的下标一一对应
