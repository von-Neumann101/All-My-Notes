# 程序即数据

Scheme表达式由表达式组成（基本表达式，组合表达式）

eval过程可以执行符号程序（类似于Py的eval执行字符串）


```scheme
(eval '(quotient 10 2))
```




    5




```scheme
(eval (list 'quotient 10 2))
```




    5



我们会发现一个惊人的事实：Scheme代码都是列表，而eval又可以执行所有的符号<br>
意味着我们可以做一个可以编程的程序？


```scheme
(list + 1 2) 
```




    (#<procedure> 1 2)



但这貌似不是需要的表达式，原因在于我们对`+`进行求值了

解决方法很简单——符号编程


```scheme
(list '+ 1 2)
```




    (+ 1 2)




```scheme
(define (fact n)
  (if (= n 0)
      1
      (* n (fact (- n 1)))
      )
  )
```


```scheme
(fact 5)
```




    120




```scheme
(define (fact-expr n)
  (if (= n 0)
      1
      (list '* n (fact-expr (- n 1)))
      )
  )
```


```scheme
(fact-expr 5) ;返回表达式
```




    (* 5 (* 4 (* 3 (* 2 (* 1 1)))))




```scheme
(define (fib n)
  (if (<= n 1)
      n
      (+ (fib(- n 2)) (fib(- n 1)))
      )
  )
```


```scheme
(define (fib-expr n)
  (if (<= n 1)
      n
      (list '+ (fib-expr(- n 2)) (fib-expr(- n 1)))
      )
  )
```


```scheme
(fib-expr 6)
```




    (+ (+ (+ 0 1) (+ 1 (+ 0 1))) (+ (+ 1 (+ 0 1)) (+ (+ 0 1) (+ 1 (+ 0 1)))))




```scheme
(eval (fib-expr 6))
```




    8



# 代码生成

Quasiquotation在大部分情况下和Quotation一样，但是在使用`,`时不同，前者将其直接应用于后面的表达式，直接求值：


```scheme
(define b 4)
```


```scheme
'(a ,(+ b 1))
```




    (a (unquote (+ b 1)))




```scheme
`(a ,(+ b 1))
```




    (a 5)




```scheme
(define (make-add-procedure n) `(lambda (d) (+ d ,n)))
```


```scheme
(make-add-procedure 2) ;有点像python的柯理化那块
```




    (lambda (d) (+ d 2))



## 示例：While语句

```python
x = 2
total = 0
while x < 10:
    total = total + x * x
    x = x + 2
```


```scheme
(begin
    (define (f x total)
      (if (< x 10)
          (f (+ x 2) (+ total (* x x)))
          total
          )
      )
    (f 2 0))
```




    120



但是我们想随意修改传入的值，如何做呢？


```scheme
(define (sum-while initial-x condition add-to-total update-x)
  ;      sum-while     2     (< x 10)     (*x x)     (+ x 2)
`(begin
    (define (f x total)
      (if ,condition
          (f ,update-x (+ total ,add-to-total))
          total))
    (f ,initial-x 0))
   )
```


```scheme
(define gen-code (sum-while 2 '(< x 10) '(* x x) '(+ x 2)))
```


```scheme
(eval gen-code)
```




    120


