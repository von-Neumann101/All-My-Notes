# 偏微分
$$\frac{\partial}{\partial x}\big(f(x)g(x)\big)

=

\frac{\partial f}{\partial x}g(x)

+

f(x)\frac{\partial g}{\partial x}$$
# 梯度：
$$\text{若记 } \mathbf{x}=(x_1,\ldots,x_n)^{\top},\ \text{则}\quad

\nabla f(\mathbf{x})

=

\begin{bmatrix}

\frac{\partial f}{\partial x_1}\\

\frac{\partial f}{\partial x_2}\\

\vdots\\

\frac{\partial f}{\partial x_n}

\end{bmatrix}$$
# 向量值函数：
$$
\mathbf{f}:\mathbb{R}^n \rightarrow \mathbb{R}^m
$$

$$
\mathbf{x}=
\begin{bmatrix}
x_1\\
x_2\\
\vdots\\
x_n
\end{bmatrix}
$$

$$
y_i = f_i(\mathbf{x}) = f_i(x_1,x_2,\dots,x_n)
$$
函数值向量
$$
\mathbf{y}=
\begin{bmatrix}
y_1\\
y_2\\
\vdots\\
y_m
\end{bmatrix}
=
\begin{bmatrix}
f_1(\mathbf{x})\\
f_2(\mathbf{x})\\
\vdots\\
f_m(\mathbf{x})
\end{bmatrix}
=
\mathbf{f}(\mathbf{x})
$$
# Jacobian Matrix：
$$J=\nabla_{\mathbf{x}}\mathbf{f}=\frac{\mathrm{d} \mathbf{f}(\mathbf{x})}{\mathrm{d} \mathbf{x}}

=

\begin{bmatrix}

\nabla f_1(\mathbf{x})\\

\nabla f_2(\mathbf{x})\\

\vdots\\

\nabla f_m(\mathbf{x})

\end{bmatrix}

=

\begin{bmatrix}

\frac{\partial}{\partial \mathbf{x}}f_1(\mathbf{x})\\

\frac{\partial}{\partial \mathbf{x}}f_2(\mathbf{x})\\

\vdots\\

\frac{\partial}{\partial \mathbf{x}}f_m(\mathbf{x})

\end{bmatrix}

=

\begin{bmatrix}

\frac{\partial}{\partial x_1}f_1(\mathbf{x}) &

\frac{\partial}{\partial x_2}f_1(\mathbf{x}) & \cdots &

\frac{\partial}{\partial x_n}f_1(\mathbf{x})\\

\frac{\partial}{\partial x_1}f_2(\mathbf{x}) &

\frac{\partial}{\partial x_2}f_2(\mathbf{x}) & \cdots &

\frac{\partial}{\partial x_n}f_2(\mathbf{x})\\

\vdots & \vdots & \ddots & \vdots\\

\frac{\partial}{\partial x_1}f_m(\mathbf{x}) &

\frac{\partial}{\partial x_2}f_m(\mathbf{x}) & \cdots &

\frac{\partial}{\partial x_n}f_m(\mathbf{x})

\end{bmatrix}\in\mathbb{R}^{m\times n}$$
可视化微分大小：
![[Pasted image 20260318093008.png|286]]
# 向量逐元素运算求导
$\mathbf{y}=\mathbf{f}(\mathbf{w})\bigcirc\mathbf{g}(\mathbf{x})$这意味着一个关键的事实，逐元素运算的每个输出只依赖对应索引的输入
考虑Jacobian矩阵：
$$J_{\mathbf w}

=

\frac{\partial \mathbf y}{\partial \mathbf w}

=

\begin{bmatrix}

\frac{\partial}{\partial w_1}\!\big(f_1(\mathbf w)\odot g_1(\mathbf x)\big) &

\frac{\partial}{\partial w_2}\!\big(f_1(\mathbf w)\odot g_1(\mathbf x)\big) & \cdots &

\frac{\partial}{\partial w_n}\!\big(f_1(\mathbf w)\odot g_1(\mathbf x)\big)\\

\frac{\partial}{\partial w_1}\!\big(f_2(\mathbf w)\odot g_2(\mathbf x)\big) &

\frac{\partial}{\partial w_2}\!\big(f_2(\mathbf w)\odot g_2(\mathbf x)\big) & \cdots &

\frac{\partial}{\partial w_n}\!\big(f_2(\mathbf w)\odot g_2(\mathbf x)\big)\\

\vdots & \vdots & \ddots & \vdots\\

\frac{\partial}{\partial w_1}\!\big(f_n(\mathbf w)\odot g_n(\mathbf x)\big) &

\frac{\partial}{\partial w_2}\!\big(f_n(\mathbf w)\odot g_n(\mathbf x)\big) & \cdots &

\frac{\partial}{\partial w_n}\!\big(f_n(\mathbf w)\odot g_n(\mathbf x)\big)

\end{bmatrix}$$
$$J_{\mathbf x}

=

\frac{\partial \mathbf y}{\partial \mathbf x}

=

\begin{bmatrix}

\frac{\partial}{\partial x_1}\!\big(f_1(\mathbf w)\odot g_1(\mathbf x)\big) &

\frac{\partial}{\partial x_2}\!\big(f_1(\mathbf w)\odot g_1(\mathbf x)\big) & \cdots &

\frac{\partial}{\partial x_n}\!\big(f_1(\mathbf w)\odot g_1(\mathbf x)\big)\\

\frac{\partial}{\partial x_1}\!\big(f_2(\mathbf w)\odot g_2(\mathbf x)\big) &

\frac{\partial}{\partial x_2}\!\big(f_2(\mathbf w)\odot g_2(\mathbf x)\big) & \cdots &

\frac{\partial}{\partial x_n}\!\big(f_2(\mathbf w)\odot g_2(\mathbf x)\big)\\

\vdots & \vdots & \ddots & \vdots\\

\frac{\partial}{\partial x_1}\!\big(f_n(\mathbf w)\odot g_n(\mathbf x)\big) &

\frac{\partial}{\partial x_2}\!\big(f_n(\mathbf w)\odot g_n(\mathbf x)\big) & \cdots &

\frac{\partial}{\partial x_n}\!\big(f_n(\mathbf w)\odot g_n(\mathbf x)\big)

\end{bmatrix}$$
由逐元素运算的性质可知，Jacobian就是对角矩阵
$$\begin{align}
\frac{\partial \mathbf{y}}{\partial \mathbf{w}}
&=
\operatorname{diag}\!\Big(
\frac{\partial}{\partial w_1}\!\big(f_1(w_1)\odot g_1(x_1)\big),\,
\frac{\partial}{\partial w_2}\!\big(f_2(w_2)\odot g_2(x_2)\big),\,
\ldots,\,
\frac{\partial}{\partial w_n}\!\big(f_n(w_n)\odot g_n(x_n)\big)
\Big),\\[6pt]
\frac{\partial \mathbf{y}}{\partial \mathbf{x}}
&=
\operatorname{diag}\!\Big(
\frac{\partial}{\partial x_1}\!\big(f_1(w_1)\odot g_1(x_1)\big),\,
\frac{\partial}{\partial x_2}\!\big(f_2(w_2)\odot g_2(x_2)\big),\,
\ldots,\,
\frac{\partial}{\partial x_n}\!\big(f_n(w_n)\odot g_n(x_n)\big)
\Big).
\end{align}$$








