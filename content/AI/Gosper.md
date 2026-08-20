# Gosper 算法流程

目标：求

$$
\sum a_k
$$

也就是找一个 \(S(k)\)，使得

$$
a_k=S(k)-S(k-1)
$$

---

## 1. 计算相邻项比值

先算

$$
\frac{a_k}{a_{k-1}}
$$

如果它不是关于 \(k\) 的分式，Gosper 算法不适用。

如果可以写成

$$
\frac{a_k}{a_{k-1}}=\frac{A(k)}{B(k)}
$$

则继续。

---

## 2. 初始设定

先取

$$
p(k)=1,\qquad q(k)=A(k),\qquad r(k)=B(k)
$$

也就是

$$
\frac{a_k}{a_{k-1}}
=
\frac{p(k)}{p(k-1)}\frac{q(k)}{r(k)}
$$

---

## 3. 处理冲突因子

检查有没有这种情况：

$$
(k+a)\mid q(k)
$$

$$
(k+b)\mid r(k)
$$

并且

$$
a-b=0,1,2,3,\dots
$$

如果没有，进入下一步。

如果有，就做：

$$
q(k)\leftarrow \frac{q(k)}{k+a}
$$

$$
r(k)\leftarrow \frac{r(k)}{k+b}
$$

$$
p(k)\leftarrow p(k)(k+b+1)(k+b+2)\cdots(k+a)
$$

然后重复检查，直到没有这种冲突因子。

---

## 4. 统一记号

原来的 Gosper 方程是

$$
p(k)=q(k+1)f(k)-r(k)f(k-1)
$$

为了书写方便，把 \(q(k+1)\) 重新记成 \(q(k)\)。

于是方程写成

$$
p(k)=q(k)f(k)-r(k)f(k-1)
$$

---

## 5. 计算指标 \(d\)

先定义

$$
Q(k)=q(k)-r(k)
$$

$$
R(k)=q(k)+r(k)
$$

再分别计算次数：

$$
P=\deg p(k)
$$

$$
u=\deg Q(k)
$$

$$
v=\deg R(k)
$$

### 情况一：如果

$$
u\ge v
$$

那么

$$
d=P-u
$$

### 情况二：如果

$$
u<v
$$

那么通常取

$$
d=P-v+1
$$

如果算出

$$
d<0
$$

则 Gosper 算法失败。

---

## 6. 设 \(f(k)\)

设

$$
f(k)=c_0+c_1k+c_2k^2+\cdots+c_dk^d
$$

代入

$$
p(k)=q(k)f(k)-r(k)f(k-1)
$$

展开后，比较 \(k\) 的各次幂系数，解出

$$
c_0,c_1,c_2,\dots,c_d
$$

如果解不出来，说明 Gosper 算法失败。

---

## 7. 写出 \(S(k)\)

如果求出了 \(f(k)\)，则

$$
S(k)=\frac{q(k)}{p(k)}f(k)a_k
$$

于是

$$
a_k=S(k)-S(k-1)
$$

所以

$$
\sum_{k=m}^{n}a_k=S(n)-S(m-1)
$$

---

# 例子：求 \(\sum_{k=1}^{n}k2^k\)

令

$$
a_k=k2^k
$$

---

## 1. 计算相邻项比值

$$
\frac{a_k}{a_{k-1}}
=
\frac{k2^k}{(k-1)2^{k-1}}
=
\frac{2k}{k-1}
$$

所以

$$
A(k)=2k,\qquad B(k)=k-1
$$

初始取

$$
p(k)=1,\qquad q(k)=2k,\qquad r(k)=k-1
$$

---

## 2. 处理冲突因子

\(q(k)=2k\) 里面有因子

$$
k=k+0
$$

\(r(k)=k-1\)，也就是

$$
k-1=k+(-1)
$$

所以

$$
a=0,\qquad b=-1
$$

因此

$$
a-b=1
$$

这是非负整数，需要处理。

于是

$$
q(k)\leftarrow 2
$$

$$
r(k)\leftarrow 1
$$

$$
p(k)\leftarrow k
$$

所以最后得到

$$
p(k)=k,\qquad q(k)=2,\qquad r(k)=1
$$

---

## 3. 计算指标 \(d\)

这里

$$
q(k)=2,\qquad r(k)=1
$$

所以

$$
Q(k)=q(k)-r(k)=2-1=1
$$

$$
R(k)=q(k)+r(k)=2+1=3
$$

因此

$$
\deg Q(k)=0
$$

$$
\deg R(k)=0
$$

$$
\deg p(k)=1
$$

因为

$$
\deg Q(k)\ge \deg R(k)
$$

所以

$$
d=\deg p(k)-\deg Q(k)=1-0=1
$$

因此设

$$
f(k)=Ak+B
$$

---

## 4. 解 \(f(k)\)

Gosper 方程是

$$
p(k)=q(k)f(k)-r(k)f(k-1)
$$

代入

$$
p(k)=k,\qquad q(k)=2,\qquad r(k)=1
$$

得到

$$
k=2f(k)-f(k-1)
$$

设

$$
f(k)=Ak+B
$$

则

$$
f(k-1)=A(k-1)+B=Ak-A+B
$$

所以

$$
2f(k)-f(k-1)
=
2(Ak+B)-(Ak-A+B)
$$

整理得

$$
2(Ak+B)-(Ak-A+B)=Ak+A+B
$$

因此

$$
Ak+A+B=k
$$

比较系数：

$$
A=1
$$

$$
A+B=0
$$

所以

$$
B=-1
$$

因此

$$
f(k)=k-1
$$

---

## 5. 写出 \(S(k)\)

$$
S(k)=\frac{q(k)}{p(k)}f(k)a_k
$$

代入：

$$
S(k)=\frac{2}{k}(k-1)k2^k
$$

所以

$$
S(k)=(k-1)2^{k+1}
$$

于是

$$
k2^k=S(k)-S(k-1)
$$

---

## 6. 得到求和结果

$$
\sum_{k=1}^{n}k2^k
=
S(n)-S(0)
$$

其中

$$
S(n)=(n-1)2^{n+1}
$$

$$
S(0)=(-1)2^1=-2
$$

所以

$$
\sum_{k=1}^{n}k2^k
=
(n-1)2^{n+1}-(-2)
$$

最终

$$
\boxed{
\sum_{k=1}^{n}k2^k=(n-1)2^{n+1}+2
}
$$