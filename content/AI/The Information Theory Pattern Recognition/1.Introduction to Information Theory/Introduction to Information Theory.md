# Fundamental Problem
Claude Shanon的信息论希望结局这样的问题——在不可靠信道(channel)实现可靠通信。由于噪音的存在，接收信号和发送信号不完全相同。他希望构建一个接收消息等于发送原始消息的通信方式
# Information Theory
$$
\begin{align}
&s:\text{information}\to\fbox{ENCODER}\to t:\text{coded transmission}\\&\to\fbox{Channel(plus noise $n$)}
\to r:\text{received}\to\fbox{DECODER}\to \hat s
\end{align}
$$
编码器是用于添加 **冗余(redundancy)** 的系统，解码器则是推测$n$和$s$的系统
## Binary Symmetric Channel
输入和输出都是$0,\ 1$，其中输入和输出不同的概率是$f$

**Example**($f=0.1$):
![[Pasted image 20260811211115.png|616]]
## Encoder
1. repitation code $R_3$：

| s   | t   |
| --- | --- |
| 0   | 000 |
| 1   | 111 |
**Example**：
```
s = 01101
t = 000 111 111 000 111
n = 000 100 000 101 000 #翻转位当且仅当n的位位1
r = 000 011 111 101 111
```
`r`是模2下`t`和`n`的加法
2. Parity bits：
$\text{7,4 Hamming Code}$：每次取4个源bits，然后编码为7个传输bits
![[fa196a35cc57afa70a840fcd1e421d5e.png|565]]
这里添加的规则是——要**使得每个大圆内数之和为偶数**
## Decoder
1. Majority vote decoder：看每3位中的众数作为$\hat s$
具体的推导是高中概率题，此处省略。从直觉上说，由于 $f$ 较小，再重复了以后翻转的位为众数的概率很小
2. Parity bits：
![[d89769976ceacb8c2be465b696404587.jpg|541]]
假设`r = 1100101`，明显是第二位改了。我们找到图中圆内的奇偶性——我们 *猜测*“在所有奇环内，偶环外”的数是被翻转的位。
这种方法只对**只有一个位被翻转的**情况有效，如果多余一个，则方法失效
# What's achievable
![[Pasted image 20260814160310.png|584]]
图的横坐标是码率，也就是s和t长度的比值，代表添加冗余的大小，越小说明冗余越大。从直觉上说，如果我们完全不改变长度($t=s$)，那么每一个位的翻转概率就是每一位的错误率。
## Shannon Theorem
从上图看，某种**我们能达到的界限**，是一条过原点的曲线。但是香农证明，不需要使得码率无穷小才能使得错误率无穷小
使得错误率无穷小的码率最小值为信道容量$C$
![[Pasted image 20260814160835.png|556]]

比如翻转概率为$f$的BSC的信道容量为：
$$
C_{\text{BSC}}=1-H_2(f)
$$
其中，$H_2(x)=x\log_2\dfrac1x+(1-x)\log_2\dfrac1{1-x}$
当$f=0.1$的时候，$C\approx0.53$
