# 对象

参考Java

# 字符串示例


```python
s = 'Hello'
```

这里的upper()就是方法，而不是所谓的函数


```python
s.upper()
```




    'HELLO'




```python
from unicodedata import name, lookup
```


```python
name("草")
```




    'CJK UNIFIED IDEOGRAPH-8349'




```python
lookup("WHITE SMILING FACE")
```




    '☺'



# 可变性

## 可变操作


```python
Dict = ['A', 'B', 'C', 'D', 'E']
original_Dict = Dict
```


```python
Dict.pop()#去掉最后一个元素
```




    'E'




```python
Dict.remove('A')
```


```python
Dict
```




    ['B', 'C', 'D']




```python
Dict.append('awa')
```


```python
Dict.extend(['qwq', 'QAQ'])
```


```python
Dict[4] = 'QwQ'
```

所有指向相同对象的名字都会受到改变的影响


```python
print(Dict)
print(original_Dict)
```

    ['B', 'C', 'D', 'awa', 'QwQ', 'QAQ']
    ['B', 'C', 'D', 'awa', 'QwQ', 'QAQ']
    


```python
Dict = {'I': 1, 'V': 5, 'X': 10}
```


```python
Dict['F'] = 4
```


```python
Dict
```




    {'I': 1, 'V': 5, 'X': 10, 'F': 4}



## Tuple


```python
(4, 2, 1)
```




    (4, 2, 1)




```python
4, 2, 1
```




    (4, 2, 1)




```python
tuple([4, 2, 1])
```




    (4, 2, 1)




```python
(1, 2) + (3, 4)
```




    (1, 2, 3, 4)



Tuple是不可变量，所以其可以作为键值对的键（但是包含列表的Tuple不可以）


```python
s = ([1, 2], 3)
s[0].append(421)
```


```python
s
```




    ([1, 2, 421], 3)



## 可变性


```python
1 is 1
```


```python

```
