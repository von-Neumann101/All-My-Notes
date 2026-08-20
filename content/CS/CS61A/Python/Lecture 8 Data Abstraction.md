### 8.1数据抽象 & 数据对

把多个对象组合起来,形成一个新对象(日期包含年月日).他将程序使用数据分为两个部分——数据的操作和数据的修改

e.g.有理数可以表示为分子除以分母,是一对整数,但是如果我们直接用$\frac{1}{3}$,那么他会变为一个浮点数(精度差距),这并非有理数$\frac{1}{3}$的表示方式

rational(n,d) returns a rational number x:构造函数,他接受分子和分母,返回一个"有理数"类型<br>
numer(x) returns the numerator of x 以及 denomer(x) return s the denominator of x:选择器,用来获得整个有理数的部分


```python
pair = [1,2]
x,y = pair #x=1 y=2 ->列表解包
from operator import getitem
getitem(pair,1)
```




    2




```python
def rational(n,d):#修改,这么做完全把列表分离了
    def select(name):#表示有理数
        if name=='n':
            return n
        if name=='d':
            return d
    return select
def numer(x):#获取分子
    return x('n')
def denom(y):#获取分母
    return y('d')
```

### 8.2抽象屏障

我们考虑使用有理数进行运算的程序,这里的"**有理数**"已经上升为了抽象的**数据**,而不是一个pairs,程序对他使用有理数加法(add_rational),有理数乘法(mul_rational)...(不需要在意实现,他们是**抽象**)

*在他们之间有一个抽象屏障,我们不能把上下两个函数混用

但是对于创建或者实现有理数运算的程序,"有理数"是一个由**分子分母构成的pairs**,程序就需要运行构造函数(rational),以及选择器(numer\denom)了

*再底层,这里还有一个抽象屏障

还有,对于实现构造函数和选择函数,他们将"有理数"视作两个元素的list,然后他们对这个list操作

其实和Java的封装,抽象完全一样,你在接口那里完完全全可以看到一样的逻辑——永远不要暴露底层的实现,保持程序的鲁棒性\独立性



### 7.3数据的表示

构造器函数和选择器函数共同工作以保证合适的行为(比如说他真正是一个有理数)
e.g.$\frac{numer(x)}{denom(x)}=\frac{n}{d}$<br>
**数据抽象就是用选择器和构造函数来定义行为**

类似于接口,只要有构造器和选择器,这些函数只要进行运算就行了


```python
def add_rational(x,y):
    nx,dx=numer(x),numer(y)
    ny,dy=numer(x),numer(y)
    return rational(nx*dy+ny*dx,dx*dy)
def mul_rational(x,y):
    return rational(numer(x)*numer(y),denom(x)*denom(y))
def ratioanl_are_equal(x,y):
    return numer(x)*denom(y) == numer(y)*denom(x)
def print_ratioanl(x):
    print(numer(x),'/',denom(x))
```


```python
x,y=rational(1,2),rational(3,4)
print_ratioanl(mul_rational(x,y))
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    /tmp/ipython-input-3662278535.py in <cell line: 0>()
    ----> 1 x,y=rational(1,2),rational(3,4)
          2 print_ratioanl(mul_rational(x,y))
    

    NameError: name 'rational' is not defined

