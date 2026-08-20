# 引用
![[Pasted image 20260318170857.png|375]]
输出5 2
![[Pasted image 20260318171651.png|376]]
输出5 5

最基本的知识点：在计算机中信息以0/1序列存储在内存中，每一个位置都是一个bit

`=`的作用是把bits完全复制
`y=x`就是把x的bits完全复制给y
对于Java的基本类型(byte, shot, int, long, float, double, boolean, char)，他们bits都是定长的，例如int就是32个bits，每个bit位上都填0或者1，表示一个int类型的数
除了这八个基本类型以外，都叫做**引用类型** ^342a3d

当我们实例化一个对象，Java为每个实例变量创建一个bits盒子，这个盒子里就放着实例的属性
![[Pasted image 20260318172019.png|190]]
 在创建对象时，new关键字做的是在内存中找到一个位置，创建实例，然后**返回实例的地址**(64 bits)
 ![[Pasted image 20260318182034.png|467]]
（这里绿色代表的就是weight，蓝色代表的就是tuskSize）
Java就是值传递语言（地址也是值）
由于地址（实例的位置）对人类来说是无意义的，所以我们通过箭头表示不全为0的地址（全为0的地址就是null）——“盒子-指针标记法”

![[Pasted image 20260318183512.png|487]]
所以对于这段代码，我们往doStuff传入walrus, x，这里形参walrus的地址就赋值给了W，x的值就赋值给了*x*，W.weight就相当于直接开盒了，找到了weight的地址，把他改了，但是由于x给的是值本身，所以*x*不知道这个9到底在哪，自然也没可能修改到x，*x*就这样迷失在0/1的海洋中了
# Arrays & == vs equal()
![[Pasted image 20260318184518.png|425]]
![[Pasted image 20260318184536.png|347]]
# int List
创建一个无限拓展的列表(CS61A)
![[Pasted image 20260318190018.png|450]]
![[Pasted image 20260318185952.png|487]]

获得长度：.rest有点类似于Cpp中的指针地址+1
![[Pasted image 20260318190524.png|333]]
#equals #基本类型 #引用类型 #Java #值传递





