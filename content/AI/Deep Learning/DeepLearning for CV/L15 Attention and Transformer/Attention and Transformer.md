# Attention
Encoder-Decoder：
![[Pasted image 20260729103231.png|383]]
Encoder把序列的所有信息压缩到一个**定长**的上下文向量$c$中。显然，我们**输入的序列长度很可能会远远大于$c$的长度**，从信息熵的角度来说，$c$绝对会**损失信息**。所以我们考虑在每次输出结果的时候都**回顾**一下输入序列

Attention：
![[Pasted image 20260729103614.png]]
每个时间步中，*Encoder* 部分会根据**输入序列**以及 *Decoder* 部分的**隐藏状态**，输出 *Encoder* **每个隐藏状态的权重**(Attention)，其加权求和作为**上下文向量**输入 *Decoder* 部分

**Example**：
![[Pasted image 20260729105018.png|327]]
比如这里在翻译européenne的时候，European的权重几乎为1
> [!NOTE] 端到端 (E2E)
> 模型直接从任务的原始输入，产生最终需要的输出，并且整个过程主要由最终任务的损失函数统一训练。

可以发现，这里的Attention被嵌入到RNN中解决其上下文过长信息丢失的问题，但是Attention的作用**远不止于此**——Attention Layer
# Transformer
![[Pasted image 20260729112251.png]]
这里的Query Vector的命名是非常准确的（对应《Attention is All You Need》）
从信息量的角度来解释：Data Vector是**不变**的，他是由输入序列生成的蕴含前文信息的向量，到底要提取什么信息，这是由当前**准备输出**的数据(decoder states)决定，也就是Query Vector。
如此，我们将Attention从RNN中剥离开来，输入的序列变为Data Vector，经过Query Vector查询得到Data Vector的加权（当前准备输出的token），就是Attention的输出
## Attention Layer
![[Pasted image 20260729114447.png|697]]
这里取$f_{\text{att}}(q,X_i)=\vec q\cdot\vec X_i/\sqrt{D_Q}$（除以的这个常数防止梯度消失——过大的数进入softmax的平缓区域）

为了提高性能，我们需要矩阵运算：
![[Pasted image 20260729115726.png]]
注意到$X$被用在多个地方——和查询向量生成权重（softmax前），作为数据被加权。我们需要**分离这两种用法**，具体的做法**交给神经网络来处理**（当然，还有一种直接的解释，因为矩阵大小不匹配）——我们多加两个可学习参数$W_K,W_V$。于是我们有了Keys和Values的概念
![[Pasted image 20260729115314.png]]
$$\mathrm{Attention}(Q,K,V)=\mathrm{softmax}\!\left(\frac{QK^{\top}}{\sqrt{d_k}}\right)V$$
美化一下：
![[Pasted image 20260729120742.png]]
由于该层接受两个来源的输入Query和Data，所以叫其交叉注意力

如果只有一个Data的输入，我们叫他自注意力
**Self-Attention**：
![[Pasted image 20260729120520.png]]
## 位置编码
![[Pasted image 20260729144040.png|243]]
我们把输入序列打乱，对输出序列的**唯一影响**就是输出序列按照同样方式打乱（输出的结果**不会有其他任何差别**）。但是文本需要顺序，**如果我们调整语序，句子的含义应该是要不同的**，否则我们会缺少文本顺序的信息量。

为了解决这个问题，我们在向量中加入位置编码：

![[Pasted image 20260729144527.png|302]]
点积的结果为：
$$
{ ( R ( \theta _ { i } ) q _ { i } ) ^ { T } ( R ( \phi _ { j } ) k _ { j } ) } \\ { = q _ { i } ^ { T } R ( \phi _ { j } - \theta _ { i } ) k _ { j } } \\
$$
## 掩码
再次申明，Query向量的作用是对Key向量进行查询，可以得到想要对文本的哪个部分进行关注，再通过加权求和来得到结果。
但是，由于自回归的属性，在生成第一个token时，**Query向量能看到这个token之后的数据**，那么显然预测后面的那个字就会更关注$V_2$，但这是一种作弊，可能会把模型训坏。
所以我们在训练时不能让模型查看到未来，所以：
![[Pasted image 20260729150458.png]]
这里要**竖着看**，就拿第一行举例
## Multiheaded Self-Attention Layer
![[Pasted image 20260729150829.png]]
用多个注意层在同一个序列上**并行**运行注意力，然后将输出的向量拼接。这里$O_i$就相当于单个注意力层输出的$Y_i$
## The Transformer
![[Deep Learning/DeepLearning for CV/L15 Attention and Transformer/Pic/image-3.png|430]]
在上述的多头注意力层后，我们对输出序列的每个token都施加一个MLP（同一个参数）
注意，Encoder可以提前算，也就是说，运行时不断循环计算的只是Decoder的部分
# ViT
![[Pasted image 20260729152539.png]]
这里把图片切为**Patches**然后展平为一维向量——一个 patch 相当于一个 token；这个 patch 展平后再经过线性投影，得到的向量相当于该 token 的 embedding

ViT中没有掩码注意力了，因为图像没有所谓的未来
#注意力 #Transformer #ViT #残差 #归一化