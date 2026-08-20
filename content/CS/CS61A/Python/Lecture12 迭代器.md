# 迭代器
iter返回一个迭代器（这里是t）
![[Pasted image 20260227122453.png]]
```python
s = [[1, 2], 3, 4, 5]
t = iter(s)
```
```python
next(t)
```
list()函数会直接将迭代器用完
```python
list(t)
```
# 字典的迭代
可以创建字典的keys，values，items的迭代器，默认是keys
在使用字典的迭代器的过程中，字典**大小**发生变化，迭代器失效
# for语句
```python
r = range(3, 6)
ri = iter(r)
```
```python
next(ri)
print(ri)
```
for语句会改变迭代器的位置
```python
for i in ri:
	print(i)
```
# 内置迭代函数
他们返回一个**迭代器**
map，filter，zip，reversed都是

例如：map函数返回一个序列，其将传入的func应用到传入的序列的每一个元素上，返回对应序列的迭代器
```python
asd = ['a', 's', 'd']
ia = map(lambda x:x.upper(), asd)
for i in ia:
	print(i)
```
# zip函数
zip函数将索引相同的元素打包为一个tuple（跳过多余索引的元素）
```python
list(zip([1, 2],[3, 4, 5]))
```
# 使用迭代器
数据抽象：无论是list，tuple还是map，怎样改变数据的表示，使用迭代器的抽象，都不用重写代码（我们只取其可迭代的属性）
迭代器把可迭代对象和其位置打包保存
通过传递迭代器，而不是位置，你可以保证每个元素只被处理最多一次
# 生成器
由生成器函数（yield一个值，而不是return一个值）返回的特殊迭代器
```python
def plus_minus(x):
	yield x
	print("x")
	yield -x
	print("-x")
	yield "awa"
t = plus_minus(3)
```
```python
next(t)
```
```python
list(t)
```
语句执行到yield时暂停，等迭代器next以后，才开始继续执行下面的语句
# 生成器和迭代器
`yield from`用于一个可迭代对象，等于yield其所有的元素
```python
def a_then_b(a, b):
	yield from a
	yield from b
print(list(a_then_b([1, 2, 3],[4, 5])))
```
```python
def prefixes(s):
	if s:
		yield from prefixes(s[:-1])
		yield s
def substring(s):
	if s:
		yield from prefixes(s)
		yield from substring(s[1:])
```
```python
print(list(prefixes("fyr")))
print(list(prefixes("yr")))
print(list(prefixes("r")))
print(list(substring("fyr")))
```
# 例子：数的分拆
`partitions(n,k)`:将n用不减的、不超过k的数字分拆的方法数
```python
def partitions(n, m):
	if n < 0 or m == 0:
		return []
	else:
		exact_match = [] if n != m else [str(m)]
		with_m = [p + '+' + str(m) for p in partitions(n-m, m)]
		without_m = partitions(n, m-1)
		return exact_match + with_m + without_m
print(partitions(6,4))
```
随想：我们就假设我们知道`partitions(n-m, m)`的内容（其实递归就是归纳法的逆向）
```python
def partitions(n, m):
	if n > 0 and m > 0:
		if n == m:
			yield str(m)
		for p in partitions(n-m, m):
			yield p + '+' + str(m) 
		yield from partitions(n, m-1)
print(list(partitions(6,4)))
```
这就更加的形象了（加了list()以后我们就把yield当成返回一个列表的东西）：
1. 完全匹配
2. 从n-m的分拆中挑选元素加上m
3. 无法选m，直接照搬n的分拆
这有一个好处，对于大数的分解，我们可以只从其中选择部分样例计算（这里可以体现lazy机制的优势）