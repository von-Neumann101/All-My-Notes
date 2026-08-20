# Java Class
## 对象创建
`<Class> <name> = new <Class>()`左边代表放置对象（告诉编译器这是放置`<Class>`的地方），右边则是**创建**一个对象
和Python类似：`__init__`相当于构造器，用点取的方法访问属性以及方法
## 静态对象
Static可以理解为”永恒的，不变的“
静态方法绑定到类
调用静态方法用类调用，而非静态方法必须要对象调用
例：Math类
不需要创建实例：
```java
Math m = new Math();
x = m.round(x);
```
`x = Math.round(x)`就可以了
技术上说可以使用对象调用静态方法，但是工程上不推荐
不要改变静态变量！
# 语法
## List
Java中有许多的List
![[Pasted image 20260316194337.png|416]]
如图，如果你没有指定List里的元素类型，那么他可以像Py中增加任何类型元素，但是这也会导致你用List中的元素直接给一个对象赋值（没有保证)
![[Pasted image 20260316194542.png|418]]
使用“钻石语法”，接受限制，不要成为伊卡洛斯
## Array
必须在创建时申明长度，且不可变，其也没有任何方法
![[Pasted image 20260316194859.png|456]]
## Maps
Python的字典
Java的Map需要指定键和值的类型
有TreeMap和HashMap
![[Pasted image 20260316195311.png|454]]
#对象 #数组 #字典 #列表 #static #Java





















