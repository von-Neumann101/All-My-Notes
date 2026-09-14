# Strongly Connected Components (SCCs)
**定义**：**强联通分量**是图$G=(V,E)$一个子图$G'=(V',E')$，满足**每个顶点**$v\in V'$都有一条路径到达其他**每个顶点**$u\in V'$
**定理**：**有向无环图**(DAG)都是其**强联通分量**的**DAG**
![[1d886f77bc7ed389eb635cca64e7000b.jpg|250]]
# Find Shortest Paths
## 概览
对于无权图，可以使用**BFS**(Breath First Search)，以$O(m+n)$得到最短路径
对于有权图：
如果权重大于0，可以使用**Dijkstra算法**，以$O((m+n)\log n)$得到最短路径
如果权重小于0（在金融领域使用，比如正权重花钱，正权重赚钱），这会非常复杂
![[3e3e076ef0b7eabe6265ce3407e32e66.jpg|193]]这称为负环(negative cycle)，$u\to v$的最短路径不存在
**Bellman-Ford算法**，以$O(mn)$得到最短路径或指明存在负环

如果我们把图限制为DAG，我们能以$O(m+n)$的复杂度得到最短路径
## DFS
[[Cross Correlation, Graphs#边的分类|边的分类]]
我们对下面的图运行DFS，得到每个边的分类（Tree edge一定是Forward edge）
![[ca6cccc1f1f7ac79d9fe257ef5128c61.jpg|419]]
我们只需要查看前序和后序就能判断每个边的类型

考虑边$e=(u,v)$
访问$u$，再访问$v$，离开$v$，再离开$u$$$\text{pre}(v)<\text{pre}(u)<\text{post}(v)<\text{post}(u)\Longrightarrow e\in T\cup F$$访问$v$，再访问$u$，离开$u$，再离开$v$
$$\text{pre}(u)<\text{pre}(v)<\text{post}(u)<\text{post}(v)\Longrightarrow e\in B$$
访问$v$，离开$v$，再访问$u$，离开$u$
$$\text{pre}(v)<\text{post}(v)<\text{pre}(u)<\text{post}(u)\Longrightarrow e\in C$$

**定理**：图$G$是一个DAG，当且仅当DFS没有找到Back edge
证明略（使用前序后序大小关系）

**定理**：在DAG中，每条边$e=(u,v)$，都有$\text{post}(v)<\text{post}(u)$
[[Relations, Partial Orders, and Scheduling#Relations|MIT 6.042J]]
**拓扑排序**：对顶点按其依赖顺序排序。具体算法是运行DFS，然后按照后序序号排序
![[ae8fdd31baf92d69d77512792ec7d330.jpg]]
拓扑排序就是B-E-A-D-C
[[MIT 6.042J/L6-Graph-Theory-and-Coloring/Graph-Theory-and-Coloring#定义|连通]]是一种[[Relations, Partial Orders, and Scheduling|等价关系]]。对于任何顶点，我们都能给出其等价类，所以可以将所有顶点划分为不相交的集合，满足集合内的顶点互相连通(SCCs)

**定理**：每个图都是其强联通分量的一个DAG
![[ffbd86536ce86e1dd7d3b658c92784e2.jpg]]

**约定**：源(source)强联通分量**没有来自别的SCCs的入边**，汇(sink)强联通分量**没有通向其他SCCs的出边**

![[556b5bf60021f121d3e76c6b18bbaee4.jpg|603]]

观察到，对于任意顶点$v\in \text{SinkSCC}$，运行$\text{DFS(v)}$只会访问$\text{SinkSCC}$中的点。我们只要从$\text{SinkSCC}$内的点开始，运行完以后就删除这个分量，最后就能遍历完整个图
**Alg**：
```text
label <- 0
repeat:
	if !visited[u] and inSinkSCC(u):
		label ++
		explore(u)
until all u labeled
```
注意到，如果一个顶点的post order最大，那么他一定在source SCC中。又由于sourceSCC更好求，我们反转所有的箭头，在新的图里求出来的source SCC就是原图的sink SCC
## Shortest Path
1. 边权均为1——BFS
选择一个点$s$，求出他到所有其他点的最短路径
**Data Structure**：队列$Q$
**Alg**：
记dist(u)为s到u的距离，特殊地，dist(s)=0. 对于其他所有的顶点$v_i$，dist($v_i$)=$\infty$，队列Q初始化为$[s]$
```text
while !isEmpty(Q):
	u = pop(Q)
	for (u, v) in E:
		if dist(v) = inf and !visited[v]:
			dist(v) = dist(u) + 1
			push(v)
```
 ![[ec1c519e55c272cd56b2b03a8c59dba1.jpg]]
我们要访问每个节点，同时也要走每个节点相连的边，所以运行时间为$\Theta(m+n)$

**补充**：对于一些特殊结构的图，比如Social Network，我们可以使用这些图特有的最短路径算法
#最短路径 #图 #BFS #强联通分量 #DAG 