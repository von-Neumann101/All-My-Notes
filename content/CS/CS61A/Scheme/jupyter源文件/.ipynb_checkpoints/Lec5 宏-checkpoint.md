# Macros

可以允许定义新的特殊形式

宏是在源代码执行前对其处理的一种操作，先执行宏语句然后产生新表达式，然后再对该表达式求值


```Racket
(define (twice expr)
  (list 'begin expr expr)
  )
```


```Racket
(twice (print 2)) ;普通定义过程，先对expr求值，然后代入计算
```

    2




<code>'(begin #&lt;void&gt; #&lt;void&gt;)</code>




```Racket
(define-syntax twice
  (syntax-rules ()
    ((_ expr)
     (begin expr expr)))
  )
```


```Racket
(twice (print 2))
```

    22


```Racket
(define-syntax check
  (syntax-rules ()
    ((_ expr)
     (if expr
         'passed
         (list 'failed: 'expr)
         )
     )
    )
  )
```


```Racket
(define x -2)
(check (> x 0))
```




<code>'(failed: (&gt; x 0))</code>



无论如何，常规过程无法得到表达式的原来内容

# for 宏


```Racket
(define-syntax for
  (syntax-rules ()
    ((_ var lst expr)
     (map (lambda (var) expr) lst)))
  )
```


```Racket
(for x '(2 3 4 5) (* x x))
```




<code>'(4 9 16 25)</code>



# Trace

![image.png](<Lec5 宏-checkpoint_files/fac3beff-3ff0-471f-8d5b-37dc8e4f4c03.png>)


```Racket

```

