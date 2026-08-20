**定理**：给定一个概率空间$S$，事件$A_1,A_2,...,A_n\subset S$，发生这些事件的数量的期望等于$\sum_{i=1}^nP(A_i)$
主要的思路是将事件用指示来解释，然后利用期望的线性性来分别计算指示的概率（较为容易）

**定理**：$P(T\ge 1)\le\mathbb E[T]$，这里的$T$是事件发生的数量
不过这个只在期望比较小（小于1）的时候有意义

**定理**（墨菲定理）：如果有**互相独立**的事件$A_1,A_2,...,A_n$，那么他们都不发生的概率$P(T=0)\le \exp({-\mathbb E[T]})$
>Proof.
>$P(T=0)=P(\bar A_1\bar A_2...\bar A_n)=\prod_{i=1}^n(1-P(A_i))\le\prod \exp(-P(A_i))=\exp({-\mathbb E[T]})$

**定理**（期望的乘积法则）：如果随机变量$R_1,R_2,...,R_n$是相互独立的，那么
$$\mathbb E[R_1R_2...R_n]=\mathbb E[R_1]\mathbb E[R_2]...\mathbb E[R_n]$$

**Example**：
以下是RISC和CISC指令集在处理不同Benchmark的代码量，我们求代码量的比值再取平均，便可以判断指令集的好坏（吗？）
![[Pasted image 20260626134753.png|411]]
![[Pasted image 20260626134810.png|396]]
可以看到，我们用CISC/RISC会发现CISC的代码量平均比RISC高20%，但是反之，我们又得到CISC的代码量平均比RISC低10%——这里有问题，不可能一个东西又好又坏

我们记$x$为benchmark，$R(x),C(x)$分别为RISC和CISC在$x$上的代码量，$P(x)$是$x$出现的概率（假设其为均匀的（吗？））
$\mathbb E(C/R)=1.2$但是我们无法推出$\mathbb E(C)=1.2\mathbb E(R)$，期望并没有除法法则
#期望 #墨菲定理