## 2.4函数定义
Python的赋值是**一次性**的，而非同步(注意这和Cpp的区别)
```python
%%script python
a=3
b=a*2
a=4
print(b)
```

可以“赋值”函数
```python
%%script python
f=max
print(f(1,2))
max=7
print(f(1,2,max))
```

```python
i=0
i+1
print(i)
```

函数会在**调用**时重新计算


```python
%%script python
a=2
b=3*a+a*a #b=10
def adds():
    return a+b
print(f'a=2 函数:{adds()}')
a=3
print(f'a=3 变量:{b}')
print(f'a=3 函数:{adds()}')
```

Local Frame就是函数在调用时创建的，用于保存这次函数调用的所有本地变量的一块命名空间（保存name和value的绑定关系）

函数的`<test>(<formal parameters>)`就是函数的签名(signature),签名包含了构建Local Frame的所有信息，告诉我们函数调用时对应的帧

**环境就是sequence of frame**


```python
%%script python
from operator import mul
def square(square):
    return mul(square, square)
print(square(-2))
#调用square函数时，先查找square定义，然后创建帧，把square和-2关联起来
```

## 2.5 print and None

None:=函数没有任何返回值返回的值

Pure Function:abs()——传入-2，返回2

Non-Pure Function:print()——传入-2，返回None，产生Python display the output "-2"效果


```python
print(print(1),print(2))
```


