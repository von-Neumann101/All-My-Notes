# HardWare
## GPU
![[Pasted image 20260324083858.png|513]]
 CPU：很少的核心，每个核心都很快、很有能力，善于执行**序列任务**
 GPU：很多的核心，每个核心都很慢、看似笨拙，善于执行**并行任务**
![[Pasted image 20260324084714.png]]
 每个核心，同等级的GPU大概 比CPU慢2~3倍

GPU组成：内存 & 处理器
![[Pasted image 20260324085242.png]]
这里的Tensor Core就是专门为了深度学习设计的，用于矩阵运算
由于矩阵计算的结果矩阵的每一个元素都是完全独立的，矩阵的计算是完全并行的，这是非常合适GPU的
## GPU编程
### CUDA
只能用于NVIDIA显卡，可以直接在GPU上编程
### OpenCL
类似于CUDA
## Google TPU
谷歌自己用于计算Tensor的卡
只能用TensorFlow
## GPU内存
在前向传播的时候需要储存所有的激活值，这存储在显存中
相较于计算机GPU，消费级的GPU是不会有很大的内存的，其内存宽带也不同（例如ReLU，其速度不受制于计算速度，其受制于内存到计算单元的传输速度）
# SoftWare
![[Pasted image 20260324092204.png]]
## Pytorch
三个抽象层级(↓)
1. **Tensor**：类似于numpy数组，但是在GPU上跑
2. **Autograd**：自动构建计算图，自动计算梯
3. **Module**：神经网络层
### Tensor
......
### Autograd
在构建Pytorch的张量时，可以传入`requires_grad=True`，标记为需要跟踪（一个规则：如果Pytorch对一个`requires_grad=True`的量运算以后，其结果默认`requires_grad=True`）
```python
import torch
N, D_in, H, D out = 64, 1000, 100, 10
x = torch.randn (N, D_in)
y = torch.randn(N, D_out)
w1 = torch.randn(D_in, H, requires_grad=True)
w2 = torch.randn(H, D_out, requires_grad=True)

learning_rate = 1e-6
for t in range(500):
#不再需要显式跟踪结果，因为这些必要中间值已经被Pytorch储存
	y_pred = x.mm (w1).clamp(min=0).mm(w2)
	loss = (y_pred - y).pow(2).sum()
	
	loss.backward()#这里会告诉Pytorch计算所有权重的梯度
	
	with torch.no_grad():#不要把参数更新加入计算图，否则对更新参数过程求导
		w1 -= learning_rate * w1.grad
		w2 -= learning_rate * w2.grad
		w1.grad.zero_()#清除梯度，Pytorch不会自己清除
		w2.grad.zero_()
```
遇到`loss.backward()`的时候会遍历所有的`requires_grad=True`叶子结点，然后更新权重
![[Pasted image 20260324170436.png|299]]
反向传播结束以后，计算图会被清空，对应内存被释放，梯度被存入`wi.grad`中
### New functions
`y_pred = sigmoid(x.mm (w1)).mm(w2)`
![[Pasted image 20260324171913.png|301]]
不过对于sigmoid和softmax之类的，这么计算并不合适，不然会数值爆炸，以及反向传播时不能使用一些优雅结果而是只能强算一通
![[Pasted image 20260324172216.png|347]]
### Pytorch.nn
 给予了一种面向对象的抽象
 ![[Pasted image 20260324182922.png]]
 ![[Pasted image 20260324183702.png|371]]
### Pytorch: optim
![[Pasted image 20260324183811.png|440]]
后面两句就是自动执行梯度下降，并归零梯度
### Pytorch: nn Defining Modules

![[Pasted image 20260324190229.png]]
可以做一些自己的自定义网络：
![[Pasted image 20260324190343.png]]
Pytorch有着不错的数据加载功能
Pytorch可以提供一些有名的预训练模型

### Pytorch: 动态计算图
![[Pasted image 20260327154259.png]]
动态计算图可以让我们以Python的控制流方法控制梯度

### Pytorch: 静态计算图
![[Pasted image 20260327154530.png]]静态计算图，可以随意修改，我们可以把例如Conv和ReLU融合
![[Pasted image 20260327154812.png|562]]
静态计算图的另一个好处是，可以把这种**数据结构**导入到磁盘，然后用别的更高效的语言运行，如C++
不过，动态计算图对于**输入数据影响模型结构**（RNN、递归神经网络）很友好
#GPU #Pytorch #计算图
