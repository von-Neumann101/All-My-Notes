LLaVA——**L**arge **L**anguage **a**nd **V**ision **A**ssistant
# Visual Instruction Tuning
## Architecture
![[Pasted image 20260730103422.png|570]]
Vision Encoder用于**提取图像$X_v$的特征**$Z_v=g(X_v)$，接下来使用一个可学习的简单线性层(Projector)把图像特征**映射到word embedding空间**$H_v=W\cdot Z_v$
然后加上Prompt的word embedding一起输入到大语言模型$f_{\phi}$中
## Training
对于每张图像$X_v$，我们使用GPT-4（仅语言模型）生成多轮对话数据$(X_q^1,X_a^1,...,X_q^T,X_a^T)$，上标代表轮数，将第$t$轮的指令定义为：
$$
\mathbf{X}_{\mathrm{instruct}}^{t}
=
\begin{cases}
\text{Randomly choose } [\mathbf{X}_{q}^{1}, \mathbf{X}_{v}]
\text{ or } [\mathbf{X}_{v}, \mathbf{X}_{q}^{1}],
& \text{the first turn } t = 1, \\
\mathbf{X}_{q}^{t},
& \text{the remaining turns } t > 1.
\end{cases}
$$
目标答案的概率，每个词都有图像、之前的指令、已生成的答案（包括以前的答案序列和该序列已生成的token）作为条件
$$
p ( X _ { a } \mid X _ { v }, X _ { \mathrm { i n s t r u c t } } ) = \prod _ { i = 1 } ^ { L } p _ { \theta } \left( x _ { i } \mid X _ { v }, X _ { \mathrm { i n s t r u c t }, < i }, X _ { a, < i } \right).
$$
多轮对话拼为一个输入序列，其形式是：
![[Pasted image 20260730105110.png]]
在自回归模型中，***只有$X_a^k$以及$\text{<STOP>}$参与损失函数的计算***
> [!NOTE] GPT-4生成对话数据
> 先从数据集取一张图像和其标注（caption和bounding box的坐标）
> 由于**GPT-4无法看到图片**，把标注输入进去，作为图像的**代替表示**
> 一辆黑色 SUV 停在地下车库，几个人正在往车里装行李。  
> person: $[0.68,0.24,0.77,0.69]$
> suitcase: $[0.75,0.41,0.84,0.69]$
### 微调
**Stage 1——特征对齐**
我们**只训练Projector**，把其他预训练模型的参数冻结，这样我们就能为冻结的 LLM 训练一个与之兼容的视觉分词器

**Stage 2——E2E微调**
仍然始终冻结视觉编码器的参数，但会继续更新 LLaVA 中投影层和 LLM 的参数
#微调 #后训练 #网络训练 #特征对齐 #LLaVA #Vision-Encoder #多模态