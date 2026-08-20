### 9.1树

树的抽象结构:


```python
"""tree(3,[tree(1),
        tree(2,[tree(1),
                tree(1)])])"""
```

对于一个树而言,他是由标签+分支(树)组成


```python
def tree(label,branches=[]):#branches在开始是没有的
    for branch in branches:
        #抽象屏障
        assert is_tree(branch),'分支必须是树'
    return [label]+list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree)!=list or len(tree)<1:
        #树是有至少一个数的列表
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            #树的每个分支是树
            return False
    return True

def is_leaf(tree):
    return not branches(tree)
```


```python
#tree(1,[5])
tree(1,[[5]])
```




    [1, [5]]




```python
t=tree(3,[tree(1),
        tree(2,[tree(1),
                tree(1)])])
print(t)
```

    [3, [1], [2, [1], [1]]]
    


```python
print(label(t))
print(branches(t)[1])
```

    3
    [2, [1], [1]]
    

### 9.2树的处理

fib_tree


```python
def fib_tree(n):
    if n<=1:
        return tree(n)
    else:
        left,right=fib_tree(n-2),fib_tree(n-1)
        return tree(label(left)+label(right),[left,right])
```


```python
fib_tree(4)
```




    [3, [1, [0], [1]], [2, [1], [1, [0], [1]]]]




```python
label(fib_tree(4))
```




    3



叶子节点计数


```python
def count_leaves(t):
    if is_leaf(t):
        return 1
    else:
        #每个树的叶子结点树就是分支的叶子节点数之和
        branche_counts = [count_leaves(branch) for branch in branches(t)]
        return sum(branche_counts)
```




```python
def count_path(t, total):
  if total == label(t):
    found = 1
  else:
    found = 0
  return found + sum([count_path(branche, total - label(t)) for branche in branches(t)])
```
