Octo
# Octo Model
![[Pasted image 20260806082445.png]]
Octo提供了一种**非常模块化**的模型架构设计，可以非常便捷地拓展模型输入与输出
有各种预训练的Transformer块，比如需要新的摄像头输入，无需重改整个模型，只需要往模型中插入Observation块即可
## Model
### Architecture
主要是三个部分
- input tokenizers：将语言指令$l$（或目标图像$g$）和观察序列$o_1,...,o_H$转换为输入Token
- transformer backbone：将输入Token转化为动作生成的Embedding
- readout heads：产生动作$a$的读出头
#### Task and observation tokenizers
具体见架构图片，注意这里添加了**可学习的位置编码**
#### Transformer backbone and readout heads
在Transformer Backbone中使用了**块级掩码**，比如Observation块只能看到之前Observation块的输出。这种块级掩码同时也可以**使得Readout不被任何Observation, Task块关注**
### Training objective
我们每次只需要一次Transformer的前向传播得到的Embedding $e$，然后就能使用扩散模型以此生成动作$a$
具体是：采样一个高斯噪声向量$x^K\sim\mathcal N(0,I)$，并进行$K$步去噪：
$$
x ^ { k \, - \, 1 } = \alpha ( x ^ { k } - \gamma \epsilon _ { \theta } ( x ^ { k }, e, k ) + \mathcal { N } \big ( 0, \sigma ^ { 2 } I \big ) ).
$$
其中$\epsilon_\theta$是去噪网络，其接收时间步$k$，Transformer输出的Embedding $e$，和上一步的向量$x^k$。参数$\alpha,\gamma,\sigma$是noise scheduler，文章中使用标准余弦scheduler
#Diffusion-Model #Transformer #卷积神经网络 #VLA 