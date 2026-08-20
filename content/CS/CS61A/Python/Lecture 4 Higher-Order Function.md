## 4.1高阶函数

断言语句


```python
assert 3>2,'Math is broken'
#assert 3<2,'That is false'
```

返回函数的函数


```python
%%script python
def make_adder(n):
    def adder(k):
        return k+n
    return adder
three_adder = make_adder(3)
print(three_adder(5))
print(make_adder(4)(5))
```

函数是first-class:函数可以被当做参数传递与返回

高阶函数就是做这些事情的函数:体现了泛用性（抽象）

## 4.2高阶函数的环境

环境依旧可以解释高阶函数


```python
def apply_twice(f,x):
    return f(f(x))#在f1中,f指向的是square,这两者建立绑定
def square(x):
    return x*x
def triple(x):
    return 3*x
print(apply_twice(square,3))
```

    81
    

## 4.3嵌套定义的环境


```python
def make_adder(n):
    def adder(k):
        return k + n
    return adder
add_three = make_adder(3)
result = add_three(5)
```

<font size=3>
5->创建一个frame,并且将n绑定到3,接下来定义adder函数,将adder绑定到绑定到make_adder的frame下的adder函数体中

接下来return到Global Frame中,把返回的函数adder给了add_three
</font>

<font size=3>用5来调用add_three,创建了frame:f2(f1子框架),顺着找,在f2中找到了k=5,在f1中找到了n=3</font>

## 4.5函数组合


```python
def compose1(f,g):
    def h(x):
        return f(g(x))
    return h
squiple=compose1(square,triple)
print(squiple(5))

```

    225
    


```python

```
