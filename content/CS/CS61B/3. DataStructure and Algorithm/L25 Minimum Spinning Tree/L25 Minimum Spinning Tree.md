给定一个无向图，检测其是否含有环
1. DFS（一直走直到遇到标记的顶点），其时间复杂度是O(V+E)[[3. DataStructure and Algorithm/L23 BFS, DFS and implementations/L23 BFS, DFS and implementations#^80d554|时间复杂度]]
2. WeightQuickUnionUF，我们把融合遇到的顶点，如果一个顶点的两边都被连接——环，其时间复杂度是O(V+E$\alpha$(V))
# 最小生成树（MST）
生成树定义：无向图的一个子图，所有顶点在子图中可到达，且无环，并且包含所有的顶点
最小生成树就是边权和最小的生成树
## cut property
Cut：**将顶点分配到两个非空集合**（就是数学上的划分）
crossing edge：连接两个不同cut元素的边
Cut property：对于任意的cut，最小权的crossing edge一定在MST中
注意，cut虽然有点像刀切，但是下面也是cut
![[Pasted image 20260409195050.png|472]]
证明最小割性质
![[Pasted image 20260409200026.png]]假设最小的crossing edge——e，不在MST里，那么一定有另外一条边连接了两边而且权比e大，我们把f换成e，得到一个更小的树，矛盾！
但是我们找全部的割过于慢且不够优雅
# Prim's Algorithm
我们任意选择一个起始点，然后选择最小的边，他至少有一个节点在最小生成树内部（这么解释有点怪，看下面的例子）
![[Pasted image 20260409201553.png|237]]
先往C走
然后注意，我们的割将变为(A,C)和(其他的点)
![[Pasted image 20260409201733.png|313]]
然后到E
![[Pasted image 20260409201842.png|301]]
![[Pasted image 20260409201914.png|303]]
红色线代表的就是我们待选的边（最小割性质）

这里和DIjistra有点像但是又有所不同，因为dijistra在意的是原点的距离，而Prim考虑的是目前构建树的距离，这两个等价的
![[Pasted image 20260409203036.png]]


> [!NOTE] 优先队列
> 看到这里可能你会疑惑，优先队列在干嘛？好像一直提到他。
> 他的作用很简单，用来存储数据并找到最小，并弹出它（当我们找到了某个顶点的最短路径，我们就得弹出它，对于不确定的，我们先放到优先队列里
> 因为我们要存储访问的顶点的信息，我们可以用数组来实现，但这会很慢
> Note： decreasePriority(v, 新的更小的 dist)



![[Pasted image 20260409203141.png]]![[Pasted image 20260409203222.png]]

复杂度
![[Pasted image 20260409204524.png]]
每个顶点都会被删一次，每个顶点都会被加入一次，我们每次要扫描约E个值，然后更新（比如从∞变到1）
# Kruskal Algorithm
![[Pasted image 20260409205252.png]]
先把所有边权排一排，然后一个个添加，每次添加就问：是不是有环？
![[Pasted image 20260409210237.png]]
有环？跳过！
一直这么做直到全部连上
![[Pasted image 20260410095607.png]]
我们用并查集来检测是否联通
![[Pasted image 20260410100059.png|434]]
![[Pasted image 20260410100153.png]]
#DAG #环 #最小生成树 #Prim算法 #Kruskal算法 #最小割性质 #环检测 #图 #优先队列