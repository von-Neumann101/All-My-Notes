# 可变性
一个列表在修改了内容以后仍然是同样的列表
```python
a = [10]
b = a
a.append(20)
print(a == b)
```
通过identity表达式判断两个表达式是否相同
```python
b = [10, 20]
print(f"a == b:{a == b}")
print(f"a is b:{a is b}")
```
**可变默认参数的风险**
函数的default参数值不会在每次调用时重新生成
```python
def f(s=[]):
	s.append(5)
	return len(s)
```
多次run：
```python
f()
```
# 可变函数
同样的输入值，返回不同的值
```python
def make_withdraw_list(ba):
	kb = [ba]
	def withdraw(amount):
		if amount > kb[0]:
			return "insufficient"
		else:
			kb[0] -= amount
			return kb[0]
	return withdraw
withdraw = make_withdraw_list(100)
```
kb始终指向[ba]这个列表
```python
withdraw(10)
```
换成int亦可：
```python
def make_withdraw_int(ba):
	kb = ba
	def withdraw(amount):
		if amount > kb:
			return "insufficient"
		else:
			kb -= amount
			return kb
	return withdraw
withdrawi = make_withdraw_list(100)
```
```python
withdrawi(10)
```