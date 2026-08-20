---
type: concept
course: Machine Learning
priority: A
status: draft
aliases: []
related: []
---

# Decision Boundary

## 一句话定义

decision boundary 是分类模型把特征空间划分为不同类别的边界。它解决的是概率或 score 如何转化为最终类别区域的问题。

## 核心思想

分类模型通常输出概率或 score，真正的类别来自阈值规则。对于 [[logistic-regression]]，当阈值是 $0.5$ 时，sigmoid 的分界等价于线性 score $w^\top x+b=0$，因此边界可以从模型参数中直接读出几何含义。

## 核心边界 / Objective / Assumption

decision boundary 本身不是训练 objective，它是训练后模型和阈值共同决定的分类面。二分类 logistic regression 中，$x,w\in\mathbb{R}^n$，$z=w^\top x+b$，若 $g(z)\ge 0.5$ 预测为 1，则边界为 $z=0$。批量时 $X\in\mathbb{R}^{m\times n}$，$z=Xw+b\mathbf{1}\in\mathbb{R}^m$。

## 模型假设 / 局限

线性模型给出线性 decision boundary。若真实类别边界非线性，可以加入多项式特征、做特征工程，或转向 [[neural-network]]。边界还依赖阈值选择；在类别不平衡任务中，默认 $0.5$ 阈值可能不合适，需要结合 precision/recall。

## 在 Machine Learning 中的位置

它连接 [[classification]] 和 [[logistic-regression]]：模型输出概率，decision boundary 给出类别划分。继续向后，它帮助理解多项式特征、神经网络非线性表达和分类器可视化。

## 重要公式 / 算法

- 公式 / 算法名称：Logistic Regression Boundary
- 解决的问题：从概率阈值得到分类边界。
- 核心含义：$f_{w,b}(x)\ge 0.5 \Leftrightarrow w^\top x+b\ge 0$；$w,x\in\mathbb{R}^n$。
- 相关概念链接：[[logistic-regression]]

- 公式 / 算法名称：Linear Decision Boundary
- 解决的问题：描述线性分类面的几何形状。
- 核心含义：$w^\top x+b=0$ 是特征空间中的超平面；二维时是直线。
- 相关概念链接：[[classification]]

- 公式 / 算法名称：Nonlinear Boundary via Features
- 解决的问题：表达非线性分类区域。
- 核心含义：index.md 提到可向 sigmoid 输入多项式特征形成非线性边界；具体构造需要人工补充。
- 相关概念链接：[[feature-engineering]]

## 容易混淆点

- decision boundary vs sigmoid：sigmoid 输出概率，boundary 是分类分界。
- score vs probability：$z$ 是线性 score，$g(z)$ 才是概率。
- boundary vs loss：boundary 用于分类解释，loss 用于训练。
- linear boundary vs nonlinear boundary：非线性边界通常来自特征变换或神经网络。

## 相关概念

- [[classification]]
- [[logistic-regression]]
- [[loss-function]]
- [[feature-engineering]]

## 跨课程连接

- CS61A：阈值判断对应谓词函数和条件分支。
- CS61B：边界可类比空间划分，复杂模型涉及更复杂的数据分区。
- CSAPP：边界附近的浮点误差可能影响分类结果，批量判断受向量化性能影响。
- UMich DL：分类器可视化、logits、sigmoid/softmax 输出和 decision surface。
