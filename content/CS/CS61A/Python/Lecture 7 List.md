### 7.1列表

列表中可以放表达式,而且列表里面可以放任何东西


```python
from operator import getitem
odds=[41,43,47,51,1,5,53,77,59]
print(odds)
print(odds[0]==getitem(odds,0))
print(len(odds))
print([1,3]+odds*2)#add和mul也可以
```

    [41, 43, 47, 51, 1, 5, 53, 77, 59]
    True
    9
    [1, 3, 41, 43, 47, 51, 1, 5, 53, 77, 59, 41, 43, 47, 51, 1, 5, 53, 77, 59]
    

注意list的index可以为负数


```python
print(odds[-1])
print(odds[-9])
```

    59
    41
    

### 7.2Containers

in检测某**个**元素是否在列表中


```python
print(41 in odds)
print(2 in odds)
```

    True
    False
    

### 7.3For


```python
def count(s,value):#统计某个值出现的次数
    total=0
    for element in s:
        if element == value:
            total+=1
    return total
print(count([1,23,42,1,1,1,2],1))
```

    4
    

for `<name>` in `<expression>`:<br>
其中expression必须返回一个可迭代的值(序列)


```python
pairs = [[1,2],[2,2],[3,2],[4,4]]
same_count=0
for x,y in pairs:#x和y分别对应pairs中的键值对中的元素(序列解包)
    if x==y:
        same_count +=1
print(same_count)
```

    2
    

### 7.4Range

Range属于序列但不是列表,主要表示按顺序递归的整数序列,range(a,b)代表在[a,b)中的递增整数序列


```python
print(list(range(-2,2)))
print(list(range(4)))
#range本身不是列表,但是调用list函数就能得到包含所有元素的列表
```

    [-2, -1, 0, 1]
    [0, 1, 2, 3]
    

重复执行语句,_可以是任何变量名


```python
for _ in range(3):
    print("awa")
```

    awa
    awa
    awa
    

### 7.5列表推导式


```python
letters=['z','r','y','e','f','q']
[letters[i] for i in[4,2,1]]#letters中index为4,2,1分别对应的元素
```




    ['f', 'y', 'r']




```python
print([x+1 for x in odds])#列表中的元素是x+1
print([x for x in odds if x>45])#列表中的元素是x(满足大于45)
```

    [42, 44, 48, 52, 2, 6, 54, 78, 60]
    [47, 51, 53, 77, 59]
    


```python
def divisors(n):#能整除数字n的所有整数
    return [1]+[x for x in range(2,n//2+1) if n%x==0]+[n]
print(divisors(24))
```

    [1, 2, 3, 4, 6, 8, 12, 24]
    

### 7.6切片


```python
print(odds[1:])#从索引1及以后的列表
```

    [43, 47, 51, 1, 5, 53, 77, 59]
    


```python
def sum_list(s):
    return 0 if len(s)==0 else sum_list(s[1:])+s[0]
sum_list([1,2,3,5])
```




    11




```python
def large(s,n):#s是正数列表,n是非负数,返回小于n的最大s子列和
    if s==[]:
        return []
    elif s[0]>n:
        return large(s[1:],n)
    else:
        first = s[0]
        with_s0 =[first]+large(s[1:],n-first)#选x0,边界缩短,把剩下的取最大
        without_s0=large(s[1:],n)#不选x0,边界不变,把剩下的取最大
        return with_s0 if sum_list(with_s0)>sum_list(without_s0) else without_s0
large([4,2,5,6,7],3)
```




    [2]



这里其实是动态规划

### 7.7盒子-指针标记法

盒子-指针标记法就是在环境图中用来表示列表的方法

一个组合数据值的方法要满足闭合属性,组合后的结果能用相同方法继续组合(也许是代数的封闭性?)我们把元素放入列表中,我们亦可把列表放到另外一个列表中

### 7.8切片(Slicing)


```python
print([odds[i] for i in range(1,3)])
print(odds[1:3])#1 2
print(odds[:3])#0 1 2
```

    [43, 47]
    [43, 47]
    [41, 43, 47]
    

### 7.8容器值的处理

sum(iterable[, start])返回和


```python
print(sum([2,3,4]))
print(sum([2,3,4],5))
#print(sum([2,3,4],[6])) #会报错,起始项不加东西,默认0
print(sum([[2,3,4],[4]],[]))
```

    9
    14
    [2, 3, 4, 4]
    

max(iterable/a,b,c,...[, key=func])


```python
print(max(range(5)))
```

    4
    

其中func会应用在每一个元素上,再根据函数返回值计算最大值


```python
max(range(10), key=lambda x:7-(x-4)*(x-2))
```




    3



all(iterable)返回bool类型,输入为空返回True,所有数据经过bool后都为真,则返回True

剩下的还有min函数和any函数,分别是max和all函数的反转

### 7.9字符串


```python
"mjq=lambda x:x+7"
exec("mjq=lambda x:x+7")
mjq(1)
```




    8




```python
name='ZEqwq'
print(len(name))
print(name[2])
print(type(name[2]))#字符串中的元素还是字符串
print(type(name))
```

    5
    q
    <class 'str'>
    <class 'str'>
    


```python
'here' in "Where's ZEq"
```




    True



### 7.10字典

储存键值对的对象,java中的Map


```python
numerals={'Z':4,'E':2,'Q':1}#'键1':'值1','键2':'值2'...
print(numerals['Z'])
#print(numerals[2]) #单向查找
```

    4
    


```python
print(list(numerals)) #输出键表
print(numerals.values()) #输出"字典值视图"
print(list(numerals.values()))
```

    ['Z', 'E', 'Q']
    dict_values([4, 2, 1])
    [4, 2, 1]
    


```python
{1:'first',1:'awa'}
```




    {1: 'awa'}



键不能是列表或者字典(不可哈希)


```python
#{[1]:'awa'}
```

字典表达式:if可以不需要,满足if中的表达式则添加该键值对


```python
#{<key exp>:<value exp> for <name> in <iter exp> if <filter exp>}
```


```python
{x*x:x for x in range(1,6) if x>2}
```




    {9: 3, 16: 4, 25: 5}




```python

```
