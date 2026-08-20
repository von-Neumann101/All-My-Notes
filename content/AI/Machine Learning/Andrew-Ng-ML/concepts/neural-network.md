---
type: concept
course: Machine Learning
priority: A
status: draft
aliases: []
related: []
---

# Neural Network

## 一句话定义

neural network 是由多层可学习变换和非线性激活函数组成的模型。它解决的是线性模型表达能力不足时，如何从数据中自动学习中间特征并完成预测。

## 核心思想

一个神经元可以看作类似 [[logistic-regression]] 的计算单元；多层神经元组合后，前面层学习中间表示，后面层把表示转成输出。非线性激活函数是关键，否则多层线性变换仍等价于一个线性模型。

## 核心边界 / Objective / Assumption

输入可写为 $X\in\mathbb{R}^{m\times n}$，每层有权重和偏置。常见 dense layer 的 model form 可写为 $A^{[l]}=g(Z^{[l]})$，$Z^{[l]}=A^{[l-1]}W^{[l]}+b^{[l]}$；这是标准写法，当前笔记只明确到矩阵乘法和激活值，完整符号系统需要人工补充。参数是各层 $W,b$，输出由任务决定，训练目标是最小化对应 loss/cost。

## 模型假设 / 局限

神经网络适用于结构化和非结构化数据，尤其在手工特征难以设计时有优势。但它更慢、需要更多数据和计算，且更依赖正则化、模型选择和错误分析。若数据是小型表格数据，决策树类模型可能更快且更易解释；若任务很简单，线性或逻辑回归可能足够。

## 在 Machine Learning 中的位置

它从 [[linear-regression]] 和 [[logistic-regression]] 延伸而来：线性变换提供 score，激活函数提供非线性，多层结构提供特征学习。它向后连接 [[forward-propagation]]、[[backpropagation]]、[[optimization]] 和深度学习应用。

## 重要公式 / 算法

- 公式 / 算法名称：Dense Layer Computation
- 解决的问题：计算一层神经元输出。
- 核心含义：笔记中用矩阵乘法理解为 $A^TW+B$ 后接激活函数；更标准 shape 约定需要人工补充。
- 相关概念链接：[[forward-propagation]]

- 公式 / 算法名称：Nonlinear Activation
- 解决的问题：避免多层网络退化为线性模型。
- 核心含义：隐藏层常用 ReLU，输出层根据任务选择 sigmoid、linear 或 softmax。
- 相关概念链接：[[activation-function]]

- 公式 / 算法名称：TensorFlow Sequential Model
- 解决的问题：实现多层网络。
- 核心含义：index.md 提到 `Sequential([... Dense(...) ...])`、`compile(loss=...)`、`fit(...)`。
- 相关概念链接：[[optimization]]

## 容易混淆点

- neural network vs logistic regression：逻辑回归可看作单个简单神经元，神经网络是多层组合。
- layer vs neuron：layer 是一组神经元，neuron 是单个计算单元。
- forward propagation vs training：前向传播计算预测，训练还需要 loss 和梯度更新。
- bigger network vs better generalization：更大网络可能降低 bias，但仍需正则化和数据。

## 相关概念

- [[forward-propagation]]
- [[backpropagation]]
- [[activation-function]]
- [[loss-function]]
- [[optimization]]

## 跨课程连接

- CS61A：神经网络是函数组合，多层结构对应组合式抽象。
- CS61B：层和计算依赖可类比图结构，训练数据需要批量组织。
- CSAPP：矩阵乘法、内存布局、cache、SIMD/GPU 向量化直接影响训练和推理速度。
- UMich DL：对应 tensor shape、Dense layer、autograd、loss、optimizer 和模型结构设计。
