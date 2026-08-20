# Dijkstra算法
`dist[u]`:=起点到`u`的**当前最短距离**
`prev[u]`:=从起点到`u`的最短路径上，`u`的前一个顶点
`Q`:=优先队列——这里使用二叉堆
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

#Dijkstra算法 #最短路径 #图 #堆 #优先队列 
# Bellman-Ford算法
