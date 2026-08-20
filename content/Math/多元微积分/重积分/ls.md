# 基础
**确定积分范围**的步骤：
在xOy平面内取任意点，然后画一条线戳上去，算出z的范围，然后再在区域在xOy上的投影取任意x，算y范围

**换元公式**（非常重要）：
设 $f ( x, y )$ 在闭区域 $D$ 上连续，映射 $T : ( u, v ) \to ( x ( u, v ), y ( u, v ) )$ 是 $D ^ { \prime } \to D$的双射，这里 $x ( u, v ), y ( u, v )$都具有一阶连续偏导数，并且在 $D ^ { \prime }$ 上雅可比行列式 $J = \frac { \partial \left( x, y \right) } { \partial \left( u, v \right) } = \left| \begin{array} { c c } { x _ { u } } & { x _ { v } } \\ { y _ { u } } & { y _ { v } } \\ \end{array} \right| \neq 0$ ，则有
$$
\iint _ { D } f \left( x, y \right) d x d y = \iint _ { D ^ { \prime } } f \left( x \left( u, v \right), y \left( u, v \right) \right) \left| \frac { \partial \left( x, y \right) } { \partial \left( u, v \right) } \right| d u d v
$$
1. 换元 $x = r \cos \theta, y = r \sin \theta$ 的雅可比行列式为 $J = r$
2. 换元 $x = r \sin \varphi \cos \theta, y = r \sin \varphi \sin \theta, z = r \cos \varphi$ 的雅可比行列式为 $J = r ^ { 2 } \sin \varphi$
3. 如果区域是单位圆（球）内部，则范围分别是 $r \in \left[ 0, 1 \right], \theta \in \left[ 0, 2 \pi \right] ; r \in \left[ 0, 1 \right], \varphi \in \left[ 0, \pi \right], \theta \in \left[ 0, 2 \pi \right]$
4. 如果换元是正交变换，则雅可比行列式为 ±1（适用于任何n重积分)
一般的有 $\frac { \partial \left( x, y \right) } { \partial \left( u, v \right) } \cdot \frac { \partial \left( u, v \right) } { \partial \left( x, y \right) } = 1 \Leftrightarrow \left| \begin{array} { c c } { { x _ { u } } } & { { x _ { v } } } \\ { { y _ { u } } } & { { y _ { v } } } \end{array} \right| \cdot \left| \begin{array} { c c } { { u _ { x } } } & { { u _ { y } } } \\ { { v _ { x } } } & { { v _ { y } } } \end{array} \right| = 1,$ ，从而可选一个好算的操作（用于反解——有的时候另一个行列式不好算） ^be53a1
# 重积分计算
## 对称性
定积分换元只换字母不影响结果
![[Pasted image 20260518193933.png]]
**切记切记，对z变量积分，可以把其他的变量视为常数**
### T1
$$
\int _ { - { 1 } {} } ^ { 1 } \iint _ { x ^ { 2 } + y ^ { 2 } \leqslant 1 - z ^ { 2 } } \frac { \left( \sin x + \cos y - \sqrt { 3 } z \right) ^ { 2 } } { \left( x ^ { 2 } + y ^ { 2 } + z ^ { 2 } \right) ^ { 2 } + 1 } d x d y d z
$$
展开以后，对于交叉项，我们可以通过选择先对哪个变量积分（对称性），从而使得交叉项为0
进而得到
$$
 \iiint _ {x^2+y^2+z^2\le1 } { \frac { \sin ^ { 2 } \! x + \cos ^ { 2 } \! y + 3 z ^ { 2 } } { \left( x ^ { 2 } + y ^ { 2 } + z ^ { 2 } \right) ^ { 2 } + 1 } } d x d y d z
