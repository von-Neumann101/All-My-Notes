## 6.1递归函数


```python
def split(n):
    return n//10,n%10
def sum_all_digits(n):
    if n <10: #基准情况
        return n
    else: #递归
        rest,last=split(n)
        return sum_all_digits(rest)+last
print(sum_all_digits(123))
```

    6
    

## 6.2互递归

Lun校验:奇数位置的数字翻倍,超过9则算翻倍后的各位数字之和,偶数位置不变,将新的序列求和,结果mod10余0.


```python
def luhn_sum(n):#直接拆然后加
    if n<10:
        return n
    else:
        rest,last=split(n)
        return luhn_sum_double(rest)+last
def luhn_sum_double(n):#下一个拆出来的要翻倍
    rest,last=split(n)
    luhn_digit=sum_all_digits(2*last)
    if n<10:
        return luhn_digit
    else:
        return luhn_sum(rest)+luhn_digit
print(luhn_sum(312))
```

    7
    

## 6.3递归调用顺序

一个函数必须返回了value(包括None),这一串函数语句才能算结束


```python
def cascade(n):
    if n<10:
        print(n)
    else:
        print(n)
        cascade(n//10)
        print(n)
print(cascade(123))
```

    123
    12
    1
    12
    123
    None
    

a.123进入cascade,打印123,将123//10传入cascade(注意n没有改变).<br>
b.12进入cascade,打印12,将12//10传入cascade<br>
c.1进入cascade,1<10,打印1,cascade函数返回return None(没写就是return None)<br>
d.注意到我们上一次调用用的是谁吗?12,他还要接着运行(他已经经过了cascade(n//10)了),打印12,返回None.<br>
……

### Inverse cascade


```python
def inverse_cascade(n):
    grow(n)#加一位然后输出
    print(n)
    shrink(n)#输出然后减一位
def f_then_g(f,g,n):
    if n:
        f(n)
        g(n)
grow = lambda n: f_then_g(grow,print,n//10)#这是精髓
shrink = lambda n: f_then_g(print,shrink,n//10)
print(inverse_cascade(123))
```

    1
    12
    123
    12
    1
    None
    

对于shrink,这是自然的,因为shrink是一个信息量递减的的过程,后一项的信息量是前一项的子集<br>
但是对于grow来说,信息量是递增的,所以grow必须在每一次输出的时候都保留n//10(这里n//10是不变的,n等于123的时候,n//10=12)这个信息(也就是每次循环都必须保证grow可以以某些路径调用到n//10).<br>
所以对于grow,print必须在grow之后,这样由grow处理完一次给print

### 6.4树形递归


```python
def fib(n):
    return 0 if n==0 else 1 if n==1 else fib(n-2) + fib(n-1)
print(fib(8))
```

    21
    

树形:求fib(5)要fib(3)和fib(4),fib(3)要fib(1)和fib(2)……,fib(4)要fib(3)和fib(2)……

### 6.5Example:分拆数

count_partitions(n,m) => 将n表示为k个[1,m]之间非递减整数的和的分拆数量

考虑递归:cp(n,m)=cp(n,m-1)+cp(n-m,m)


```python
def count_partitions(n,m):
    if n==0:
        return 1
    elif n<0 or m==0:
        return 0
    else:
        return count_partitions(n,m-1)+count_partitions(n-m,m)
print(count_partitions(5,3))
```

    5
    
