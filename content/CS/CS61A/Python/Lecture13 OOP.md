# OOP
复杂大型程序拆分成小型模块化组件
不是建立一个很长信息列表，再用函数来操作它，而是让一堆不同对象相互交互（方法），对象管理自己的信息
函数是全局的，方法是专属的
类定义了对象的行为
例如银行账户：Account类
不顾持有人是谁，余额多少，进行怎样的操作，都是一样的
```python
class Account:
	interest = 0.02 #use it in the future
	def __init__(self, account_holder):
		self.balance = 0
		self.holder = account_holder
	
	def deposit(self, amount):
		self.balance += amount
		return self.balance
	
	def withdraw(self, amount):
		if amount > self.balance:
			return 'Insufficient'
		else:
			self.balance -= amount
			return self.balance
```
# 创建实例
```python
a = Account('awa')
```
调用一个类的时候会创建改类型的一个实例，通过init方法（类似构造器，对象创建时自动调用对其初始化）
创建的实例作为init的第一个参数`self`，调用Account时传入的参数依次对应init后面的参数
```python
type(a)
```
使用is判断两个变量名是否指向同一个对象（调用类就会创建一个独一无二的方法）
# 方法调用
通过“.”表达式，调用实例的类定义的方法
```python
a.deposit(100)
```
`<name>.<method>`叫做绑定方法，通过self绑定到对应的方法
```python
f = a.withdraw
```
```python
f(100)
```
# 属性查找
`<expression>.<name>`左边的表达式返回一个对象，右边的是要查找的属性名
```python
a.holder
```
name可以是实例的属性，也可以是*类的属性*（有限查找对应实例属性）
使用函数查找：
```python
getattr(a, 'holder')
```
判断是否有属性：
```python
hasattr(a, 'deposit')
```
# 类属性
```python
class Clown:
	nose = 'big and red'
	def dance():
		return 'No thanks'
```
```python
print(Clown.nose)
print(Clown.dance())
```
**类属性会在所有实例中共享**
# 绑定方法
通过类查找方法，得到的就是普通函数。通过实例查找，得到的就是绑定方法
其中对象作为绑定方法的第一个参数传入
# 属性赋值
```python
jim_account = Account('Jim')
tom_account = Account('Tom')
```
实例jim_account没有interest，于是用jim_account*修改*类属性的时候，会给这个实例**创建一个**属性
```python
jim_account.interest = 0.03
print(tom_account.interest)
```
jim_account的interest属性就不再会随着类属性变化而变化了
# 继承
类和类直接不完全孤立，他们之间可能有联系
```
class <name>(<base class>):
	<suite>
```
支票账户（在一般银行账户上加了手续费，以及利率降低：
```python
class CheckingAccount(Account):
	withdraw_fee = 1
	interest = 0.01
	def withdraw(self, amount):
		return Account.withdraw(self, amount + self.withdraw_fee)#not the bounded method
```
属性查找：子类没有新定义父类有的属性时，子类该属性继承父类
方法同理

**组合**：has-a关系
银行类和账户类：银行类有**账户列表**作为属性，账户也不会继承银行，银行也不会继承账户。他们是组合关系
```python
class Bank:
	def __init__(self):
		self.accounts = []

	def open_account(self, holder, amount, kind=Account):
		account = kind(holder)
		account.deposit(amount)
		self.account.append(account)
		return account

	def pay_interest(self):
		for a in self.accounts:
			a.deposit(a.balance * a.interest)
```
# 属性查找例子
没有`__init__`方法，实例就没有实例属性（`__init__`本身就是方法，所以子类没有就会查找基类）
```python
class A:
	z = -1
	def f(self, x):
		return B(x-1)
		
class B(A):
	n = 4
	def __init__(self, y):
		if y:
		    self.z = self.f(y)
		else:
			self.z = C(y+1)

class C(B):
	def f(self, x):
		return x
```

`C(2)`：首先由于C没有`__init__`方法，他会去B（父类）查找。y=2传入，`C(2)`的实例属性添加 **z** ，值为`self.f(y)`，由于创建的是C的实例，所以调用的f是C的f。那么该实例的值为2
`B(1).z.z.z`：B(1): z -> B(0): z -> C(1): z = 1
# 多继承（Java没有）
没有什么特殊的，就是查找时从多个基类中查找