$$
注意x->y, y->x的换元的雅可比行列式是1，利用轮换对称性，继续化简
时刻注意**积分区域的对称性**以及被积函数的对称性，当你发现了积分区域的对称性以后，一定要非常注意被积函数的对称性！（对称反对称......）
此外，**两个变量轮换的雅可比行列式是1**
## 换序与积分区域
### T1
1.设区域 $D$ 为 $x ^ { 2 } + y ^ { 2 } \leq 1, x + y \geq 1$ ，计算
$$
\iint _ { D } \frac { 1 } { x y \left( \operatorname { l n } ^ { 2 } x + \operatorname { l n } ^ { 2 } y \right) } d x d y
$$
2.设区域 $D$ 是曲线 $e ^ { - 2 x } + e ^ { - 2 y } = 1, e ^ { - x } + e ^ { - y } = 1$ 之间的区域，计算 $$\iint _ { D } { \frac { x ^ { 2 } - y ^ { 2 } + 1 } { x ^ { 2 } + y ^ { 2 } } } d x d y$$
1.难度在一元积分
2.注意到曲线区域是轮换对称的，而被积函数中$\frac{x^2-y^2}{x^2+y^2}$是斜对称函数，从而大大简化积分
### T2
设区域 $D$ 由 $y = { \sqrt { x } }, x = { \sqrt { y } }, x ^ { 2 } + y ^ { 2 } = x + y - { \frac { 1 } { 4 } }, x, y \in \left[ 0, { \frac { 1 } { 2 } } \right]$ 构成，计算
$$
\iint _ { D } \left( x - y ^ { 2 } \right) \left( y - x ^ { 2 } \right) \left( 1 - 4 x y \right) d x d y
$$
注意到一个显然的换元$u=x-y^2,v=y-x^2$
这里既可以通过对等式两边求偏导得出，也可以使用[[多元微积分/重积分/ls#^be53a1|雅可比行列式性质]]
### T3
设 $D = \left\{ ( x, y ) \left| 2 \leqslant \frac { x } { x ^ { 2 } + y ^ { 2 } }, \frac { y } { x ^ { 2 } + y ^ { 2 } } \leqslant 4 \right. \right\}$ 计算 $$\iint _ { D } \frac { 1 } { x y } d x d y$$看起来可以用极坐标来做，但是最后要讨论$\theta$范围，进而确定$r$，这会很麻烦
积分区域简单和被积函数简单之间虽然有一个trade-off，但是先把一个变简单总不会是一个坏的尝试
## 常见基本算法
### T1
设 $D = \left\{ ( x, y ) \left| 1 \leq x ^ { 2 } + y ^ { 2 } \leq 4, x \geq 0, y \geq 0 \right. \right\}$ ，求 $f ( x, y )$ ，在 $D$ 上连续且满足
$$
f \left( x, y \right) = \sin \left( \pi \sqrt { x ^ { 2 } + y ^ { 2 } } \right) - { \frac { 1 } { \pi } } \iint _ { D } { \frac { s f \left( s, t \right) } { s + t } } d s d t
$$
这里我们要注意到二重积分是一个常数，然后我们根据$f(x,y)$和积分区域的对称性解决
### T2
更强的对称性——旋转任意角度都可以
$$I = \iint _ { x ^ { 2 } + y ^ { 2 } \leqslant 1 } \left| \frac { x + y } { \sqrt { 2 } } - x ^ { 2 } - y ^ { 2 } \right| d x d y$$
换为极坐标以后，$\frac{x+y}{\sqrt{2}}=\sin(\theta+\frac{\pi}{4})$，由于圆的旋转对称性（旋转不变性），这里直接换$\theta+\frac{\pi}{4}$为$\theta$不改变积分
画图，可以看正面积和负面积
### T3
设 $D$ 是单位正方形， $f ( x, y )$ 有二阶连续偏导且 $f \left( x, 1 \right) = f \left( 1, y \right) = 0, \iint _ { D } f \left( x, y \right) d x d y = A$ ，计算 ^8e9e5a
$$
\iint _ { D } x y f _ { x y } \left( x, y \right) d x d y
$$
分部积分
### T4
$$\int _ { 0 } ^ { \infty } \int _ { x } ^ { \infty } e ^ { - ( x - y ) ^ { 2 } } { \sin ^ { 2 } } \left( x ^ { 2 } + y ^ { 2 } \right) \frac { x ^ { 2 } - y ^ { 2 } } { \left( x ^ { 2 } + y ^ { 2 } \right) ^ { 2 } } d y d x.$$
这种区域不复杂、很多平方项，优先尝试极坐标换元
## 几何应用
### T1
设椭球 ${ \frac { x ^ { 2 } } { 2 } } + { \frac { y ^ { 2 } } { 3 } } + { \frac { z ^ { 2 } } { 4 } } \leqslant 1$ 被平面 $x + y + z = 1$ 切成两部分，计算各自的体积.
先仿射变换（重积分换元），将椭球变为球，再利用球的[[多元微积分/重积分/ls#^8e9e5a|旋转对称性]]，把原本斜着的球冠变正（旋转保持距离不变）
### T2
将曲线 $L : \left\{ \begin{array} { c } { x ^ { 2 } + z ^ { 2 } = 2 x } \\ { y = \sqrt { x ^ { 2 } + z ^ { 2 } } } \\ \end{array} \right.$ 绕 $z$ 轴旋转一圈，得到一个曲面，其内部记为区域 $\Omega$ ，计算
$$
\iiint _ { \Omega } { \sqrt { x ^ { 2 } + y ^ { 2 } + z ^ { 2 } } } d x d y d z
$$
我们先要得到一个图——这里需要通过投影辅助判断。大致判断完曲面是什么样的，我们尝试求出曲面方程：
方法是，假设曲面上任意一点$(x,y,z)$，由在曲线$L$上的一点$(x_0,y_0,z_0)$旋转而来，求解方程进而得到曲面方程
## 证明题
### 泊松积分
$$
\begin{aligned} { \iiint _ { x ^ { 2 } + y ^ { 2 } + z ^ { 2 } \leqslant 1 } f \left( a x + b y + c z \right) d x d y d z = \pi \int _ { - 1 } ^ { 1 } \left( 1 - x ^ { 2 } \right) f \left( \sqrt { a ^ { 2 } + b ^ { 2 } + c ^ { 2 } } x \right) d x } \\ \end{aligned}
$$
$$
\iiint _ { x ^ { 2 } + y ^ { 2 } + z ^ { 2 } \leqslant 1 } f \left( a x + b y + c z \right) g \left( x ^ { 2 } + y ^ { 2 } + z ^ { 2 } \right) d V = \iiint _ { x ^ { 2 } + y ^ { 2 } + z ^ { 2 } \leqslant 1 } f \left( \sqrt { a ^ { 2 } + b ^ { 2 } + c ^ { 2 } } x \right) g \left( x ^ { 2 } + y ^ { 2 } + z ^ { 2 } \right) d V.
$$
最重要的**正交变换**（说白了就是换正交系）
$$
\left\{ \begin{array} { l } { x = a _ { 1 1 } u + a _ { 1 2 } v + a _ { 1 3 } w } \\ { y = a _ { 2 1 } u + a _ { 2 2 } v + a _ { 2 3 } w } \\ { z = a _ { 3 1 } u + a _ { 3 2 } v + a _ { 3 3 } w } \\ \end{array} \right. \Leftrightarrow A = ( a _ { i j } ) _ { 3 \times 3 }, A ^ { T } A = I, \left( \begin{array} { l } { x } \\ { y } \\ { z } \\ \end{array} \right) = A \left( \begin{array} { l } { u } \\ { v } \\ { w } \\ \end{array} \right)
$$
雅可比行列式是1，同时球在正交变换下也不变
写过程的时候，只需要写$u = \frac{ax+by+cz}{\sqrt{a^2+b^2+c^2}}$，$v,w$存在，然后直接使用泊松积分
### T1
设 $B = B ( 0, 1 )$ 是单位球，计算六重积分 $\iint _ { B \times B } \frac { 1 } { | x - y | } d x d y$ ，这里 $x, y \in B$是三维向量.
泊松积分的价值在于***正交变换***（线性组合可以直接变为其中一个变量，同时保证**任何**球不变）
 