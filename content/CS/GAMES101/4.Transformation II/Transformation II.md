# 3D Rotations
绕$x$轴旋转：
$$
R_x(\alpha)=
\begin{pmatrix}
1 & 0 & 0 & 0\\
0 & \cos\alpha & -\sin\alpha & 0\\
0 & \sin\alpha & \cos\alpha & 0\\
0 & 0 & 0 & 1
\end{pmatrix}
$$
绕$y$轴旋转：
$$
R_y(\alpha)=
\begin{pmatrix}
\cos\alpha & 0 & \sin\alpha & 0\\
0 & 1 & 0 & 0\\
-\sin\alpha & 0 & \cos\alpha & 0\\
0 & 0 & 0 & 1
\end{pmatrix}
$$
绕$z$轴旋转：
$$
R_z(\alpha)=
\begin{pmatrix}
\cos\alpha & -\sin\alpha & 0 & 0\\
\sin\alpha & \cos\alpha & 0 & 0\\
0 & 0 & 1 & 0\\
0 & 0 & 0 & 1
\end{pmatrix}
$$
显然，任何一个图形可以按$x,y,z$分别旋转：
$$
\mathrm R_{xyz}(\alpha,\beta,\gamma)=\mathrm R_x(\alpha)\mathrm R_y(\beta)\mathrm R_z(\gamma)
$$
# Viewing Transformation
## View / Camera Transformation
![[Pasted image 20260920160700.png|580]]
如果相机和物体没有相对运动，那么拍的照是一样的
![[Pasted image 20260920160848.png|446]]
所以我们最好是固定二者之一，约定：相机在原点，up在y，look在-z
![[Pasted image 20260920161010.png|242]]
