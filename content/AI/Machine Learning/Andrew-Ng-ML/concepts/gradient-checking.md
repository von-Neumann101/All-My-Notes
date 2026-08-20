---
type: concept
course: Machine Learning
priority: B
status: draft
aliases: []
related: []
---

# Gradient Checking

## 一句话定义

gradient checking 是用数值近似梯度验证反向传播或自动微分实现是否正确的调试方法。当前 index.md 明确标记笔记没有系统讨论它，因此本卡只保留概念边界，公式细节需要人工补充。

## 核心思想

[[backpropagation]] 很高效，但实现复杂时容易在链式法则、矩阵转置或 broadcasting 上出错。gradient checking 的思路是不用反向传播，而是轻微扰动参数，观察 [[cost-function]] 的数值变化，再和反向传播给出的 gradient 对比。它用于调试梯度，不用于正式训练。

## 核心边界 / Objective / Assumption

设所有参数展平成 $\theta\in\mathbb{R}^p$，objective 是 $J(\theta)$，反向传播给出 $g_{backprop}\in\mathbb{R}^p$。gradient checking 比较数值梯度和解析梯度是否接近。它不改变 model form、input、output 或训练目标；它检查 optimization 信号是否可信。当前笔记只给出反向传播和自动微分线索，完整公式需要人工补充。

## 模型假设 / 局限

gradient checking 适合小模型、小 batch 和调试阶段。它不适合大规模训练循环，因为每个参数都需要额外计算 cost，复杂度很高。dropout、随机数据增强、mini-batch 随机性等会让数值比较不稳定，通常需要关闭随机项。若使用成熟框架 autograd，重点转向 tensor shape、loss 定义和数据管道检查。

## 在 Machine Learning 中的位置

它位于 [[backpropagation]] 和 [[optimization]] 之间：先确认 gradient 正确，再让 optimizer 更新参数。它与 [[gradient-descent]] 的边界是，gradient checking 只验证梯度，gradient descent 才使用梯度更新参数。

## 重要公式 / 算法

- 公式 / 算法名称：Numerical Gradient
- 解决的问题：用 cost 的有限差分近似某个参数方向的梯度。
- 核心含义：标准形式通常比较 $J(\theta+\epsilon)$ 和 $J(\theta-\epsilon)$，但当前笔记未明确给出，正式公式需要人工补充。
- 相关概念链接：[[cost-function]]、[[backpropagation]]

- 公式 / 算法名称：Gradient Difference Check
- 解决的问题：判断数值梯度和反向传播梯度是否接近。
- 核心含义：需要比较 $g_{num}$ 与 $g_{backprop}$ 的差异；阈值、范数形式和 $\epsilon$ 选择需要人工补充。
- 相关概念链接：[[optimization]]

## 容易混淆点

- gradient checking vs backpropagation：前者是调试验证，后者是训练中计算梯度的方法。
- numerical gradient vs analytic gradient：数值梯度慢但直观，解析梯度快但实现可能出错。
- gradient checking vs unit test：它测试导数一致性，不测试模型效果。
- optimization vs debugging：通过检查不代表模型会泛化，只说明梯度实现更可信。

## 相关概念

- [[backpropagation]]
- [[gradient-descent]]
- [[optimization]]
- [[cost-function]]

## 跨课程连接

- CS61A：对应用简单输入验证函数行为，再比较期望输出。
- CS61B：可用于调试复杂算法实现中的局部错误，尤其是矩阵和数组索引。
- CSAPP：有限差分受浮点误差、舍入误差和数值范围影响。
- UMich DL：对应 autograd/backpropagation 调试、tensor shape 检查和 optimizer 前的梯度验证。
