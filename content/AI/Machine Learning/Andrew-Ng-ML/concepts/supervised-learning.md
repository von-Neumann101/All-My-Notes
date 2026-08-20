---
type: concept
course: Machine Learning
priority: A
status: draft
aliases: []
related: []
---

# Supervised Learning

## 一句话定义

监督学习是在给定输入特征和正确标签的情况下，学习从 $x$ 到 $y$ 的映射。它解决的是如何用带答案的数据训练模型，并让模型泛化到未见样本。

## 核心思想

监督学习需要标签，因为模型必须知道预测 $\hat y$ 和真实标签 $y$ 的差距，才能通过 [[loss-function]]、[[cost-function]] 和 [[gradient-descent]] 改进参数。它的目标不是记住训练集，而是在训练样本中学习可迁移到新数据的规律。

## 核心边界 / Objective / Assumption

数据通常写成 $X \in \mathbb{R}^{m \times n}$，其中 $m$ 是样本数，$n$ 是特征数；第 $i$ 个样本是 $x^{(i)} \in \mathbb{R}^n$；标签向量是 $y \in \mathbb{R}^m$，分类时也可取离散类别。模型 $f_\theta$ 接收 $x$ 并输出 $\hat y=f_\theta(x)$。训练目标是让预测和标签的差距在训练集上尽量小，同时希望在新数据上仍然有效。

## 模型假设 / 局限

监督学习适用于有可靠标签、训练分布和未来测试分布相近的任务。不适用于没有标签、只想发现数据结构的场景，此时通常转向 [[unsupervised-learning]]；也不适用于奖励延迟的序列决策问题，此时通常转向 [[reinforcement-learning]]。如果训练集标签噪声很大或分布偏移严重，需要人工补充更具体的处理方法。

## 在 Machine Learning 中的位置

监督学习是这组笔记的入口：[[supervised-learning]] → [[linear-regression]] → [[loss-function]] → [[cost-function]] → [[gradient-descent]]。它再向分类任务扩展到 [[logistic-regression]]，并进一步连接到 [[neural-network]]。

## 重要公式 / 算法

- 公式 / 算法名称：监督学习预测框架
- 解决的问题：从输入特征预测标签。
- 核心含义：$\hat y^{(i)}=f_\theta(x^{(i)})$，其中 $\theta$ 是模型参数，$x^{(i)}$ 是单个样本，$\hat y^{(i)}$ 是预测。
- 相关概念链接：[[loss-function]]、[[cost-function]]

- 公式 / 算法名称：训练集矩阵表示
- 解决的问题：批量表示训练样本。
- 核心含义：$X \in \mathbb{R}^{m \times n}$，$y \in \mathbb{R}^m$；每一行对应一个样本，每一列对应一个特征。
- 相关概念链接：[[linear-regression]]、[[feature-scaling]]

## 容易混淆点

- supervised learning vs unsupervised learning：前者有标签，后者没有标签。
- supervised learning vs reinforcement learning：前者学习输入到答案，后者学习状态到动作。
- regression vs classification：回归输出连续值，分类输出离散类别。
- training error vs generalization error：训练集误差低不等于新数据表现好。

## 相关概念

- [[linear-regression]]
- [[classification]]
- [[loss-function]]
- [[cost-function]]
- [[gradient-descent]]

## 跨课程连接

- CS61A：模型 $f_\theta(x)$ 可对应函数抽象；训练过程可看作反复改进函数行为。
- CS61B：$X \in \mathbb{R}^{m \times n}$ 是批量样本的数据组织问题，涉及数组、表和批处理。
- CSAPP：大规模训练会受到浮点表示、内存布局、cache 和向量化性能影响。
- UMich DL：监督学习是 tensor shape、loss、optimizer 和 autograd 的基本使用场景。
