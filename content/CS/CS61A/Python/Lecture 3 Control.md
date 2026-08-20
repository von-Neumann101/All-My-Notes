## 3.1多重环境

顺着某个帧的父帧就可以找到整个环境


```python
%%script python
from operator import  mul
def square(x):
    return mul(x,x)
print(square(square(3)))
```

名称离开环境就没有意义，名称会被解析为在当前环境中最早找到他的那个那个帧里所绑定的值（帧可以理解为命名空间）

Global frame(环境的最后一帧):mul->func mul()  squre->func square()

f1:square`[parent=Global]`
x->3  Return value=9

f2:square`[parent=Global]`
x->9  Return value=81

比如f2中的x（在第二次运行square的时候），先在当前环境的第一帧里找（return mul(x,x)），x在帧里为9（最早），然后在f2中找有没有mul，再在下一个帧（Global Frame）里找到mul


```python
%%script python
from operator import  mul
def square(square):
    return mul(square,square)
print(square(4))
```

现在f2中有square->4(最早找到的)，找到以后就不会继续往下一个帧搜索的

## 3.2条件语句

False,0,'',None都是False value

`<left>`"Logical Operator"`<right>`

and:`<left>`为false,返回`<left>`,否则返回`<right>`

or:`<left>`为true,返回`<left>`,否则返回`<right>`


```python
print(2 and 3)
```

所有参数在函数调用之前求值，而条件语句会跳过不满足条件的语句，这就是为什么编程语言既需要函数语句也需要控制语句


```python
%%script python
from math import sqrt
def if_(c,t,f):
    if c:
        return t
    else:
        return f
def real_sqrt(x):
    if x>=0:
        return sqrt(x)
    else:
        return 0
def real_sqrt_(x):
    return if_(x>=0,sqrt(x),0)
n=int(input("Enter the number of elements: "))
print(real_sqrt(n))
print(real_sqrt_(n))
```

## 3.3迭代


```python
%%script python
def fib(n):
    pred,curr=0,1
    k=1
    while k<n:
        pred,curr=curr,pred+curr#利用定义移动下标，同时有记忆化
        k=k+1
    return curr
print(fib(5))
```

## 3.4控制表达式

`<left>`and`<right>`短路与，在`<left>`为false的时候不会执行`<right>`


```python
%%script python
from math import sqrt
def has_big_sqrt(x):
    return x>0 and sqrt(x)>10
def reasonable(n):
    return n==0 or 1/n != 0
a=10
print(has_big_sqrt(a))
print(reasonable(a))
```
