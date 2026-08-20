# Scheme

Scheme程序由表达式构成：
1. 基础表达式：2,3.3,true,+,quotient,...
2. 组合表达式：(quotient 10 2),(not true),...<br>
数字可以自己计算，但是符号必须绑定值

表达式以运算符开头，后面有多个操作数，都放在括号里


```scheme
(quotient 10 2) ;内置的整数除法过程（本质和函数一样）
```




    5




```scheme
(quotient (+ 8 7) 5)
```




    3




```scheme
(+ (* 3 (+ (* 2 4)
           (+ 3 5))) 
   (+ (- 10 7) 6)) ;不在意换行
```




    57




```scheme
(+ 1 2 3 4)
```




    10




```scheme
(+)
```




    0




```scheme
(*)
```




    1




```scheme
(number? 3) ;是否为数字？
```




    True




```scheme
(zero? 2) ;是否是0
```




    False




```scheme
;(integer? 2)
;无法运行，但是不重要
```

# Scheme解释器

Proj4你会遇到利用Python编写scheme解释器

# 特殊形式

1. if语句：`if <predicate> <consequent> <alternative>`根据p的真假决定执行c还是a<br>
2. and 和 or：`(and <e1> <e2> ...)`
3. define语句：`(define <symbol> <expression>)`把值绑定到符号上
4. 函数：`(define (<symbol> <formal parameters>) <body>)`


```scheme
(if (and (< 1 0) (> 2 3))
        (+ 1 2) 
        (- 1 2)
    )
```




    -1




```scheme
(define pi 3.14)
(* pi 2)
```




    6.28




```scheme
(define (abs x)
  (if (< x 0)
      (- x)
      x
      )
  )
```


```scheme
(abs -3)
```




    3




```scheme
(define (square x)
  (* x x)
  )
```


```scheme
(define (average x y)
  (/ (+ x y) 2)
  )
```


```scheme
(average (square 3) (square 5))
```




    17




```scheme
(define (sqrt x)
  (define (update guess)
    (if (= (square guess) x)
        guess
        (update (average guess (/ x guess)))
        )
    )
  (update 1)
  )
;由于解释器不同，这个函数只是一个花瓶而已
```

# Lambda表达式

`(lambda (<formal-parameters>) <body>)`


```scheme
(define plus4 (lambda (x) (+ x 4)))
```

直接用组合表达式：


```scheme
(
 (lambda (x y z) (+ x y (square z)))
 1 2 3
 )
```




    12



# 其他特殊形式

cond语句类似elif


```scheme
(define x 123)
(
 cond ((> x 10) (print 'big))
      ((> x 5) (print 'medium))
      (else (print 'small))
 )
```

    big
    


```scheme
(print(
 cond ((> x 10) 'big)
      ((> x 5) 'medium)
      (else 'small)
 ))
```

    big
    

begin用于合并多个表达式，并返回最后一个子表达式的值。这解决了if与cond语句只能放一个expression的缺点


```scheme
(
 cond ((> x 10) (begin (print 'big)
                       (print 'guy)))
      (else (begin (print 'small)
                   (print 'fry)))
)
```

    big
    guy
    

let用于**临时**绑定变量和值
```lisp
(let((<var1> <expr1>) (<var2> <expr2>) ...)
    expr)
```
总结就是`(let((临时绑定))主要表达式)`<br>
需要注意的是，let除了expr以外的语句结束才算绑定完成


```scheme
(define c 
  (let ((a 3) (b (+ 2 2)))
  (* a b))
  )
```


```scheme
c
```




    12




```scheme
a ;错误
```

# 示例：谢尔宾斯基三角形

解释器不一致，无法展示
