# 独立
**定义**：如果$P(A\mid B)=P(A)$ 或 $P(B)=0$，那么称事件$A$和$B$独立
![[Pasted image 20260620100903.png|448]]
注意：互斥事件不一定独立

**定理**（独立事件的乘法法则）：如果$A$和$B$独立，那么$P(A\cap B)=P(A)P(B)$

**Example**：
分别抛掷两个公平、独立的硬币。记事件$A:两个硬币结果一样$，事件$B:第一个硬币为正面$。我们设硬币正面的概率为$p$，反面的概率为$1-p$
$P(A\mid B)=p$，$P(A)=p^2+(1-p)^2$
事件$A$和$B$独立，当且仅当$p=0或p=\frac12$
**可以看出，独立性并不能通过所谓的“语义”来判断。上面的例子中，除了p的两个取值以外，其他情况中，事件A和B都是不独立的**

**定义**：事件 $E _ { 1 }, E _ { 2 }, \ldots, E _ { n }$ 是相互独立的，当 $\forall i \in[ 1, n ]$ 且 $\forall S \subseteq [ 1, n ] /\{ i \},$ 有
$$
\operatorname* { P r } \left[ \, \bigcap _ { j \in S } E _ { j } \, \right] = 0 \quad { \mathrm { o r } } \quad \operatorname* { P r } [ E _ { i } ] = \operatorname* { P r } \left[ \, E _ { i } \, \, { \bigg | } \, \, \bigcap _ { j \in S } E _ { j } \, \right].
$$
**定理**：事件 $E _ { 1 }, E _ { 2 }, \ldots, E _ { n }$ 是相互独立的，当且仅当 $\forall S \subseteq[ 1, n ]$
$$
\operatorname* { P r } \left[ \, \bigcap _ { j \in S } E _ { j } \, \right] = \prod _ { j \in S } \operatorname* { P r } [ E _ { j } ].
$$
这里也可以看出，独立性是**不具有传递性**的

**Example**：
抛掷三枚公平、独立的硬币。
记事件$A_1:硬币1和硬币2一样$，$A_2:硬币2和硬币3一样$，$A_3:硬币3和硬币1一样$
$P(A_i)=\frac12$
$P(A_i\cap A_j)=\frac14$（所有硬币都一样）
这里就证明了三个事件**两两独立**
$P(A_i\cap A_j\cap A_k)=P(A_i\cap A_j)=\frac14\ne P(A_1)P(A_2)P(A_3)$
所以这三个事件**不相互独立**

**Example**：
M个人中，两个人相同生日（共N种生日）的概率
我们做出两个假设：
- 生日均匀分布（实则不然）
- 每个人的生日独立
Fact：23个人就有约50%的概率（365天）
我们利用树来表示生日的关系：
每个人有N个可能的生日，对于第一个人每个生日日期$v_1\sim v_N$的可能性，我们都能创造一条M-1个人的世界线——这是一个**深度为M的满N叉树**
样本空间$S=\{(b_1,b_2,...,b_M)\mid b_i\in V\}$，显然$|S|=N^M$
任意一种可能的组合出现的概率为$p=\frac{1}{N^M}$
从反面计算，一共有$\tbinom{N}{M}$种每个人生日都不一样的情况
所以存在相等生日的概率为
$$
p=1-\frac{N!}{(N-M)!N^M}\sim1-e^{-\frac{M^2}{2N}}
$$
当然，可以把这个问题抽象，这实际是一个HashMap的问题——我们不能让两个不相同的元素有相同的HashCode——M个数据，两个数据的HashCode（共N种HashCode）相等的概率尽可能小
#独立性  #哈希 #树 