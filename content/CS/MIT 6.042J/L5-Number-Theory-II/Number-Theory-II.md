# 模运算
性质：
$$
\gcd(a,b)=1\ \Longleftrightarrow\  sa+tb=1
$$
充分性是因为上节证明的最大公约数性质，必要性是因为任意两自然数最小公约数为1
## 同余
定义1：
$$
x在模n下和y同余\Longleftrightarrow x\equiv y\pmod n\Longleftrightarrow n\mid(x-y)
$$
定义2：
$$
x模n下的乘法逆元为x^{-1}\in\{0,1,...,n-1\},使得xx^{-1}\equiv1\pmod n
$$
比如
$$
2\times3\equiv1\pmod 5
$$
2和3就互为模5下的乘法逆元
注意，模运算下不一定每个数都存在乘法逆元，比如在模$6$运算下，$2$不存在乘法逆元
性质
$$
\gcd(n,k)=1\Rightarrow k在模n下一定有乘法逆元
$$
## Euler's Function
$$
\varphi(n)=\left|\left\{\,k\in\mathbb{Z}\mid 1\le k\le n-1,\ \gcd(k,n)=1\,\right\}\right|.
$$
例如，在1~12之间——1, 5, 7, 11和12互质，所以$\varphi(12)=4$
### Euler's Theorem
$$
\gcd(a,n)=1 \Longrightarrow a^{\varphi(n)}\equiv 1 \pmod n.
$$
当n为素数时，称为费马小定理
引理（模运算消去律）：
$$
\gcd(c,n)=1 \ \land\ ac\equiv bc\pmod n
\Longrightarrow
a\equiv b\pmod n.
$$
引理：
$$
\begin{aligned}
&\text{假设 } \gcd(k,n)=1.\\
&\text{令 } \{k_1,\ldots,k_r\}\subseteq\{1,2,\ldots,n-1\}
\text{ 表示所有与 } n \text{ 互质的整数} (显然r=\varphi(n)).\\
&\text{则 }
\left\{
kk_1\bmod n,\ldots,
kk_r\bmod n
\right\}
=
\{k_1,\ldots,k_r\}.
\end{aligned}
$$
两步证明：1.证明集合里有r个数    2.证明这个集合被包含于$\{k_1,\ldots,k_r\}$
前者易证，我们来看后者的证明
我们只需证明
$$
\gcd(kk_i\bmod n,n)=1
$$
由欧几里得算法可得：
$$
\gcd(kk_i\bmod n,n) = \gcd(kk_i,n)=1
$$
引理得证
接下来证明欧拉定理：
我们证明了
$$
\left\{
kk_1\bmod n,\ldots,
kk_r\bmod n
\right\}
=
\{k_1,\ldots,k_r\}.
$$
则两个集合中元素的乘积相同，进而得到
$$
k_1k_2\ldots k_r\equiv kk_1kk_2\ldots kk_r\mod n
$$
由消去律可得
$$
1\equiv k^r\mod n，其中r=\varphi(n)
$$
# 密码学
事先将秘钥$keys$交换，记加密前的信息为$m$，加密后的消息为$m'$
加密：
$$
m' = \mathrm{E}_{keys}(m)
$$
解密：
$$
m=\mathrm{D}_{keys}(m')
$$
我们希望，在没有$keys$的时候，知道$m'$也无法知道$m$
## Turing Code I
将消息变为**质数**
### Example
对于一个单词，我们用他在字母表的位置作为其对应的数字
```
  v  i  c  t  o  r  y
m=22 09 03 20 15 18 25
```
我们在m后面加一个`13`，使得m变成质数
我们事先交换一个秘钥$k$(secret **prime**)，加密非常简单：
$$
m' = mk\ \ \ (m,\ k为素数)
$$
虽然加密很简单，但事实上：**分解两个大素数乘积是困难的** ^903185

但是如果我们发送第二条消息$n$，则会
$$
m'=mk,\ n'=nk\Rightarrow k=\gcd(m',n')
$$
而最大公约数非常好求

## Turing Code II
除了交换一个秘钥$k$以外，再交换一个**公开素数**$p$，消息表示为$m\in\{0,1,...,p-1\}$
加密：
$$
m'=mk\bmod p
$$
解密：
$$
m=m'k^{-1}\pmod p
$$
### 明文攻击
已知消息明文$m$和密文$m'$，由于$p$是质数，所以$sm+tp=1$，两边同时取$p$的模，得到m在模p下的乘法逆元为s，可以计算出秘钥$k$（同样，可以计算其模p下乘法逆元）
$$
k\equiv ms\pmod p
$$
## RSA
由费马小定理得到
$$
p \text{ 为素数}且a\in\{1,2\ldots,p-1\}
,\ 
a^{p-1}\equiv 1 \pmod p\Longrightarrow aa^{p-2}\equiv1\pmod p
$$
这将有助于我们求解乘法逆元
## 内容
事先，接收方生成公钥（公布）和私钥（自己保留）。任何人可以使用公钥加密一个信息，加密后的消息发送给接收者，他将使用自己的私钥来恢复出明文消息
1. 生成两个不同的质数$p$和$q$（非常高效）
2. 计算[[Number-Theory-II#^903185|乘积]]，$n=pq$
3. 对于公钥：选择一个整数$e$，使得$e$和$(p-1)(q-1)$互质，其为数对$(e,n)$
4. 对于私钥：计算$d$，使得$de\equiv 1\pmod{(p-1)(q-1)}$，其为数对$(d,n)$
加密
$$
m'\equiv m^e\pmod n
$$
解密
$$
m\equiv(m')^d\pmod n
$$
证明：
$$
m\equiv m'^d\pmod n=m^{ed}\pmod n
$$
由私钥生成的方式：
$$
存在一个整数r，使得de=1+r(p-1)(q-1)
$$
如果m不为p和q的倍数，我们可以应用费马引理
因为$n=pq$，我们有：
$$
(m')^d\equiv mm^{r(p-1)(q-1)}\pmod p
$$
对$q$同理
再结合费马小定理，得到
$$
(m')^d\equiv m\pmod p
$$
以及
$$
(m')^d\equiv m\pmod q
$$
由以上两个式子得到：
$$
(m')^d\equiv m\pmod n
$$
因为大质数乘积分解很难，所以$n$可以被公开，又由于$p$和$q$对私人已知，所以容易计算$(p-1)(q-1)$
#数论 #费马小定理 #RSA #加密 #欧拉函数 #素数