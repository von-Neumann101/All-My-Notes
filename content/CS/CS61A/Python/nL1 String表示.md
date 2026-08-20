# 字符串表示

对象的行为与其所代表的数据类型相符

所有对象有两种字符串表示：`str`和`repr`<br>
前者是给人看的，后者是给Python解释器看的（也就是表达式）<br>
一般情况下两者都是一样的


```python
12e12
```




    12000000000000.0




```python
print(repr(12e12))
```

    12000000000000.0
    


```python
repr(min) #这里的结果是人类可读，因为实现min没有简单的的Python可读的字符串
```




    '<built-in function min>'



对于大部分对象类型`eval(repr(object)) == object`（`eval()`函数会把输入的字符串当做python语句运行）


```python
from fractions import Fraction
half = Fraction(1,2)
```


```python
repr(half) #注意这里输出的是字符串
```




    'Fraction(1, 2)'




```python
str(half)
```




    '1/2'




```python
print(half)
```

    1/2
    


```python
repr(half * half) #进一步体现了这是给python看的
```




    'Fraction(1, 4)'



看看一般的字符串：


```python
s = "Hello World"
```


```python
s
```




    'Hello World'




```python
str(s)
```




    'Hello World'



`repr()`返回的是给Python阅读的，所以有""


```python
r = repr(s)
print(r)
print(s)
```

    'Hello World'
    Hello World
    


```python
eval(r)
```




    'Hello World'




```python
eval(s) #这里就会出错，因为直接在Py中写Hello World显然报错
```

# F-Strings


```python
from math import pi
```


```python
'pi strats with ' + str(pi) + '...'
```




    'pi strats with 3.141592653589793...'



f-strings可以在大括号里直接执行表达式


```python
f'pi strats with {pi}...'
```




    'pi strats with 3.141592653589793...'



# 多态函数

我们知道`repr()`可以返回所有对象的字符串。实际上，python内置的`__repr__()`只有类属性可以调用


```python
half.__repr__()
```




    'Fraction(1, 2)'



之所以half能调用`__repr()__`函数，只是因为Fraction类知道怎么生成repr字符串。`str`一样


```python
def repr(x):
    return type(x).__repr__(x)#先向上转型
```

`str()`：实例属性调用其会被忽略，如果没有`__str__`属性，则返回repr字符串

对象通过查询其他对象的属性或方法来进行**信息传递**

接口就是一种标准，告诉别的类我有什么属性（例如：可迭代——能生成迭代器， 不可修改的——无法修改...）


```python
class Ratio:
    def __init__(self, n, d):
        self.numer = n
        self.denom = d
    def __repr__(self):
        return f'Ratio({self.numer}, {self.denom})'
    def __str__(self):
        return '{0}/{1}'.format(self.numer, self.denom)

    def __add__(self, other):
        def gcd(n ,d):
            while n != d:
                n, d = min(n, d), abs(n-d)
            return n
        if isinstance(other, int): #类型检查
            n = self.numer + self.denom * other
            d = self.denom
        elif isinstance(other, Ratio):
            n = self.numer * other.denom + self.denom * other.numer
            d = self.denom * other.denom
        g = gcd(n, d)
        return Ratio(n//g, d//g)
    __radd__ = __add__ #__radd__是右加法
```


```python
half = Ratio(1, 2)
```


```python
print(half)
```

    1/2
    


```python
repr(half)
```




    'Ratio(1, 2)'



# 特殊方法名

`__add__`双参数方法，用于两个对象相加<br>
`__bool__`用于把对象转换为bool值<br>
`__float__`把对象转为float类型


```python
zero, one, two = 0, 1, 2
one.__add__(two) #和 one + two等价
```




    3




```python
zero.__bool__(), one.__bool__()
```




    (False, True)




```python
Ratio(1,3) + Ratio(1,6)
```




    Ratio(1, 2)




```python
Ratio(1,3).__add__(Ratio(1, 6))
```




    Ratio(1, 2)




```python
Ratio(1, 2) + 1
```




    Ratio(3, 2)


