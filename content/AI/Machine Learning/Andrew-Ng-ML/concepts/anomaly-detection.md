---
type: concept
course: Machine Learning
priority: B
status: draft
aliases: []
related: []
---

# Anomaly Detection

## 一句话定义

anomaly detection 是通过估计正常数据分布来识别低概率样本的方法。它解决的是未来异常可能很少、且不一定像已知异常时，如何发现可疑样本。

## 核心思想

异常检测不直接学习“异常长什么样”，而是学习正常样本的密度 $p(x)$。如果一个测试样本在该分布下概率很低，即 $p(x_{test})<\epsilon$，就把它标记为异常。

## 核心边界 / Objective / Assumption

设样本 $x\in\mathbb{R}^n$，训练集 $X\in\mathbb{R}^{m\times n}$ 多数为正常样本。高斯模型假设各特征可用均值 $\mu_i$ 和方差 $\sigma_i^2$ 估计，密度为 $p(\vec{x})=\prod_{i=1}^{n}p(x_i;\mu_i,\sigma_i^2)$。阈值 $\epsilon$ 是 hyperparameter，通常用 dev 集调整。

## 模型假设 / 局限

它适合异常样本少、未来异常类型不确定的任务。若有大量正负样本且未来异常与训练异常相似，监督分类可能更合适。它依赖特征工程：若特征不能让异常呈现低概率，模型会失败。笔记还提到特征最好接近高斯分布，非高斯特征可做变换。

## 在 Machine Learning 中的位置

它属于 [[unsupervised-learning]] 应用，和 [[classification]] 的边界很重要：异常检测把小概率事件视为可疑，而监督分类学习已知类别边界。它也连接 feature engineering、dev/test 评估和 precision/recall。

## 重要公式 / 算法

- 公式 / 算法名称：Gaussian Density Model
- 解决的问题：估计样本出现概率。
- 核心含义：$p(\vec{x})=\prod_{i=1}^{n}p(x_i;\mu_i,\sigma_i^2)$；$n$ 是特征数，$\mu_i,\sigma_i^2$ 是第 $i$ 个特征的估计参数。
- 相关概念链接：[[unsupervised-learning]]

- 公式 / 算法名称：Anomaly Threshold
- 解决的问题：把概率转成异常判断。
- 核心含义：若 $p(x_{test})<\epsilon$，则判断为异常；$\epsilon$ 是阈值。
- 相关概念链接：[[classification]]

- 公式 / 算法名称：Feature Engineering for Detection
- 解决的问题：让异常更容易表现为低概率。
- 核心含义：选择或构造能区分异常的特征；具体变换方法需要人工补充。
- 相关概念链接：[[feature-engineering]]

## 容易混淆点

- anomaly detection vs supervised classification：前者学习正常分布，后者学习类别边界。
- low probability vs wrong label：低概率表示可疑，不等同于已知类别错误。
- threshold vs parameter：$\epsilon$ 是人为选择的阈值，不是由梯度训练出的参数。
- feature scaling vs Gaussian transform：缩放调整尺度，分布变换让特征更接近高斯。

## 相关概念

- [[unsupervised-learning]]
- [[classification]]
- [[feature-engineering]]
- [[precision-recall]]

## 跨课程连接

- CS61A：异常判断可看作概率函数加阈值谓词。
- CS61B：需要组织正常样本、dev 异常样本和测试样本，涉及批量数据处理。
- CSAPP：概率连乘可能有数值下溢风险，批量密度计算受浮点和向量化影响。
- UMich DL：连接异常检测任务、数据分布、feature representation 和评估指标。
