品鉴过无数次了：
[[Minimum-Spanning-Trees|一些树有关的证明]]
[[L25 Minimum Spinning Tree|最小割性质及其证明]]


**Meta-Algorithm**：
先初始化边集$X=\varnothing$，然后重复$n-1$次：
1. 选择一个Cut，使得任何$e\in X$，$e$不跨越Cut（这一步的做法产生两种不同算法——Kruskal和Prim算法）——这一步的目的是防止成环
2. 将Cut中权重最小的的Cross edge加入$X$

Kruskal算法在MIT 6.042J里证明过了，Prim算法使用最小割性质是显然的

**Implementing Kruskal**：
1. 初始化边集$X=\varnothing$并按权重排序所有的边
2. 按照边递增的顺序，添加不成环的边（这里使用DFS从加的边的任意顶点开始遍历$X$）

一共有$m$条边，然后对每条边使用DFS，所以时间复杂度是$O(mn)$

**Optimization**：
- 并不需要使用DFS检查环，我们只需要检查**边的两端是否是属于同一个联通分量**，这里需要用到[[L15 Disjoint Set|并查集]]
  由于[[L15 Disjoint Set#^839a7d|并查集的复杂度]]是$O(\log^*n)$，几乎接近常数。所以优化的算法的时间复杂度几乎是线性的

Prim算法和Dijkstra算法有相似之处：
Prim算法是把“当前路径”打包为一个连通分量，然后再求一个最短距离，由于每次都会使得顶点数-1（因为打包了），所以最后自然会把所有顶点纳入其中
