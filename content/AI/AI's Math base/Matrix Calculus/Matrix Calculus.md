我们讨论的矩阵$X$中的元素之间**没有依赖关系**，也即：
$$
\frac { \partial X _ { k l } } { \partial X _ { i j } } = \delta _ { i k } \delta _ { l j }
$$
较为常用的求导运算法则
$$
 \begin{aligned} \partial \mathbf{A} &= 0 && (\mathbf{A}\text{ is a constant}) \\[2mm] \partial(\alpha \mathbf{X}) &= \alpha\,\partial \mathbf{X} \\[2mm] \partial(\mathbf{X}+\mathbf{Y}) &= \partial\mathbf{X}+\partial\mathbf{Y} \\[2mm] \partial\!\left(\operatorname{Tr}(\mathbf{X})\right) &= \operatorname{Tr}(\partial\mathbf{X}) \\[2mm] \partial(\mathbf{X}\mathbf{Y}) &= (\partial\mathbf{X})\mathbf{Y} +\mathbf{X}(\partial\mathbf{Y}) \\[2mm] \partial(\mathbf{X}\circ\mathbf{Y}) &= (\partial\mathbf{X})\circ\mathbf{Y} +\mathbf{X}\circ(\partial\mathbf{Y}) \\[2mm] \partial(\mathbf{X}\otimes\mathbf{Y}) &= (\partial\mathbf{X})\otimes\mathbf{Y} +\mathbf{X}\otimes(\partial\mathbf{Y}) \\[2mm] \partial(\mathbf{X}^{-1}) &= -\mathbf{X}^{-1}(\partial\mathbf{X})\mathbf{X}^{-1} \\[2mm] \partial\!\left(\det(\mathbf{X})\right) &= \operatorname{Tr}\!\left( \operatorname{adj}(\mathbf{X})\,\partial\mathbf{X} \right) \\[2mm] \partial\!\left(\det(\mathbf{X})\right) &= \det(\mathbf{X}) \operatorname{Tr}\!\left( \mathbf{X}^{-1}\partial\mathbf{X} \right) \\[2mm] \partial\!\left(\ln(\det(\mathbf{X}))\right) &= \operatorname{Tr}\!\left( \mathbf{X}^{-1}\partial\mathbf{X} \right) \\[2mm] \partial\mathbf{X}^{T} &= (\partial\mathbf{X})^{T} \\[2mm] \partial\mathbf{X}^{H} &= (\partial\mathbf{X})^{H} \end{aligned}
$$
其中$\otimes$代表Kronecker 积
$$
X\otimes Y=\begin{bmatrix}
a & b \\
c & d
\end{bmatrix}\otimes Y=\begin{bmatrix}
aY & bY \\
cY & dY
\end{bmatrix}
$$
$\circ$代表Hadamard 积
$$
(X\circ Y)_{ij}=X_{ij}Y_{ij}
$$
# Matrix Differentation
令$y=\phi(x)$，其中 $y$ 和 $x$ 分别是$m,n$维向量，我们约定：
$$
\frac{\partial \mathbf{y}}{\partial \mathbf{x}} = \begin{bmatrix} \frac{\partial y_1}{\partial x_1} & \frac{\partial y_1}{\partial x_2} & \cdots & \frac{\partial y_1}{\partial x_n} \\[2mm] \frac{\partial y_2}{\partial x_1} & \frac{\partial y_2}{\partial x_2} & \cdots & \frac{\partial y_2}{\partial x_n} \\[2mm] \vdots & \vdots & \ddots & \vdots \\[2mm] \frac{\partial y_m}{\partial x_1} & \frac{\partial y_m}{\partial x_2} & \cdots & \frac{\partial y_m}{\partial x_n} \end{bmatrix}
$$
**定理**：若$y=Ax$，其中 $x,y$ 分别为 $n,m$ 维向量，$A$ 不依赖 $x$，那么：
$$\frac{\partial y}{\partial x}=A$$
**定理**：若 $x$ 是向量 $z$ 的函数，且 $A$ 不依赖 $z$，那么：
$$
\frac{\partial y}{\partial x}=A\frac{\partial x}{\partial z}
$$
**定理**：若$\alpha=x^TAx$，其中 $A$是方阵 ，那么
$$
\frac{\partial\alpha}{\partial x}=x^T(A+A^T)
$$
**定理**：若$\alpha=y^TAx$，其中 $A\in \mathbb R^{m\times n}$ ，那么
$$
\frac{\partial\alpha}{\partial z}=x^TA^T\frac{\partial y}{\partial z}+y^TA\frac{\partial  x}{\partial z}
$$
**定义**：若$A\in \mathbb R^{m\times n}$的每个元素都是标量参数$\alpha$的函数，那么：
$$
\frac{\partial \mathbf{A}}{\partial \alpha} = \begin{bmatrix} \frac{\partial a_{11}}{\partial \alpha} & \frac{\partial a_{12}}{\partial \alpha} & \cdots & \frac{\partial a_{1n}}{\partial \alpha} \\[2mm] \frac{\partial a_{21}}{\partial \alpha} & \frac{\partial a_{22}}{\partial \alpha} & \cdots & \frac{\partial a_{2n}}{\partial \alpha} \\[2mm] \vdots & \vdots & \ddots & \vdots \\[2mm] \frac{\partial a_{m1}}{\partial \alpha} & \frac{\partial a_{m2}}{\partial \alpha} & \cdots & \frac{\partial a_{mn}}{\partial \alpha} \end{bmatrix}
$$
