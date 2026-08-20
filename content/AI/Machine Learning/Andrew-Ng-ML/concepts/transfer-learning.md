---
type: concept
course: Machine Learning
priority: C
status: draft
aliases: []
related: []
---

# Transfer Learning

## 一句话定义

transfer learning 是把一个已在相关任务上训练好的模型或特征提取层迁移到新任务上的方法。它解决的是新任务数据较少时，从零训练神经网络成本高、效果不稳定的问题。

## 核心思想

笔记把预训练网络的输入层和隐藏层称作“处理层”：这些层已经学到图像等输入的通用表示。新任务可以替换输出层，再选择冻结前面层只训练新输出层，或把预训练权重作为初始值继续微调。大数据集上预训练、小数据集上微调就是监督预训练的典型用法。

## 核心边界 / Objective / Assumption

设预训练特征提取器为 $h=F_{\theta}(x)$，新输出头为 $\hat y=g_{\phi}(h)$。输入 $x$ shape 取决于任务，例如图像可为 $\mathbb{R}^{h\times w\times c}$；参数 $\theta$ 可冻结或微调，$\phi$ 通常新初始化并训练。训练 objective 是新任务上的 loss，而不是保留原任务输出层。

## 模型假设 / 局限

transfer learning 适合源任务和目标任务输入结构相似、底层特征可复用的场景，例如图像识别。若源任务与目标任务差异太大，迁移可能帮助有限甚至负迁移。它主要适用于神经网络；笔记也指出决策树不容易像神经网络一样串联多个模型一起训练。冻结层数、微调策略和学习率需要人工补充。

## 在 Machine Learning 中的位置

它位于 [[neural-network]]、[[data-augmentation]] 和泛化诊断之后，是项目层面的训练策略。它把已有表示迁移到新数据上，减少对大规模标注数据的依赖。

## 重要公式 / 算法

- 公式 / 算法名称：Frozen Feature Extractor
- 解决的问题：在小数据集上复用预训练表示。
- 核心含义：$\hat y=g_{\phi}(F_{\theta}(x))$，冻结 $\theta$，只训练 $\phi$。
- 相关概念链接：[[neural-network]]

- 公式 / 算法名称：Fine-tuning
- 解决的问题：让预训练模型适配新任务。
- 核心含义：用预训练 $\theta$ 作为初始值，再在新任务 loss 上更新部分或全部参数；具体策略需要人工补充。
- 相关概念链接：[[optimization]]

## 容易混淆点

- transfer learning vs data augmentation：前者复用已有模型，后者扩充训练数据。
- frozen layer vs fine-tuning：冻结不更新旧层，fine-tuning 会继续更新部分旧层。
- pretraining vs new output head：预训练保留的是表示，不一定保留原输出层。
- model reuse vs data leakage：预训练数据和评估协议需要清楚区分。

## 相关概念

- [[neural-network]]
- [[data-augmentation]]
- [[optimization]]
- [[overfitting]]

## 跨课程连接

- CS61A：可看作函数组合中复用已有子函数，再替换最后一层输出函数。
- CS61B：模型组件复用类似模块化系统设计，需要清楚接口和数据 shape。
- CSAPP：预训练模型推理和微调受内存、矩阵计算和硬件性能限制。
- UMich DL：直接连接 pretrained models、fine-tuning、frozen backbone 和 transfer learning workflow。
