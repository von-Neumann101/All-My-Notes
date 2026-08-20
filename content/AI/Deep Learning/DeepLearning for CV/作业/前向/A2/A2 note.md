# 支持向量机部分(SVM)：
**这是Score(N x C)部分**，简单的矩阵乘法
$$Socre=\begin{bmatrix}
x_1\\x_2\\x_3
\end{bmatrix}
\begin{bmatrix}
W_1 & W_2 & W_3
\end{bmatrix}=\begin{bmatrix}
x_1W_1 & x_1W_2 & x_1W_3\\
x_2W_1 & x_2W_2 & x_2W_3\\
x_3W_1 & x_3W_2 & x_3W_3
\end{bmatrix}$$

**这是Margin部分**（这里只是举一个例子，让一些结果为0了
$$margin=\begin{bmatrix}
0 & x_1W_2-x_1W_1+1 & 0\\
0 & 0 & 0\\
x_3W_1-x_3W_3 +1& x_3W_2-x_3W_3 +1& 0
\end{bmatrix}$$
简单说说这是怎么算的：
$$L_i=\sum_{j\ne y_i}\max\!\left(0,\; s_j-s_{y_i}+1\right)$$
这里我们是对 $j$ 求和，也就是每列的非对角元素，宽泛的说就是样本中和 $y_{train}$ 不等的地方对应的分数，即：$$\begin{bmatrix}
0 & x_1W_2-x_1W_1 & x_1W_3-x_1W_1\\
x_2W_1-x_2W_2 & 0 & x_2W_3-x_2W_2\\
x_3W_1-x_3W_3 & x_3W_2-x_3W_3 & 0
\end{bmatrix}$$
这时我们就需要广播了
最后 +1 取 0 就得到Margin了

**这是Loss部分**
注意我们$Loss$部分是不对正确部分求和的，所以我们把margin里**每个样本**里**正确标签的位置**变为0（就是把1变为0），再把矩阵的每个元素都加起来，除以N就得到Loss了

**这是dW部分**
我们先不看ReLU的部分，先对矩阵求导
$$\frac{\partial L}{\partial W_j}

=

\frac{\partial L}{\partial m_{ij}}

\cdot

\frac{\partial m_{ij}}{\partial s_{ij}}

\cdot

\frac{\partial s_{ij}}{\partial W_j}$$ 这样就非常直观了
第一项：就是当大于0的时候是1，小于等于0的时候是0
第二项：j不等于y[i]的时候是+1不是的时候则是-1
第三项：例如对$W_1$求导的时候$$\begin{bmatrix}
x_1 & 0 & 0\\
x_2 & 0 & 0\\
x_3 & 0 & 0
\end{bmatrix}$$
**注意注意**，这里是**Score矩阵**对W求导
$s_{i}=W^Tx_i$ 这里的s是一个向量，是一个样本的每个类的评分
那么$s_{ij}$也就是向量s的每个分量
这样也就对应了每个W
先算$L_i$的梯度，就是对 $j$ ：第一项：我们每次都要让第j列的W减去一个x，第二项是一个固定值。这个求和的次数就是错误类的个数（margin>0)
我们创建一个mask矩阵，用于表示加的次数
$$mask=\begin{bmatrix}
0 & 1 & 0\\
0 & 0 & 0\\
1& 1& 0
\end{bmatrix}$$
然后我们需要每个正确位置（每个样本的y_train）变成-（margin>0个数）
$$mask=\begin{bmatrix}
-1& 1 & 0\\
0 & 0 & 0\\
1& 1& -2
\end{bmatrix}$$
例如我们的$W_1$：
一共三项求和，第一个是$-x_1+0x_2+x_3$(第一个负号是因为正确分类就是1，第二个0是因为margin=0，第三个正号是因为他是错误分类)
# Softmax
我真的是太高兴了，多么美好的一天！
							——2026.3.14-15:53
我们接下来彻底解决各种问题
$$dw_j=\frac{\partial L}{\partial w_j}=(p_j-y_j)x_i$$
>这里的p就是softmax搞出来的概率（模型输出），y就是真实标签（one-hot），x就是一个样本的特征向量

这很简单，就是求导
$$\begin{align}
s_{ij} &= w_j^T x_i \\
\\
p_{ij} &=
\frac{e^{s_{ij}}}{\sum_{k=1}^{C} e^{s_{ik}}} \\
\\
L_i &= -\log p_{i y_i} \\
&= -\log \frac{e^{s_{i y_i}}}{\sum_{k=1}^{C} e^{s_{ik}}} \\
&= -s_{i y_i} + \log \left(\sum_{k=1}^{C} e^{s_{ik}}\right) \\
\\
\frac{\partial L_i}{\partial w_j}
&=
\frac{\partial}{\partial w_j}
\left(
-s_{i y_i}
+
\log \sum_{k=1}^{C} e^{s_{ik}}
\right) \\
\\
\frac{\partial (-s_{i y_i})}{\partial w_j}
&=
-\mathbf{1}(j=y_i)x_i \\
\\
\frac{\partial}{\partial w_j}
\log \sum_{k=1}^{C} e^{s_{ik}}
&=
\frac{1}{\sum_{k} e^{s_{ik}}}
\frac{\partial}{\partial w_j}
\sum_{k} e^{s_{ik}} \\
&=
\frac{1}{\sum_{k} e^{s_{ik}}}
e^{s_{ij}} x_i \\
&=
\frac{e^{s_{ij}}}{\sum_{k} e^{s_{ik}}} x_i \\
&=
p_{ij}x_i \\
\\
\frac{\partial L_i}{\partial w_j}
&=
p_{ij}x_i
-
\mathbf{1}(j=y_i)x_i \\
&=
(p_{ij}-\mathbf{1}(j=y_i))x_i \\
\\
\frac{\partial L}{\partial w_j}
&=
\frac{1}{N}
\sum_{i=1}^{N}
(p_{ij}-\mathbf{1}(j=y_i))x_i
\end{align}$$
先不管样本，我们固定一个样本（暂时忽略i）
$dW_{:,j}=(p_j-y_j)\cdot x_i$这是对每一列
我们同时扩充 $j$ 
$$dW=x_i(p_i-y_i)^T$$
这里p和y就是向量了
再
$$dW=\sum_{i=1}^Nx_i(p_i-y_i)^T=X^T(P-Y)$$
