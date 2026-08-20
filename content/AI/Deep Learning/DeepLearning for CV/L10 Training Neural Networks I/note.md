# Activation Functions
![[Pasted image 20260328092024.png|492]]
## 种类
### Sigmoid
![[Pasted image 20260328092216.png|190]]
可以较好的表示 *开或关* 在很小的区间快速增长，收敛到1 or 0
但是其存在问题：
1. 梯度消失（平坦区域很大，绝对值大于5的地方就块平了），低层级无法训练，**学习困难**
2. 输出不是0中心的，全为正，或者全为负（只能在两个象限（？卦）移动）
  ![[Pasted image 20260328092925.png|225]]
  3. exp()计算昂贵（对GPU不大所谓）
### Tanh
  ![[Pasted image 20260328093604.png|213]]
  解决了Sigmoid的第二个问题
### ReLU
![[Pasted image 20260328093651.png|187]]
夯爆了（收敛快，开销少，大于0梯度明显）
问题
1. 非0中心
2. x如果小于0，下游所有神经元都是0，学习完全停止
Dead ReLU：
![[Pasted image 20260328094014.png|406]]
一旦超过Data Cloud，所有的激活值都为0，完全无法训练
### Leaky ReLU
$$f(x)=max(0.01x,x)$$
0.01是可调超参数，对于这种超参数，我们考虑学习
### Parametric Rectifier(PReLU)
$$f(x)=max(\alpha x,x)$$其中alpha可学习
### Exponential Linear Unit(ELU)
![[Pasted image 20260328094549.png|294]]
在$\mathbb{R}$上可导，有0中心（近似）
$\alpha$一般不设置为可学习
### Scale Exponential Linear Unit(SELU)
![[Pasted image 20260328094844.png|306]]
有自归一化的性质（不用归一化也能训练很多层网络），具体为什么，91页数学推导
![[Pasted image 20260328095018.png|575]]
准确率相差不大，且每次的赢家都不一样（就更LSTM的各种变种一样）
除了Sigmoid和Tanh，其他差不多（小于0.1%）
# Data Pre-processing
![[Pasted image 20260328100112.png|479]]
zero-centered->normalized
`X -= np.mean(X, axis=0)`->`X /= np.std(X, axis=0)`
这样可以0中心
![[Pasted image 20260328100209.png|506]]
## 原因
![[Pasted image 20260328100445.png|538]]
对于线性分类，如果不是0中心，会导致线性分类器对权重非常敏感（距离放大）
## 示例
![[Pasted image 20260328100647.png|480]]
PCA和白化不太常见
# Weight Initialization
全部初始化为0，显然不好！ReLU会炸
对于浅层的网络我们考虑使用高斯分布，但是这对于深层网络不太好——梯度消失，激活值趋于0
解释一下这里的图：x轴就是Activation值，y轴代表频率
![[Pasted image 20260328101220.png|561]]
我们可以考虑增大权重矩阵的初始值，但是会导致更大问题
![[Pasted image 20260328101345.png|566]]
## 种类
### Xavier初始化
![[Pasted image 20260328101532.png|510]]
这里的`Din`指的是**当前层每个神经元接收的输入数量**（如果是ConvNet，Din就是每个卷积核在一个位置上看到的输入数量）
但是这只适合tanh和Sigmoid之类的激活函数，对ReLU没有作用
![[Pasted image 20260328103148.png]]
### Kaiming/MSRA初始化
只要乘以$\sqrt{2}$，就能修复
![[Pasted image 20260328103303.png]]由于残差网络+x的特性，导致$\mathrm{Var}(F(x)+x)>\mathrm{Var}(x)$严格单增，导致方差越来越大，最后权重越来越小
解决方法就是：第一层用Kaiming，第二层全部初始化为0（方差不变）
![[Pasted image 20260328103708.png|151]]
# Regularization
L2, L1, L1+L2
## 种类
### Dropout
![[Pasted image 20260328104012.png|481]]
鲁棒性提高，多学一点（拒绝一招鲜吃遍天）
相当于我们训练的非常多共享权重的子网络，最终的结果就是这些网络的集成
但是在测试的时候我们要关闭这种不确定性，我们考虑期望$\mathbb{E}_z[f(x,z)]$
![[Pasted image 20260328105100.png]]
所以传播的时候只要乘以一个p就行了

### Inverted dropout
我们以0.5的概率丢弃神经元，其他神经元则乘以2，最后预测的时候不需要放缩
### BatchNorm
其实BatchNorm也是一种类似于dropout的正则化，由于BatchNorm我们的具体输出依赖于我们输入的种类配比，也会产生类似于dropout的防止路径依赖
### 数据增强
稍微扭曲一下，旋转一下数据
### DropConnect
![[Pasted image 20260328111744.png|411]]
### Fractional Pooling
有的神经元2x2Pooling区，有的是1x1Pooling区
### Stochastic Depth
直接把整块丢弃
![[Pasted image 20260328111943.png]]
### Cutout
![[Pasted image 20260328112015.png|567]]
### Mixup
![[Pasted image 20260328112111.png]]
从Beta分布（右上角）中抽取权重，将两个图片加权
## 总结
dropout一般只在大型全连接神经网络中有效
批归一化，数据增强是主流
有时cutout和mixup对于很少的数据量会非常有效
# 回顾
![[Pasted image 20260331194207.png|367]]
我们回顾一下全连接神经网络，顺带解决一下Dropout和Dropconnect
我们输入一个向量 $\vec{x}\in\mathbb{R}^3$ ，其三个分量分别（特征）给输入层的三个神经元，每个连接都代表乘以一个权重，前面的神经元的激活值相加，所以
$w_{ij}$代表的就是i神经元和另一个j神经元的连接
$$\begin{align}
x &= \begin{bmatrix} x_1 & x_2 & x_3 \end{bmatrix} \\

W^{(1)} &= 
\begin{bmatrix}
w_{11} & w_{12} & w_{13} & w_{14} \\
w_{21} & w_{22} & w_{23} & w_{24} \\
w_{31} & w_{32} & w_{33} & w_{34}
\end{bmatrix} \\

h &= x W^{(1)} \\
  &= \begin{bmatrix} h_1 & h_2 & h_3 & h_4 \end{bmatrix} \\

h_1 &= x_1 w_{11} + x_2 w_{21} + x_3 w_{31} \\
h_2 &= x_1 w_{12} + x_2 w_{22} + x_3 w_{32} \\
h_3 &= x_1 w_{13} + x_2 w_{23} + x_3 w_{33} \\
h_4 &= x_1 w_{14} + x_2 w_{24} + x_3 w_{34}
\end{align}$$
所以说，Dropout和Dropconnect的区别就是，一个抹去一个x一个抹去w
Dropout
![[Pasted image 20260331194329.png|371]]
这里就是$x_1=0$（这也等价与删去该点全部的连接）
Dropconnect
![[Pasted image 20260331194441.png|410]]
这里相当于$w_{11},w_{14},w_{22},w_{31}=0$
#激活函数 #dropout #参数初始化 #网络训练