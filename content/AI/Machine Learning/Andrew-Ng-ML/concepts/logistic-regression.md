---
type: concept
course: Machine Learning
priority: A
status: draft
aliases: []
related: []
---

# Logistic Regression

## 一句话定义

logistic regression 是把线性函数接 sigmoid 后输出二分类概率的模型。它解决的是如何从特征预测 $y=1$ 的概率，而不是直接预测连续数值。

## 核心思想

[[linear-regression]] 的输出没有概率边界，不适合直接做分类。logistic regression 先计算线性 score $z=w^\top x+b$，再用 sigmoid 把它压到 $(0,1)$，从而解释为 $P(y=1|x;w,b)$，并用分类 loss 训练参数。

## 核心边界 / Objective / Assumption

单样本 model form：$f_{w,b}(x)=g(w^\top x+b)$，$g(z)=\frac{1}{1+e^{-z}}$。shape convention：$X \in \mathbb{R}^{m \times n}$，$w \in \mathbb{R}^n$，$b \in \mathbb{R}$，$z=Xw+b\mathbf{1}\in\mathbb{R}^m$，$\hat y=g(z)\in(0,1)^m$，$y\in\{0,1\}^m$。训练目标是最小化 logistic loss 或对应 cost。

## 模型假设 / 局限

它适合二分类，且假设 logit 变换后的概率可由线性函数表达。若边界非线性，可加入多项式特征或转向 [[neural-network]]；多分类通常转向 softmax；多标签分类通常使用多个 sigmoid。它输出概率，不等于最终类别，类别还需要阈值或 [[decision-boundary]]。

## 在 Machine Learning 中的位置

它位于 [[linear-regression]] 和 [[neural-network]] 之间。一个神经元可以看作类似逻辑回归的单元，因此它是理解 sigmoid、分类 loss、decision boundary 和神经网络输出层的桥梁。

## 重要公式 / 算法

- 公式 / 算法名称：Sigmoid Hypothesis
- 解决的问题：把线性 score 转成概率。
- 核心含义：$f_{w,b}(x)=\frac{1}{1+e^{-(w^\top x+b)}}$；$w,x\in\mathbb{R}^n$，输出是标量概率。
- 相关概念链接：[[classification]]、[[decision-boundary]]

- 公式 / 算法名称：Logistic Loss
- 解决的问题：惩罚二分类概率预测错误。
- 核心含义：$L(f(x),y)=-y\log(f(x))-(1-y)\log(1-f(x))$；$y\in\{0,1\}$。
- 相关概念链接：[[loss-function]]、[[cost-function]]

- 公式 / 算法名称：Gradient for Logistic Regression
- 解决的问题：用梯度下降训练参数。
- 核心含义：index.md 给出 $\frac{\partial J}{\partial w_j}=\frac{1}{m}\sum(f(x^{(i)})-y^{(i)})x_j^{(i)}$；符号为样本 $i$、特征 $j$。
- 相关概念链接：[[gradient-descent]]

## 容易混淆点

- logistic regression vs linear regression：前者输出概率，后者输出连续值。
- probability vs class：概率需要阈值才变成类别。
- sigmoid vs decision boundary：sigmoid 给概率，边界由阈值和 $w^\top x+b$ 决定。
- binary vs multiclass：二分类用 sigmoid，多分类通常用 softmax。

## 相关概念

- [[linear-regression]]
- [[classification]]
- [[decision-boundary]]
- [[loss-function]]
- [[gradient-descent]]

## 跨课程连接

- CS61A：sigmoid 是函数组合，$g(w^\top x+b)$ 是组合式抽象。
- CS61B：批量样本 $X$ 和二元标签 $y$ 需要高效组织和遍历。
- CSAPP：sigmoid 涉及 exp 计算，批量推理受浮点误差、cache 和向量化影响。
- UMich DL：对应 sigmoid 输出层、binary cross entropy、tensor shape 和 autograd。
