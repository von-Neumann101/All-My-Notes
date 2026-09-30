# Linear Transformation
二维的齐次坐标表示：
$$
\begin{pmatrix}
x\\ 
y\\
1
\end{pmatrix}
$$
齐次坐标下的点，第三个分量一定为$1$。也就是说，一个三元组可以表示一个二维的点：
$$
\begin{pmatrix}
x\\ 
y\\
w
\end{pmatrix}\Longrightarrow\begin{pmatrix}
x/w\\ 
y/w\\
1
\end{pmatrix},\ w\ne 0
$$
所以，向量的表示则是：
$$
\begin{pmatrix}
x\\ 
y\\
0
\end{pmatrix}
$$
齐次坐标的表示可以除去偏置项（机器学习）
$$
\begin{pmatrix}
x'\\
y'\\
1
\end{pmatrix}
=
\begin{pmatrix}
a & b & t_x\\
c & d & t_y\\
0 & 0 & 1
\end{pmatrix}
\begin{pmatrix}
x\\
y\\
1
\end{pmatrix}
$$

对于平移变换：
$$\mathbf{T}(t_x,t_y) = \begin{pmatrix} 1 & 0 & t_x\\ 0 & 1 & t_y\\ 0 & 0 & 1 \end{pmatrix}$$
对于线性变换：
$$\mathbf{A} = 
\begin{pmatrix} 
a & b & 0\\ 
c & d & 0\\ 
0 & 0 & 1 
\end{pmatrix}$$
对于仿射变换（线性+平移）：
$$\mathbf{A} = 
\begin{pmatrix} 
a & b & t_x\\ 
c & d & t_y\\ 
0 & 0 & 1 
\end{pmatrix}$$