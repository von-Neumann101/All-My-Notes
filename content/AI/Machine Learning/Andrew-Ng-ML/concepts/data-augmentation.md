---
type: concept
course: Machine Learning
priority: C
status: draft
aliases: []
related: []
---

# Data Augmentation

## 一句话定义

data augmentation 是在不改变标签含义的前提下，对已有训练样本做合理变换来扩充数据的方法。它解决的是训练数据不足或覆盖不全时，模型容易过拟合、泛化不稳的问题。

## 核心思想

增加所有类型的数据成本很高，错误分析能指出哪些样本类型更值得补。笔记以 OCR 为例：对图像做可能真实出现的轻微扭曲或噪声，让模型看到更多同一标签下的变化。关键不是随机制造数据，而是生成“任务中合理会出现”的变化。

## 核心边界 / Objective / Assumption

无单一固定 model form，重点在训练数据变换。若图像训练集 $X\in\mathbb{R}^{m\times h\times w\times c}$、标签 $y\in\mathbb{R}^m$，augmentation 可写为 $x' = T(x)$、$y'=y$，其中 $T$ 是保持标签不变的变换。训练 objective 仍是原来的 [[loss-function]] 或 [[cost-function]]，augmentation 不直接定义新优化目标。

## 模型假设 / 局限

data augmentation 适合已知哪些输入变化不改变标签的任务，尤其是 OCR 和计算机视觉。它不适合语义容易被变换改变的场景；错误的增强会制造 label noise。它也不能解决模型太简单、loss 错误或数据分布完全不匹配的问题；这些情况通常转向模型调整、[[feature-engineering]] 或 [[transfer-learning]]。

## 在 Machine Learning 中的位置

它位于 [[overfitting]] 和 [[generalization]] 讨论之后，是提升泛化的项目级工具。它和 [[train-dev-test-split]] 的边界是：只应增强训练集，dev/test 应保持真实评估分布。

## 重要公式 / 算法

- 公式 / 算法名称：Label-preserving Transform
- 解决的问题：扩充训练样本而不改变监督信号。
- 核心含义：$x'=T(x), y'=y$；$T$ 是合理变换，$x$ 和 $x'$ shape 通常相同。
- 相关概念链接：[[supervised-learning]]

- 公式 / 算法名称：Synthetic Data
- 解决的问题：用生成或合成方式补充训练数据。
- 核心含义：笔记提到数据合成主要用于计算机视觉；具体生成方法需要人工补充。
- 相关概念链接：[[generalization]]

## 容易混淆点

- augmentation vs more data：augmentation 来自已有样本变换，新增数据来自真实采集。
- augmentation vs regularization：前者改变训练数据，后者改变训练目标或参数约束。
- augmentation vs label noise：合理增强保持标签，不合理增强会破坏标签。
- training distribution vs test distribution：增强应贴近未来真实变化。

## 相关概念

- [[overfitting]]
- [[generalization]]
- [[train-dev-test-split]]
- [[transfer-learning]]
- [[feature-engineering]]

## 跨课程连接

- CS61A：可看作对样本应用变换函数，并保持标签接口不变。
- CS61B：需要组织增强后的批量数据、索引和采样策略。
- CSAPP：图像变换和批处理会受到内存布局、cache 和向量化性能影响。
- UMich DL：连接 image augmentation、training pipeline、dataset transform 和 validation split。
