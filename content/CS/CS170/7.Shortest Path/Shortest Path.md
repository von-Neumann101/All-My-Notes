# Dijkstra算法
`dist[u]`:=起点到`u`的**当前最短距离**
`prev[u]`:=从起点到`u`的最短路径上，`u`的前一个顶点
`Q`:=优先队列——这里使用[[L21 Priority queue, Heap#Heap|二叉堆]]
**Alg**(Dijkstra)：
```text
dist <- inf
prev <- null
dist[s] <- 0
Q q = Q(V, dist) #所有的顶点和其距离进入优先队列
while Q not empty:
	u = popMin(Q)
	for all (u, v) in E:
		e = (u, v)
		if dist(v) > dist(u) + e.length:
			dist[v] <- dist[u] + e.length
			prev[v] <- u
			decreaseDist(v, dist(v))
```
**Example**：（从A开始）
![[bb3b2a6323cfaad0a3e01a984346a00c.jpg|281]]
![[084b8aaceb31a0316e9a02d3343e4b3d.jpg|593]]
红线标注的表示每次被弹出的元素

时间复杂度：$Q + n \times \text{popMin}+ O(m) + m \times \text{decreaseDist}=O((m+n)\log n)$

**理解**：
先看表的第一列，这是在A中，到A的距离。根据图，只有A能到A，所以`dist[A]=0`，（说了一些在后面看起来有意义的话）
再看表的第二列，这是**在B、C中**（A被弹出了），B和C分别到A的距离。根据图，B、C到A的距离分别为4、2，我们发现**在A、B、C这个子图**中。A到C的距离是当前最短的，那么他一定是**在A、B、C、D、E这个图中最短的**。如果在整个图中有比ABC子图更短的，那么一定是A-xxxxx-C，但是在非负边权图中，不可能绕原路反而更短的情况，所以矛盾！

#Dijkstra算法 #最短路径 #图 #堆 #优先队列
**二叉堆**：
保证父节点小于子节点
![[a59ff74a1729c2dc35369d6a99d7f7a4.jpg|582]]
![[f16e6e5cc2687ec4ddf7cf4b6fa115ad.jpg]]
斐波那契堆可以使得时间复杂度降为$O(n\log n+m)$
# Bellman-Ford算法
![[7e70685e0673c047fee457b0802c886a.jpg|189]]
Dijkstra给出S到A的最短距离是3，因为在SAB这个图中，S-A=3最短，所以S-A在整个图中最短。然而这是错误的，原因在于**负边权的图中，绕远路可能会更近**

```text
update(u,v):
	if dist(v) > dist(u) + e.length:
		dist[v] <- dist[u] + e.length
		prev[v] <- u
```
无论边权的正负，以及该操作执行的次数，我们都不会改变最短路径的结果。**这个操作永远能给出一个最短路径的正确上界**，问题只是这个上界是否是或者接近最短路径

我们假设$s\to u_1\to u_2\to...\to u_k\to t$是从$s\to t$的最短路径，且**没有负环**。那么易知$k\le n-2$，然后运行操作`update(s,u_1), update(u_1,u_2), ... , update(u_k,t)`
我们需要**最短路径上的**任意两个节点间的距离也是**全局的**最短距离，否则我们能找到一个更短的路径，这与假设矛盾

但是我们**在开始并不知道这个最短路径**，而我们又需要确保更新到最短路径的每一条边，最稳定的方法就是：**每次都更新所有的边**。比如第一次`update`所有的边，就一定能`update(s,u_1)`；第二次`update`所有的边，就一定能`update(u_1,u_2)`（当然，顺序并不重要，我们只要能确保每次更新都能使得最短路径上的一个边被更新即可）

容易得到其时间复杂度为$O(mn)$

**优化**：如果`dist`停止变化，那么可以停止算法。
**在没有负环的情况下，算法最多运行n-1次**（因为最短路径最多有n-1条边，n-1次运行肯定能覆盖到所有边）。显然如果**没有负环的话，当`dist`不再变化时，继续运行算法`dist`也不会变化**，意味着算法中止。但是如果运行完第n-1次后，再运行一次的时候，`dist`改变，则意味着**一定存在负环**（否则`dist`不变）

对于DAG来说，可以使用更好的顺序来运行Bellman-Ford算法，以下是反例（蓝色数字代表运行顺序，即先BC最后SA）
![[d8552f009a20e93c3ee7d7ea2f293adf.jpg|639]]
第一步先对BC更新，发现C原来到S的距离为∞，但是经过BC以后是∞-1，更新C到S的距离为∞-1（也可以不更新，∞-1还是∞）

最好的顺序是先SA，最后BC。我们先进行[[Graph Theory#DFS|DFS]]，按**递减的后序**对顶点进行排序（时间复杂度$O(m+n)$）——上图的例子就是SABC的顺序更新（那么这只需要访问每个边一次即可）

**补充**：2026年的《Bellman-Ford in Almost-Linear Time》以一种巧妙的方式给出了更好的复杂度——渐进线性


