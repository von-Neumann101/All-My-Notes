OpenVLA
# The OpenVLA Model
## Architecture
![[Pasted image 20260730111317.png]]
可以看出，这里具有[[LLaVA]]的大部分结构（实际上VLA模型是基于pre-trained VLM模型的）
Vision Encoder使用两个预训练模型，添加的DinoV2可以提升空间推理能力
## 训练
为了使 VLM 的语言模型主干能够预测**机器人动作**，我们**将动作表示为 LLM 输出空间中的离散标记**

首先，将机器人动作的每个维度单独离散化为 256 个区间之一。对于动作的每个维度，设置统一的区间宽度，将训练数据中该动作维度的第 1 百分位数到第 99 百分位数之间的范围均匀划分。
然后**直接覆盖LLM分词器词表中使用频率最低的 256 个 token，使之作为动作token使用**（一个token对应一种*动作元*）
#VLA #VLM #OpenVLA #网络训练

