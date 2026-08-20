---
type: concept
course: Machine Learning
priority: C
status: draft
aliases: []
related: []
---

# Softmax

## 一句话定义

softmax 是把多个类别的 logits 转换成概率分布的输出函数。它解决的是多分类任务中如何让模型在多个互斥类别之间分配概率的问题。

## 核心思想

[[logistic-regression]] 用 sigmoid 表示二分类概率；softmax 是它在互斥多分类上的推广。模型先为每个类别计算一个 score，再用指数归一化让所有类别概率非负且总和为 1。训练时通常配合 softmax loss 或 sparse categorical crossentropy。

## 核心边界 / Objective / Assumption

单样本 $x\in\mathbb{R}^n$、类别数 $K$。第 $i$ 类 logit 为 $z_i=w_i^\top x+b_i$，其中 $w_i\in\mathbb{R}^n$、$b_i\in\mathbb{R}$。softmax 输出 $a_i=\frac{e^{z_i}}{\sum_{k=1}^{K}e^{z_k}}=P(y=i|x)$。批量形式可写为 $X\in\mathbb{R}^{m\times n}$、$W\in\mathbb{R}^{n\times K}$、$b\in\mathbb{R}^{K}$、$Z=XW+b$、$A\in\mathbb{R}^{m\times K}$。training objective 通常最小化正确类别的 negative log probability。

## 模型假设 / 局限

softmax 适合单标签、多类别、类别互斥的分类任务。不适合多标签任务，因为多标签中多个类别可以同时为真，通常要用多个 sigmoid。softmax 中 exp 可能带来数值稳定性问题；笔记建议把 sigmoid/softmax 直接整合到 loss 计算中，尤其是 softmax。更完整的 log-sum-exp 推导需要人工补充。

## 在 Machine Learning 中的位置

它连接 [[classification]]、[[activation-function]] 和 [[loss-function]]。在神经网络中，softmax 常作为输出层 activation；在训练中，softmax loss 把多分类概率变成可优化的错误信号。

## 重要公式 / 算法

- 公式 / 算法名称：Softmax Activation
- 解决的问题：把多类 logits 转换为概率分布。
- 核心含义：$a_i=\frac{e^{z_i}}{\sum_k e^{z_k}}$；$z_i$ 是第 $i$ 类 logit，$a_i$ 是第 $i$ 类概率。
- 相关概念链接：[[activation-function]]

- 公式 / 算法名称：Softmax Loss
- 解决的问题：惩罚正确类别概率过低的多分类预测。
- 核心含义：$loss=-\ln(a_i)$ when $y=i$；$i$ 是真实类别索引，$a_i$ 是该类别概率。
- 相关概念链接：[[loss-function]]

- 公式 / 算法名称：Numerically Stable Softmax
- 解决的问题：减少 exp 溢出和 log 计算不稳定。
- 核心含义：笔记建议把 softmax 和 loss 整合计算；稳定实现细节需要人工补充。
- 相关概念链接：[[optimization]]

## 容易混淆点

- softmax vs sigmoid：softmax 用于互斥多分类，sigmoid 可用于二分类或多标签。
- logits vs probabilities：logits 是未归一化 score，softmax 后才是概率。
- softmax activation vs softmax loss：前者产生概率，后者定义训练惩罚。
- multiclass vs multilabel：多分类选一个类别，多标签可同时选多个类别。

## 相关概念

- [[classification]]
- [[activation-function]]
- [[loss-function]]
- [[neural-network]]
- [[optimization]]

## 跨课程连接

- CS61A：softmax 是函数组合：线性 score、指数变换、归一化。
- CS61B：批量多分类输出需要按矩阵和类别维组织 logits 与标签。
- CSAPP：exp、log、浮点溢出、内存布局和向量化影响 softmax loss 的稳定性与性能。
- UMich DL：对应 logits、SparseCategoricalCrossentropy、tensor shape 和 fused loss 实现。
