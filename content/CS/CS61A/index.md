# CS61A 课程索引

来源范围：综合读取 `Python/`、`Scheme/`、`SQL/` 下的 Markdown 笔记。标记为“需要人工补充”的内容表示现有笔记信息不足或示例未完整展开。

## 课程主线

CS61A 的主线可以从“计算如何被解释”展开：先用 Python 建立表达式、赋值、函数调用、帧和环境模型，再用高阶函数、闭包、递归和数据抽象组织复杂程序，随后进入可变对象、迭代器、生成器、OOP 和效率分析。相关起点是 [[Python/Lecture 2 Function|函数定义]]、[[Python/Lecture 3 Control|控制与环境]]、[[Python/Lecture 4 Higher-Order Function|高阶函数]]、[[Python/Lecture 5 Lambda Expressions|Lambda 与装饰器]]、[[Python/Lecture 6 Recursive Function|递归函数]]。

数据线从 Python 的列表、字典、字符串开始，逐步过渡到构造器/选择器、抽象屏障、树、链表和类表示。核心笔记包括 [[Python/Lecture 7 List|列表与容器]]、[[Python/Lecture 8 Data Abstraction|数据抽象]]、[[Python/Lecture 9 Tree|树]]、[[Python/nL2 链表|链表与树类]]、[[Python/nL6 树结构|树结构]]。

工程组织线包括可变性、对象交互、迭代抽象、异常、模块化和效率。相关笔记是 [[Python/Lecture10 Object字符串Mutation|对象、字符串与可变性]]、[[Python/Lecture11 可变性|可变性]]、[[Python/Lecture12 迭代器|迭代器与生成器]]、[[Python/Lecture13 OOP|OOP]]、[[Python/nL1 String表示|字符串表示与特殊方法]]、[[Python/nL3 效率|效率]]、[[Python/nL4 模块化设计|模块化设计]]、[[Python/nL5 异常|异常]]。

Scheme 模块把“程序如何被解释”显式化：表达式、特殊形式、列表、quote、Eval/Apply、环境、作用域、程序即数据、代码生成和宏。主要对应 [[Scheme/Lec1 Scheme|Scheme 表达式与特殊形式]]、[[Scheme/Lec2 Lists|Scheme 列表与符号编程]]、[[Scheme/Lec3 Languages|语言与解释器]]、[[Scheme/Lec4 Program is Data|程序即数据]]、[[Scheme/Lec5 宏|宏]]。

SQL 模块目前聚焦关系数据库基础：用表格记录数据，用声明式查询描述结果，涉及 `SELECT`、`FROM`、`LIMIT`、`CREATE TABLE AS`、`WHERE`、`ORDER BY` 和列算术。对应 [[SQL/数据库|数据库]]。

## 核心概念列表

- 名称、绑定、帧、环境、局部帧、全局帧、父帧查找：[[Python/Lecture 2 Function|函数定义]]、[[Python/Lecture 3 Control|控制与环境]]
- 纯函数、非纯函数、`None`、`print` 的副作用：[[Python/Lecture 2 Function|print and None]]
- 条件语句、真值/假值、`and`/`or` 短路、函数调用前参数求值：[[Python/Lecture 3 Control|条件与控制表达式]]
- 一等函数、高阶函数、闭包、函数组合、断言：[[Python/Lecture 4 Higher-Order Function|高阶函数]]
- `lambda`、柯理化、返回函数、`return` 终止、traceback、装饰器：[[Python/Lecture 5 Lambda Expressions|Lambda 与装饰器]]
- 递归、互递归、递归调用顺序、树形递归、分拆数：[[Python/Lecture 6 Recursive Function|递归函数]]
- 列表、容器、`for`、`range`、列表推导式、切片、字符串、字典：[[Python/Lecture 7 List|列表与容器]]
- 构造器、选择器、抽象屏障、有理数表示：[[Python/Lecture 8 Data Abstraction|数据抽象]]
- 树的 `label + branches` 表示、叶子计数、路径计数、`fib_tree`：[[Python/Lecture 9 Tree|树]]
- `str`、`repr`、`eval(repr(x))`、多态函数、特殊方法名：[[Python/nL1 String表示|字符串表示]]
- `Link` 链表、`Tree` 类、对象引用、链表游标、树的可变剪枝：[[Python/nL2 链表|链表与树类]]
- 可变操作、对象 identity、`is` 与 `==`、可变默认参数、闭包状态：[[Python/Lecture10 Object字符串Mutation|可变对象]]、[[Python/Lecture11 可变性|可变函数]]
- 迭代器、`iter`、`next`、迭代器耗尽、`map/filter/zip/reversed`、`yield`、`yield from`、惰性生成：[[Python/Lecture12 迭代器|迭代器与生成器]]
- 类、实例、方法、`self`、属性查找、类属性、绑定方法、继承、组合、多继承：[[Python/Lecture13 OOP|OOP]]
- 调用计数装饰器、记忆化、纯函数缓存、增长阶、空间与活动环境：[[Python/nL3 效率|效率]]
- 异常类型、`raise`、`try/except`、`reduce` 示例：[[Python/nL5 异常|异常]]
- Scheme 前缀表达式、特殊形式、`define`、`lambda`、`cond`、`begin`、`let`：[[Scheme/Lec1 Scheme|Scheme]]
- Scheme list、`cons/car/cdr/null?`、quote、符号编程、`append/map/filter/apply`：[[Scheme/Lec2 Lists|Lists]]
- Eval/Apply、特殊形式处理、`LambdaProcedure`、词法作用域与动态作用域：[[Scheme/Lec3 Languages|语言与解释器]]
- `eval`、程序即数据、quote/quasiquote/unquote、代码生成：[[Scheme/Lec4 Program is Data|程序即数据]]
- Racket 宏、`define-syntax`、`syntax-rules`、普通过程与宏的求值差异：[[Scheme/Lec5 宏|宏]]
- SQL 表、声明式查询、投影、条件筛选、排序、列算术：[[SQL/数据库|数据库]]

