# Exception


```python
raise TypeError("这是一个错误")
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Cell In[1], line 1
    ----> 1 raise TypeError("这是一个错误")
    

    TypeError: 这是一个错误


`TypeError, NameError, KeyError, RecursionError`

`try:`语句


```python
try: #try内必执行，如果出错则用expect捕获
    x = 1/0
except ZeroDivisionError as e:
    print('handling a', type(e))
    x = 0
```

    handling a <class 'ZeroDivisionError'>
    

# 示例：Reduce


```python
def divide_all(n, ds):
    try:
        return reduce(truediv, ds, n)
    except ZeroDivisionError:
        return float('inf')

def reduce(f, s, initial):
    """将s中每个元素和initial用f运算（叠加）
    >>> reduce(mul, [2, 4, 5], 2)
    80 # mul(5, (mul(4, mul(2, 2))))
    """
    for x in s:
        initial = f(initial, x)
    return initial
```


```python

```
