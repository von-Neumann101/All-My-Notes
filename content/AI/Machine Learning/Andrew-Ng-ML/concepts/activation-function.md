---
type: concept
course: Machine Learning
priority: B
status: draft
aliases: []
related: []
---

# Activation Function

## 一句话定义

activation function 是神经网络中施加在线性变换输出上的非线性函数。它解决的是多层网络如果只有线性变换就无法表达非线性关系的问题。

## 核心思想

每一层通常先计算 $z=w^\top x+b$ 或矩阵形式 $Z=AW+B$，再计算 $a=g(z)$。如果隐藏层都使用 linear activation，多层网络仍等价于一个线性模型；非线性激活让网络能学习更复杂的边界和表示。

## 核心边界 / Objective / Assumption

单神经元输入 $z\in\mathbb{R}$，输出 $a=g(z)$；批量输入 $Z\in\mathbb{R}^{m\times n_l}$ 时，ReLU、sigmoid、linear 通常逐元素作用并保持 shape。softmax 通常沿类别维度把 logits 转成概率分布。activation 本身不是训练 objective，但影响 gradient、optimization 和模型表达能力。

## 模型假设 / 局限

隐藏层常用 ReLU，因为 sigmoid 在某些区域变平会使梯度下降变慢。输出层激活必须匹配任务：二分类用 sigmoid，回归可用 linear 或 ReLU，多分类用 softmax。其他激活函数如 tanh、Leaky ReLU、GELU 当前笔记未覆盖，需要人工补充。

## 在 Machine Learning 中的位置

它连接 [[neural-network]] 和 [[forward-propagation]]，也是理解 [[logistic-regression]] 到神经元的桥梁。activation 决定层输出形式，并影响 [[backpropagation]] 中梯度传播。

## 重要公式 / 算法

- 公式 / 算法名称：Sigmoid
- 解决的问题：把 score 转为 $(0,1)$ 概率。
- 核心含义：$g(z)=\frac{1}{1+e^{-z}}$；常用于二分类输出层。
- 相关概念链接：[[logistic-regression]]

- 公式 / 算法名称：ReLU
- 解决的问题：提供简单非线性并减少 sigmoid flat 区域问题。
- 核心含义：$ReLU(z)=max(0,z)$；逐元素作用。
- 相关概念链接：[[neural-network]]

- 公式 / 算法名称：Softmax
- 解决的问题：把多分类 logits 转成概率分布。
- 核心含义：$a_i=\frac{e^{z_i}}{\sum_k e^{z_k}}$；$i$ 是类别索引。
- 相关概念链接：[[classification]]

## 容易混淆点

- activation vs loss：activation 生成层输出，loss 衡量预测错误。
- sigmoid vs softmax：sigmoid 常用于二分类或多标签，softmax 用于互斥多分类。
- hidden activation vs output activation：隐藏层关注表达能力，输出层必须匹配任务。
- linear activation vs no nonlinearity：隐藏层全线性会退化为线性模型。

## 相关概念

- [[neural-network]]
- [[forward-propagation]]
- [[backpropagation]]
- [[classification]]
- [[logistic-regression]]

## 跨课程连接

- CS61A：activation 是函数组合中的一层函数。
- CS61B：网络可看作节点函数组成的计算图。
- CSAPP：sigmoid/softmax 涉及 exp 和数值稳定，ReLU 更便宜，批量计算受向量化影响。
- UMich DL：对应 tensor operation、activation module、gradient flow 和 output layer design。