## 重要公式/代码实现

### Python 执行与抽象

闭包与返回函数：

```python
def make_adder(n):
    def adder(k):
        return k + n
    return adder
```

函数组合与柯理化：

```python
def compose1(f, g):
    def h(x):
        return f(g(x))
    return h

curry = lambda f: lambda x: lambda y: f(x, y)
```

递归分拆数公式：

```text
count_partitions(n, m) = count_partitions(n, m - 1) + count_partitions(n - m, m)
```

幂运算的线性递归与快速递归：

$$
b^n =
\begin{cases}
1, & n = 0\\
b \cdot b^{n-1}, & \text{otherwise}
\end{cases}
$$

$$
b^n =
\begin{cases}
1, & n = 0\\
\left(b^{\frac{1}{2}n}\right)^2, & n \text{ is even}\\
b \cdot b^{n-1}, & n \text{ is odd}
\end{cases}
$$

记忆化只适合笔记中定义的纯函数场景：

```python
def memo(f):
    cache = {}
    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memoized
```

有理数抽象使用构造器和选择器隔离表示：

```python
def rational(n, d):
    def select(name):
        if name == 'n':
            return n
        if name == 'd':
            return d
    return select

def numer(x):
    return x('n')

def denom(y):
    return y('d')
```

树抽象的列表表示：

```python
def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch), '分支必须是树'
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]
```

链表与树类的核心接口：

```python
class Link:
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest
```

```python
class Tree:
    def __init__(self, label, branches=[]):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)
```

当递归参数信息不足时，用内部 helper 保存额外信息：

```python
def bigs(t):
    def f(a, x):
        if a.label > x:
            return 1 + sum([f(b, a.label) for b in a.branches])
        else:
            return sum([f(b, x) for b in a.branches])
    return f(t, t.label - 1)
```

生成器版本分拆数体现惰性：

```python
def partitions(n, m):
    if n > 0 and m > 0:
        if n == m:
            yield str(m)
        for p in partitions(n-m, m):
            yield p + '+' + str(m)
        yield from partitions(n, m-1)
```

### Scheme 解释与元编程

Eval/Apply 的分工：

```text
Eval:
  Primitive values
  Look up values bound to symbols
  Eval(operator, operands) of call expr
  Apply(procedure, arguments)
  Eval(sub-expr) of special forms

Apply:
  Built-in primitive procedures
  Eval(body) of user-defined procedures
```

Scheme 函数对象保存参数、函数体和定义时环境：

```python
class LambdaProcedure:
    def __init__(self, formals, body, env):
        self.formals = formals
        self.body = body
        self.env = env
```

程序生成表达式，再交给 `eval`：

```scheme
(define (fact-expr n)
  (if (= n 0)
      1
      (list '* n (fact-expr (- n 1)))))
```

quasiquote 与 unquote 生成可参数化代码：

```scheme
(define (make-add-procedure n) `(lambda (d) (+ d ,n)))
```

宏在源代码执行前展开，能保留普通过程拿不到的原表达式：

```racket
(define-syntax twice
  (syntax-rules ()
    ((_ expr)
     (begin expr expr))))
