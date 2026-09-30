可以去看RL base中的Bellman方程，可以很好地理解DP
# Dynamic Programming
使用查找表加速递归 / 从子问题开始扩散
## Fibonacci
普通：
```python
def fib(n):
	if n <= 1:
		return n
	else:
		return fib(n-1) + fib(n-2)
```
这里维护了一个缓存，可以查表以加速递归：
```python
def cache(memo, n):
	if n <= 1:
		return n
	elif memo[n] != None:
		return memo[n]
	else:
		memo[n] = cache(memo, n-1) + cache(memo, n-2)
		return memo[n]

def fib_cache(n):
	memo = [None]*(n+1)
	return cache(memo, n)
```
自底向上：
```python
def fib_bottomup(n):
	memo = [None]*(n+1)
	memo[0], memo[1] = 0, 1
	for i in range(2, n+1):
		memo[i] = memo[i-1] + memo[i-2]
	return memo[n]
``` 
实际上我们只需要维护两个量就行了，因为`memo[i]`只来源于两个量，之前的历史不需要了
## Single Source Shortest Path
DAG：
![[ChatGPT Image 2026年9月23日 10_32_37.png|205]]
最简单的递推（最优子结构）：
$$
f(u)=\operatorname*{min}_{(u,v)\in E}\left[f(v)+w(v,u)\right]
$$

运行时间分析：
首先注意到，实际上我们要反转图中的箭头——因为递归的结构是从最后的节点不断往初始延伸的
- 反转图：每个顶点和每个边都必须访问一次，所以是$O(m+n)$
- dp（记忆化）：由于每次都记忆$f(v)$，所以只需要考虑$w(v,u)$的消耗即可——也就是考虑每一个顶点的入边（反转图的出边），所以是$O(m+n)$
