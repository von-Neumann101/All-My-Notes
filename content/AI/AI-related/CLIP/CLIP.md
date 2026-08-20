在NLP领域中，训练数据非常充足，就拿一段话来说：
`Too many times to make it home`
这个文本的每一个部分都可以作为监督（因为文本是一个token一个token生成的），比如：
在模型已经生成`Too many`的时候，可以以`Too many times`作为监督。
而互联网上有几乎无限的文本，而每个文本可以自监督，这使得NLP领域有大量数据
# CLIP
互联网上有大量的图文对，这属于“弱监督、自然监督”（人类无意标注的）。通过使用这些数据可以获得比ImageNet等人类标注数据集更多的数据量

![[Pasted image 20260807100157.png]]
我们有$N$个图文对，文本和图像同时输入模型
## 训练
每次训练使用Text Encoder和Image Encoder分别把$N$个文字和$N$个图像转换为特征向量（注意，这两个编码器之间没有交叉注意力），然后计算每个$I_i$和$T_j$的余弦相似度
实际上这里有一个可学习的温度参数$\tau$，最终的相似度矩阵是$\{T\}_{ij}=\frac{I_i^TT_j}{\tau}$

显然，$T_i,I_i$是配对的，**对角线的元素应该是最大**的，所以构造第一个Loss：
$$
\mathcal L_{\text{image}\to\text{text}}=-\frac1N\sum_{i=1}^N\log\dfrac{\exp(S_{ii})}{\sum_{j=1}^N\exp(S_{ij})}
$$
同理我们也要从文字找图片
$$
\mathcal L_{\text{text}\to\text{image}}=-\frac1N\sum_{i=1}^N\log\dfrac{\exp(S_{ij})}{\sum_{j=1}^N\exp(S_{ji})}
$$
其算术平均作为最终的Loss
> [!NOTE] $\tau$ 的作用
> 由于最后要对相似度做softmax，使用$\tau$缩放以后，两个相似度的比值变为
> $$\frac{p_i}{p_j}=\exp(\dfrac{s_i-s_j}{\tau})$$增大$\tau$会显著增加分布的方差
## 推理
推理时只输入一张图片，但是Text有$K$个候选，分别被填入模板`A photo of a {object}`，然后被输入模型产生$K$个相似度，然后选择最大的
#图像分类 #网络训练 #神经网络 