```

### SQL 基础查询

```sql
SELECT expr AS name, expr AS name FROM table LIMIT num;
CREATE TABLE name AS [SELECT-statement];
SELECT [columns] FROM [table] WHERE [condition] ORDER BY [order];
SELECT chair, single + 2 * couple AS total FROM lift;
```

## 容易混淆点

- 赋值是一次性绑定；重新绑定 `a` 不会自动更新已经算出的 `b`，但函数体在调用时会重新按环境查找名字。
- 名称查找从当前帧开始，找到最近绑定就停止；形参可以遮蔽外层同名函数或变量。
- 函数调用会先求值所有参数；`if`、`and`、`or` 会根据条件跳过部分表达式。
- `print` 显示内容但返回 `None`，所以嵌套 `print(print(1), print(2))` 会出现显示结果和返回值混在一起的现象。
- `lambda` 只能是单表达式；`def` 定义的函数和赋给变量的 `lambda` 在显示名称上不同。
- `return` 是函数终结点；递归调用返回后，外层调用仍会继续执行剩余语句。
- `range` 是序列但不是列表；`list(range(...))` 才得到实际列表。
- 切片会生成新列表；可变列表的原地操作会影响所有指向同一对象的名字。
- `==` 比较值，`is` 比较是否为同一对象；可变默认参数不会每次调用重新生成。
- tuple 本身不可变，但 tuple 内部可以包含可变对象；可作为字典键还取决于其内容是否可哈希。
- 迭代器保存当前位置；`list(t)` 会把迭代器剩余部分耗尽，`for` 也会推进同一个迭代器。
- 通过实例查找方法得到绑定方法；通过类查找方法得到普通函数。
- 给实例赋值同名属性会遮蔽类属性，不会修改所有实例共享的类属性。
- 继承是 is-a 关系；组合是 has-a 关系，例如银行拥有账户列表。
- `Link(0)` 被 `r` 和 `s` 同时指向时，修改 `s.rest` 会改变同一个对象；`s = s.rest` 只是移动游标。
- Scheme 的 quote 得到的是表达式本身，不是字符串；`(list '+ 1 2)` 与 `(list + 1 2)` 的区别在于是否对 `+` 求值。
- Scheme 词法作用域中，过程的父环境来自定义时环境；动态作用域中，父环境来自调用时环境。
- 宏不同于普通过程：普通过程会先对参数求值，宏可以在求值前改写表达式。
- SQL 是声明式查询：描述要得到的结果列和筛选条件，而不是逐步写出计算过程。

## 推荐复习顺序

1. 先复习 Python 执行模型：[[Python/Lecture 2 Function|函数定义]]、[[Python/Lecture 3 Control|控制与环境]]。重点画出名称查找、帧、`None`、短路和函数调用求值顺序。
2. 接着复习函数抽象：[[Python/Lecture 4 Higher-Order Function|高阶函数]]、[[Python/Lecture 5 Lambda Expressions|Lambda 与装饰器]]。重点掌握闭包、函数组合、柯理化和装饰器。
3. 再复习递归模式：[[Python/Lecture 6 Recursive Function|递归函数]]。重点是 base case、递归调用顺序、互递归、树形递归和分拆数。
4. 然后复习数据组织：[[Python/Lecture 7 List|列表与容器]]、[[Python/Lecture 8 Data Abstraction|数据抽象]]、[[Python/Lecture 9 Tree|树]]。重点把“表示”和“操作”用抽象屏障隔开。
5. 继续复习对象化数据结构：[[Python/nL2 链表|链表与树类]]、[[Python/nL6 树结构|树结构]]、[[Python/nL1 String表示|字符串表示与特殊方法]]。重点是对象引用、`repr/str`、特殊方法和 helper 递归。
6. 再复习状态与程序组织：[[Python/Lecture10 Object字符串Mutation|对象与可变性]]、[[Python/Lecture11 可变性|可变性]]、[[Python/Lecture12 迭代器|迭代器与生成器]]、[[Python/Lecture13 OOP|OOP]]。重点区分 identity、mutation、iterator exhaustion、bound method、继承和组合。
7. 最后复习工程与性能：[[Python/nL3 效率|效率]]、[[Python/nL4 模块化设计|模块化设计]]、[[Python/nL5 异常|异常]]。重点是 memoization、增长阶、空间中的 active environments、`try/except`。
8. Scheme 建议放在 Python 环境模型之后复习：[[Scheme/Lec1 Scheme|表达式与特殊形式]]、[[Scheme/Lec2 Lists|列表与符号编程]]、[[Scheme/Lec3 Languages|解释器与作用域]]、[[Scheme/Lec4 Program is Data|程序即数据]]、[[Scheme/Lec5 宏|宏]]。重点对照 Python 的环境、闭包和递归。
9. SQL 放在最后单独复习：[[SQL/数据库|数据库]]。重点记住表、列、投影、筛选、排序、建表和列算术的基本语法。

## 需要人工补充

- [[Python/nL4 模块化设计|模块化设计]] 中“餐厅搜索”部分只有省略号，缺少可综合的实现或概念说明，需要人工补充。
- [[Python/Lecture 8 Data Abstraction|数据抽象]] 中有理数运算示例没有成功运行，且实现细节需要人工核对后再作为复习模板。
- [[Python/Lecture10 Object字符串Mutation|对象、字符串与可变性]] 末尾的 identity 示例内容不足，需要人工补充。
- [[Scheme/Lec1 Scheme|Scheme]] 中“谢尔宾斯基三角形”说明因解释器不一致无法展示，需要人工补充。
- [[Scheme/Lec5 宏|宏]] 中 “Trace” 只有图片和空代码块，需要人工补充。
- [[SQL/数据库|数据库]] 目前只覆盖 SQL 基础查询、建表、筛选、排序和算术；更复杂数据库主题若属于课程要求，需要人工补充。
