# Cross Correlation
给定向量$y=(y_0,y_1,...,y_{n-1}),x=(x_0,x_1,...,x_{m-1})\quad(m<n)$，计算所有的
$$d_i=\sum_{k=0}^{m-1}x_ky_{i+k},\quad i = 0,1,...,n-m$$
## String Matching
判断字符串$S$是否和字符串$P$
先对问题进行简化，我们只考虑$S$和$P$是二进制串的情况。
我们想使用点积来判断匹配的情况，但是可以发现**点积类似于一种$\land$运算**，所以我们要对原来的向量进行一些**映射**:$0\mapsto(0,1),1\mapsto(1,0)$，这样我们就能保证$0*0=1,1*0=0,1*1=1$了
**所以当且仅当映射后向量的点积为$m$，$S$的和$P$匹配**
## FFT's application
先考虑以下多项式的乘积：
$$
X(z)=\sum_{j=0}^{m-1}x_jz^j,\qquad Y(z)=\sum_{j=0}^{n-1}y_jz^j
$$
这是柯西乘积，下标之和为定值，这并不是Cross Correlation的形式（下标差为定值）。我们考虑反转下标即可（减法是加上负数）
$$
X'(z)=\sum_{j=0}^{m-1}x_jz^{m-1-j},\qquad Y(z)=\sum_{j=0}^{n-1}y_jz^j
$$
他们的乘积为：
$$
(X'Y)(z)=\underbrace{(x_{m-1}y_0)}_{下标差为m-1}z^0+\underbrace{(x_{m-1}y_1+x_{m-2}y_0)}_{下标差为m-2}z+...+\underbrace{(x_0y_0+x_1y_1+...+x_{m-1}y_{m-1})}_{下标差为0}z^{m-1}+...
$$
我们从$m-1$次项以后的系数里就可以提取到我们需要的Cross Correlation的形式
#字符串匹配 #FFT #多项式乘法 #字符串相似度 #快速傅里叶变换
# Graph
***记号约定：$n$总是表示顶点数量，$m$总是表示边的数量***
本节的内容均在Match仓库的MIT 6.042J的图论部分中
**超图**(Hypergraph)：如果我们把一个图的边看做**顶点的二元组**，那么超图的边就是**顶点的$n$元组**
## Representing graphs to computer
### Adjacency matrix
二维布尔数组`A[i][j]=1`等价于$(i,j)\in E$
特殊地，对于无向图$A^T=A$
### Adjacency list
一维指针数组，数组的第$i$位代表第$i$个顶点，其指向的链表（或数组）代表**与其相邻的顶点**之集合
### Summary

|      | Adj matrix | Adj list |
| ---- | ---------- | -------- |
| 内存消耗 | $n^2$      | $n+m$    |
| 是否连通 | $1$        | $d_u+1$  |
| 邻居查找 | $n$        | $d_u+1$  |
一般使用邻接表来表示图
## Depth First Search (DFS)
探索图的一种算法（$u,v$是否连通，$u$可以通向哪些点……）
```text
DFS(G=(V,E)):
	t <- 0
	visited[1...n] <- false
	preorder[1...n], postorder[1...n]
	for u in V:
		if !visited[u]:
			visited[u] = true
			explore(u)

def explore(u):
	preorder[u] <- t++ #进入这个顶点的时间
	for (u,v) in E:
		if !visited[v]:
			visited[v] = true
			explore(v)
	postorder[u] <- t++ #退出顶点的时间
```
一般来说，`DFS`还需要传入一个参数，指定开始的顶点（而不是遍历每一个顶点）
**Example**：
![[bbc00a7347f4bf99175d1eba8f66802b.jpg|511]]
return代表`explore`的调用结束了；蓝色的`[a,b]`代表他们前序、后序数组里的值

**断言**：从顶点$v$运行DFS，顶点$u$和$v$连通当且仅当`visited[u] = true`
证明略

DFS runtime：
无论使用何种图表示方法，我们前面需要初始化变量，这需要$O(n)$的时间

|           | Adj matrix | Adj list |
| --------- | ---------- | -------- |
| 遍历所有$u$邻居 | $n^2$      | $n+m$    |
## 边的分类
$e=(u,v)$
- Tree edge：$e\in \text{DFS tree}$
- Back edge：顶点$u$是DFS树中$v$的后代（D-A）
- Forward edge：顶点$u$是$v$的祖先，且$(u,v)$不是Tree edge（A-F）
- Cross edge：其他的所有边
#图 #DFS