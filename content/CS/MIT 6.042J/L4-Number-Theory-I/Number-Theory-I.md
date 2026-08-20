研究整数的学科
# 状态机(state machine)
- **状态（state）**：当前局面的完整描述。
- **初始状态（start state）**：过程开始时的状态。
- **状态转移（transition）**：允许执行的一步操作，以及操作后状态如何变化
# 整除
$$m|a\Rightarrow m整除a$$
## Example
有一个$a\ \mathrm{L}$和$b\ \mathrm{L}$的桶，证明：若$m|a,m|b$，则**任意时刻**两个桶中的水量都能被 $m$ 整除
使用状态机来描述：
- state：$(x,y)$表示第一，第二个桶中的水量
- start state：$(0,0)$——开始时都是空桶
- transition：
1. emptying: $(x,y)\to(0,y)$ 或者 $(x,y)\to(x,0)$
2. filling: $(x,y)\to(a,y)$ 或者 $(x,y)\to(x,b)$
3. pouring:  $(x,y)\to(0,x+y)\quad \mathrm{when}\ x+y\le b$ 或者$(x,y)\to(x+y-b,b)\quad \mathrm{when}\ x+y\ge b$
我们需要证明的就是
$$P(n):m∣x 且 m∣y$$
对于所有从 $(0,0)$ 出发任意的操作步数$n$——无论状态如何一步步变化，这个性质始终不会被破坏（[[Strong-Induction#不变量|不变量]]）
我们使用归纳法来证明，我们对步数进行归纳（以确保任意步数的$P(n)$成立）
# 最大公约数
$\gcd(a,b)$表示$a$和$b$的最大公约数。如果$\gcd(a,b)=1$，则$a$与$b$互质
## 定理
1. **对于任意的$a$和$b$的线性组合$L=sa+tb\in[0,b]$，证明：都能用$a\ \mathrm{L}$和$b\ \mathrm{L}$的桶reach（模b下a和b的加减法）**
2. **$\gcd(a,b)$是$a$和$b$的最小正线性组合**

算法：
每轮往a罐子中加水，只要a罐子中有水，就把a罐子一直往b罐子中倒，b罐子满了就清空。一共操作$s'$次
$(0,0)\to(3,0)\to(0,3)\Rightarrow(0,3)\to(3,3)\to(1,5)\to(1,0)\Rightarrow(0,1)\to(3,1)\to(0,4)$

证明：
先重写$L=(s+mb)a+(t-ma)b$，所以存在$s'>0,t'$使得$L=s'a+t'b$
我们设$u$为$b$倒水的次数，那么$b$桶中的水量则为
$$r=s'a-ub=s'a+t'b-ub-t'b=L-(u+t')b$$
我们要证明$r=L$，也就是证明$u+t'=0$，这里采用反证法：
如果$u+t'>0$那么$r<0$，矛盾！
如果$u+t'<0$那么$r>b$，矛盾！
所以$u+t'=0$
Q.E.D.
或者我们观察到里面同余的结构：
b中的水量$M\equiv s'a\mod b$所以$M=L$也即b中的水量就等于$L$
**线性组合本质上描述了一种同余关系**
## Euclid Algorithm
$$
\begin{aligned}
\gcd(a,b)
&= \gcd(b, a \bmod b) \\
&= \gcd(a \bmod b,\; b \bmod (a \bmod b)) \\
&\;\;\vdots \\
&= \gcd(r_{n-1}, r_n) \\
&= r_n.
\end{aligned}
$$
其中
$$
\begin{aligned}
a &= q_1 b + r_1, && 0 \le r_1 < b,\\
b &= q_2 r_1 + r_2, && 0 \le r_2 < r_1,\\
r_1 &= q_3 r_2 + r_3, && 0 \le r_3 < r_2,\\
&\;\;\vdots \\
r_{n-2} &= q_n r_{n-1} + r_n, && 0 \le r_n < r_{n-1},\\
r_{n-1} &= q_{n+1} r_n.
\end{aligned}
$$
因此，最后一个非零余数 $r_n$ 即为
$$
\gcd(a,b)=r_n.
$$
主要的引理是：
$$
\gcd(a,b) = \gcd(b, a\bmod b)
$$
证明：
因为，如果$m|a且m|b$，那么$m|(a\bmod b)且m|a$，由于$m$可以取为$\gcd(a,b)$，所以$\gcd(a,b) \mid \gcd(b, a\bmod b)$
同时，如果$m|b且m|r\ 其中r=a-tb$，那么一定有$m|a且m|b$，由于$m$可以取为$\gcd(b,a\bmod b)$，所以$\gcd(b, a\bmod b) \mid \gcd(a,b)$
所以$\gcd(a,b) = \gcd(b, a\bmod b)$
Q.E.D.

对定理2(**$\gcd(a,b)$是$a$和$b$的最小正线性组合**)的证明： 
先证明引理：$r_{n-1}和r_n$是$a和b$的线性组合，同时$\gcd(r_{n-1}, r_n)=\gcd(a,b)$
使用归纳法：
假设不变量$P(n)$：
$$
P(n):在进行n步\mathrm{Euclid}算法后到达\gcd(x,y)，则x和y是a和b的线性组合，同时\gcd(x,y)=\gcd(a,b)
$$
基础情况：当n=0的时候，x=a，y=b，显然成立
看归纳假设：
$y=a\bmod b=a-tb$是$a$和$b$的线性组合
$x = b$也是$a$和$b$的线性组合
同时由引理得到$\gcd(x,y)=\gcd(a,b)$
Q.E.D.
=>所以我们取$n$为Euclid算法运行的最大步数，就能得到$a$和$b$的最大公约数是其的一个线性组合

我们结合：$\gcd(a,b)\mid (sa+tb)$，同时又由于其是a和b的一个正线性组合，得到其小于所有的其他正线性组合，定理得证
## Extended Euclid Algorithm
扩展欧几里得算法在欧几里得算法的基础上增加两组序列，记为 $s_i$ 和 $t_i$，使得始终有  
$$  
r_i=s_i a+t_i b.  
$$
初始化为  
$$  
\begin{array}{c|ccc}  
i & r_i & s_i & t_i\\  
\hline  
0 & a & 1 & 0\\  
1 & b & 0 & 1  
\end{array}  
$$
在欧几里得算法每一步中，令
$$  
q_i=\left\lfloor\frac{r_{i-1}}{r_i}\right\rfloor,  
$$
并计算 
$$  
\begin{aligned}  
r_{i+1}&=r_{i-1}\bmod r_i,\\  
s_{i+1}&=s_{i-1}-q_i s_i,\\  
t_{i+1}&=t_{i-1}-q_i t_i.  
\end{aligned}
$$
当某一步得到  
$$  
r_{n+1}=0  
$$
时，最后一个非零余数即为  
$$  
r_n=\gcd(a,b).  
$$
由于  
$$  
r_n=s_n a+t_n b,  
$$
因此得到  
$$  
\gcd(a,b)=s_n a+t_n b.  
$$
#数论 #欧几里得算法 #素数 #状态机 #最大公约数