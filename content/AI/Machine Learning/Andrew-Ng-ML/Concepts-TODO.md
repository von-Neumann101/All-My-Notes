# Machine Learning Concepts TODO

## 1. 高优先级概念 A

### [[supervised-learning]]

- 推荐文件名：supervised-learning.md
- 来源：Machine Learning
- 优先级：A
- 为什么重要：这是回归、分类、神经网络训练和模型评估的共同起点，后续深度学习、计算机视觉、机器人和强化学习都会反复对比“有标签学习”和其他学习范式。
- 核心问题：在给定正确答案的情况下，如何学习从输入到输出的映射？
- 应该包含的内容：监督学习定义；回归与分类；输入、标签、预测函数；训练集和测试集；与无监督学习、强化学习的区别。
- 相关公式 / 算法：$f(x)\to y$ 的预测框架；线性回归；逻辑回归。
- 相关课程连接：
  - CS61A：函数抽象、输入输出映射、组合式问题分解。
  - CS61B：数据集、样本集合、分类任务中的数据组织。
  - CSAPP：数值表示和程序性能会影响模型训练实现。
  - UMich DL：深度学习训练默认建立在监督学习框架上。
- 需要人工补充：可补充监督学习、无监督学习、强化学习的系统对照表。

### [[linear-regression]]

- 推荐文件名：linear-regression.md
- 来源：Machine Learning
- 优先级：A
- 为什么重要：线性回归是最基础的参数化模型，连接假设函数、代价函数、梯度下降、向量化和正则化。
- 核心问题：如何用线性函数预测连续数值？
- 应该包含的内容：单变量线性回归；多特征线性回归；参数 $w,b$；假设函数；向量化；正规方程的线索。
- 相关公式 / 算法：$f_{w,b}(x)=wx+b$；$f_{\boldsymbol{w},b}(\boldsymbol{x})=\boldsymbol{w}\boldsymbol{x}+b$；$A^TA\hat{x}=A^TB$。
- 相关课程连接：
  - CS61A：函数、抽象和简单模型。
  - CS61B：用数组和矩阵组织特征数据。
  - CSAPP：浮点数、矩阵运算性能、数值稳定性。
  - UMich DL：线性层和神经网络中的仿射变换。
- 需要人工补充：正规方程的适用条件、矩阵形式推导和数值稳定性。

### [[cost-function]]

- 推荐文件名：cost-function.md
- 来源：Machine Learning
- 优先级：A
- 为什么重要：cost function 是训练目标的统一表达，贯穿线性回归、逻辑回归、神经网络、K-means 和推荐系统。
- 核心问题：如何把“模型好不好”变成可优化的数值目标？
- 应该包含的内容：cost function 与 loss function 的区别；平方误差；正则化项；不同任务中的目标函数；训练目标最小化。
- 相关公式 / 算法：$J(w,b)=\frac{1}{2m}\sum_{i=1}^{m}(f_{w,b}(x^{(i)})-y^{(i)})^2$；K-means 失真函数；推荐系统 cost function。
- 相关课程连接：
  - CS61A：把问题抽象成目标函数。
  - CS61B：数据结构支持高效计算目标函数。
  - CSAPP：循环、向量化和矩阵运算性能。
  - UMich DL：loss landscape、训练目标和优化。
- 需要人工补充：不同任务中 cost、loss、objective 的术语边界。

### [[gradient-descent]]

- 推荐文件名：gradient-descent.md
- 来源：Machine Learning
- 优先级：A
- 为什么重要：梯度下降是从目标函数到参数更新的核心机制，后续深度学习训练和强化学习函数近似都会反复使用。
- 核心问题：如何沿着降低代价函数的方向更新参数？
- 应该包含的内容：学习率 $\alpha$；偏导；同步更新；batch 梯度下降；收敛检查；与反向传播的区别。
- 相关公式 / 算法：$w_{new}=w-\alpha\frac{\partial}{\partial w}J(w,b)$；$b_{new}=b-\alpha\frac{\partial}{\partial b}J(w,b)$。
- 相关课程连接：
  - CS61A：迭代改进过程。
  - CS61B：大规模数据上的迭代算法。
  - CSAPP：性能优化、向量化、缓存行为。
  - UMich DL：神经网络训练、optimizer、mini-batch。
- 需要人工补充：随机梯度下降、mini-batch 梯度下降和收敛条件的系统整理。

### [[feature-scaling]]

- 推荐文件名：feature-scaling.md
- 来源：Machine Learning
- 优先级：A
- 为什么重要：特征尺度直接影响梯度下降的收敛速度，也是理解 normalization、preprocessing 和深度学习输入处理的基础。
- 核心问题：为什么不同量纲的特征会让优化变慢，如何处理？
- 应该包含的内容：最大值归一化；均值归一化；Z-score 归一化；特征尺度对等高线和收敛的影响。
- 相关公式 / 算法：$\frac{x}{max}$；$\frac{x-\bar{x}}{max-min}$；$\frac{x-\bar{x}}{\sigma}$。
- 相关课程连接：
  - CS61A：数据变换函数。
  - CS61B：批量数据预处理。
  - CSAPP：数值范围和浮点计算。
  - UMich DL：输入标准化、batch normalization 的前置概念。
- 需要人工补充：feature scaling、normalization、standardization 的术语区分。

### [[logistic-regression]]

- 推荐文件名：logistic-regression.md
- 来源：Machine Learning
- 优先级：A
- 为什么重要：逻辑回归是从回归过渡到分类和神经元模型的关键桥梁，后续 sigmoid、交叉熵和二分类网络都依赖它。
- 核心问题：如何把线性函数转化为类别概率？
- 应该包含的内容：sigmoid；概率解释；二分类；逻辑回归损失；决策边界；与线性回归的区别。
- 相关公式 / 算法：$g(z)=\frac{1}{1+e^{-z}}$；$f_{\boldsymbol{w},b}(\boldsymbol{x})=g(\boldsymbol{w}\boldsymbol{x}+b)$。
- 相关课程连接：
  - CS61A：函数组合和条件判断。
  - CS61B：分类数据的表示。
  - CSAPP：指数函数计算和数值稳定性。
  - UMich DL：神经元、sigmoid 输出层、binary classification。
- 需要人工补充：最大似然推导和标准交叉熵公式。

### [[classification]]

- 推荐文件名：classification.md
- 来源：Machine Learning
- 优先级：A
- 为什么重要：分类是机器学习长期核心任务，连接逻辑回归、softmax、多标签分类、precision/recall 和实际模型评估。
- 核心问题：如何从输入预测离散类别？
- 应该包含的内容：二分类；多分类；多标签分类；positive/negative class；分类阈值；类别不平衡评价。
- 相关公式 / 算法：sigmoid 二分类；softmax 多分类；precision、recall、F1-score。
- 相关课程连接：
  - CS61A：谓词、条件分支和离散输出。
  - CS61B：类别标签、集合和映射。
  - CSAPP：批量推理程序性能。
  - UMich DL：图像分类、多标签识别、分类损失。
- 需要人工补充：多分类和多标签分类的标准评价指标。

### [[decision-boundary]]

- 推荐文件名：decision-boundary.md
- 来源：Machine Learning
- 优先级：A
- 为什么重要：决策边界把概率输出和最终类别连接起来，是理解分类模型几何意义的核心。
- 核心问题：模型如何把特征空间划分为不同类别区域？
- 应该包含的内容：阈值 0.5；线性决策边界；非线性决策边界；多项式特征对边界形状的影响。
- 相关公式 / 算法：$f_{\boldsymbol{w},b}(\boldsymbol{x})\ge 0.5$；$\boldsymbol{w}\boldsymbol{x}+b\ge 0$；$\boldsymbol{w}\boldsymbol{x}+b=0$。
- 相关课程连接：
  - CS61A：条件判断和谓词函数。
  - CS61B：空间划分和搜索结构的类比。
  - CSAPP：数值误差可能影响边界附近判断。
  - UMich DL：分类器可视化、线性层和非线性边界。
- 需要人工补充：多分类场景中的决策边界。

### [[regularization]]

- 推荐文件名：regularization.md
- 来源：Machine Learning
- 优先级：A
- 为什么重要：正则化是控制过拟合、提升泛化能力的通用机制，在经典模型和深度学习中都反复出现。
- 核心问题：如何限制模型复杂度，使模型不只记住训练集？
- 应该包含的内容：过拟合动机；L2 正则化；正则化参数 $\lambda$；不正则化 $b$ 的常见约定；权重衰减直觉。
- 相关公式 / 算法：$J(w,b)+\frac{\lambda}{2m}\sum_{j=1}^{n}w_j^2$；$w_{new}=(1-\alpha\frac{\lambda}{m})w-\alpha\cdots$。
- 相关课程连接：
  - CS61A：约束和惩罚项的抽象。
  - CS61B：模型复杂度与数据规模。
  - CSAPP：计算成本和模型规模。
  - UMich DL：weight decay、神经网络正则化、generalization。
- 需要人工补充：L1、dropout、early stopping 等其他正则化方法。

### [[bias-variance]]

- 推荐文件名：bias-variance.md
- 来源：Machine Learning
- 优先级：A
- 为什么重要：偏差方差是诊断模型表现和决定下一步工作的核心框架。
- 核心问题：模型表现差时，是模型太简单、数据不够，还是泛化不好？
- 应该包含的内容：高偏差；高方差；$J_{train}$、$J_{cv}$、$J_{test}$；基准性能水平；学习曲线；下一步行动。
- 相关公式 / 算法：用训练集、dev 集和测试集误差比较诊断；高方差增加数据或减少特征；高偏差增加特征或模型复杂度。
- 相关课程连接：
  - CS61A：抽象层级过强或过弱的类比。
  - CS61B：数据规模和算法选择。
  - CSAPP：模型规模与计算资源约束。
  - UMich DL：generalization、model selection、regularization。
- 需要人工补充：bias-variance decomposition 的数学公式。

### [[train-dev-test-split]]

- 推荐文件名：train-dev-test-split.md
- 来源：Machine Learning
- 优先级：A
- 为什么重要：这是模型选择和泛化评估的基本协议，能避免用测试集调模型造成过乐观估计。
- 核心问题：如何把数据划分给训练、调参和最终评估？
- 应该包含的内容：训练集；dev/cross-validation 集；测试集；模型选择；泛化误差估计；不要用测试集选模型。
- 相关公式 / 算法：训练集 60%、dev 集 20%、测试集 20% 的示例；$J_{train}$、$J_{cv}$、$J_{test}$。
- 相关课程连接：
  - CS61A：实验设计和函数验证。
  - CS61B：数据集合划分和抽样。
  - CSAPP：批处理实验和性能测量方法。
  - UMich DL：validation set、test set、model selection。
- 需要人工补充：交叉验证和数据泄漏的更多例子。

### [[neural-network]]

- 推荐文件名：neural-network.md
- 来源：Machine Learning
- 优先级：A
- 为什么重要：神经网络是深度学习、计算机视觉、VLA、机器人和深度强化学习的基础模型。
- 核心问题：如何通过多层可学习变换从数据中自动学习特征？
- 应该包含的内容：神经元；层；隐藏层；输出层；Dense Layer；神经网络和逻辑回归的关系；自动特征学习。
- 相关公式 / 算法：每个神经元类似逻辑回归；逐层计算激活值；`Sequential` 和 `Dense` 实现线索。
- 相关课程连接：
  - CS61A：函数组合和抽象层。
  - CS61B：图结构、层结构和数据流。
  - CSAPP：矩阵计算、并行性、内存访问。
  - UMich DL：深度学习核心。
- 需要人工补充：网络深度、宽度、参数数量和表达能力的系统关系。

### [[forward-propagation]]

- 推荐文件名：forward-propagation.md
- 来源：Machine Learning
- 优先级：A
- 为什么重要：前向传播是神经网络推理的基本过程，也是反向传播和计算图的前提。
- 核心问题：输入如何经过每一层变成预测输出？
- 应该包含的内容：层输入和层输出；激活值；矩阵乘法；向量化；输出层激活选择。
- 相关公式 / 算法：$A^TW+B$ 后接激活函数；sigmoid、ReLU、linear、softmax。
- 相关课程连接：
  - CS61A：函数组合。
  - CS61B：图上的数据流。
  - CSAPP：矩阵乘法性能、向量化。
  - UMich DL：inference、computation graph、model architecture。
- 需要人工补充：标准符号 $Z^{[l]}$、$A^{[l]}$、$W^{[l]}$、$b^{[l]}$。

### [[backpropagation]]

- 推荐文件名：backpropagation.md
- 来源：Machine Learning
- 优先级：A
- 为什么重要：反向传播是训练神经网络的核心机制，后续深度学习、视觉模型和深度强化学习都会用到。
- 核心问题：如何高效计算所有参数对损失的梯度？
- 应该包含的内容：计算图；链式法则；从右向左计算偏导；与梯度下降的关系；TensorFlow `fit` 和自动微分。
- 相关公式 / 算法：反向传播一次从右向左得到所有偏导；具体链式法则公式需要人工补充。
- 相关课程连接：
  - CS61A：递归、函数组合、求值过程。
  - CS61B：图遍历和依赖关系。
  - CSAPP：自动微分实现的内存和性能成本。
  - UMich DL：neural network training、autograd。
- 需要人工补充：完整链式法则推导、矩阵维度检查、gradient checking。

### [[loss-function]]

- 推荐文件名：loss-function.md
- 来源：Machine Learning
- 优先级：A
- 为什么重要：loss function 是单样本错误的度量，是 cost function、反向传播和优化的直接基础。
- 核心问题：单个预测错了多少，应该如何惩罚？
- 应该包含的内容：loss 与 cost 区别；平方误差 loss；逻辑回归 loss；binary crossentropy；softmax loss。
- 相关公式 / 算法：$L=\frac12(f(x)-y)^2$；逻辑回归损失；$loss=-\ln(a_i)$ when $y=i$。
- 相关课程连接：
  - CS61A：局部错误度量函数。
  - CS61B：逐样本计算和聚合。
  - CSAPP：数值稳定性和 log/exp 计算。
  - UMich DL：loss design、classification loss、regression loss。
- 需要人工补充：交叉熵标准公式和数值稳定实现。

### [[optimization]]

- 推荐文件名：optimization.md
- 来源：Machine Learning
- 优先级：A
- 为什么重要：优化把目标函数转化为可执行的训练过程，连接梯度下降、Adam、自动微分、mini-batch 和强化学习更新。
- 核心问题：如何有效找到让目标函数更好的参数？
- 应该包含的内容：梯度下降；学习率；Adam；GradientTape；mini-batch；soft update；优化和泛化的边界。
- 相关公式 / 算法：梯度下降更新；Adam 作为自适应学习率算法；`tf.GradientTape()` 自动微分。
- 相关课程连接：
  - CS61A：迭代改进。
  - CS61B：算法效率和数据批处理。
  - CSAPP：性能优化、并行计算、浮点误差。
  - UMich DL：optimizer、training dynamics。
- 需要人工补充：Adam 的动量和二阶矩公式、optimizer 选择原则。

### [[overfitting]]

- 推荐文件名：overfitting.md
- 来源：Machine Learning
- 优先级：A
- 为什么重要：过拟合是模型训练中最常见的失败模式之一，直接关联泛化、正则化、数据量和模型复杂度。
- 核心问题：为什么模型训练集表现很好，但对新数据表现差？
- 应该包含的内容：过拟合表现；增加数据；减少无关特征；正则化；高方差；dev/test 诊断。
- 相关公式 / 算法：正则化项 $\frac{\lambda}{2m}\sum w_j^2$；用 $J_{train}$ 和 $J_{cv}$ 诊断。
- 相关课程连接：
  - CS61A：过度拟合样例的规则。
  - CS61B：数据规模和模型复杂度。
  - CSAPP：更大模型带来的资源成本。
  - UMich DL：generalization、regularization、data augmentation。
- 需要人工补充：过拟合的可视化例子和与 high variance 的严格关系。

### [[underfitting]]

- 推荐文件名：underfitting.md
- 来源：Machine Learning
- 优先级：A
- 为什么重要：欠拟合是过拟合的对应概念，和高偏差诊断、模型容量选择紧密相关。
- 核心问题：为什么模型连训练集都拟合不好？
- 应该包含的内容：欠拟合定义；高偏差；模型太简单；增加特征；增加多项式特征；更大网络。
- 相关公式 / 算法：通过 $J_{train}$ 高来识别；与基准性能水平对比。
- 相关课程连接：
  - CS61A：抽象太粗导致表达能力不足。
  - CS61B：算法或数据表示不足。
  - CSAPP：资源限制下模型容量受限。
  - UMich DL：high bias、model capacity。
- 需要人工补充：index.md 标明 underfitting 没有被笔记系统展开，需要补充标准定义和例子。

## 2. 中优先级概念 B

### [[activation-function]]

- 推荐文件名：activation-function.md
- 来源：Machine Learning
- 优先级：B
- 为什么重要：激活函数让神经网络具备非线性表达能力，是从线性模型到深度模型的关键。
- 核心问题：为什么神经网络不能每层都只用线性函数？
- 应该包含的内容：sigmoid；ReLU；linear；softmax；输出层与隐藏层的不同选择；sigmoid flat 区域。
- 相关公式 / 算法：$ReLU(z)=max(0,z)$；$g(z)=\frac{1}{1+e^{-z}}$；softmax。
- 相关课程连接：
  - CS61A：函数组合。
  - CS61B：无直接核心连接，可联系图上的节点函数。
  - CSAPP：函数计算成本和数值稳定性。
  - UMich DL：深度网络结构与训练。
- 需要人工补充：tanh、Leaky ReLU、GELU 等当前笔记未覆盖的激活函数。

### [[gradient-checking]]

- 推荐文件名：gradient-checking.md
- 来源：Machine Learning
- 优先级：B
- 为什么重要：它是验证反向传播实现是否正确的重要方法，适合在实现神经网络时单独整理。
- 核心问题：如何确认反向传播算出的梯度没有错？
- 应该包含的内容：数值梯度；解析梯度；有限差分；梯度误差比较；什么时候使用。
- 相关公式 / 算法：需要人工补充。当前 index.md 只说明笔记没有明确讨论 gradient checking。
- 相关课程连接：
  - CS61A：测试函数输出是否符合预期。
  - CS61B：调试复杂算法实现。
  - CSAPP：浮点误差会影响数值梯度检查。
  - UMich DL：反向传播调试。
- 需要人工补充：完整公式和示例。

### [[learning-rate]]

- 推荐文件名：learning-rate.md
- 来源：Machine Learning
- 优先级：B
- 为什么重要：学习率 $\alpha$ 控制每次参数更新步长，是优化能否收敛的关键超参数。
- 核心问题：更新太大或太小会怎样影响训练？
- 应该包含的内容：$\alpha$ 在梯度下降中的位置；收敛检查；学习曲线；与 Adam 的关系。
- 相关公式 / 算法：$w_{new}=w-\alpha\frac{\partial J}{\partial w}$。
- 相关课程连接：
  - CS61A：迭代过程的步长。
  - CS61B：迭代算法调参。
  - CSAPP：训练时间和资源消耗。
  - UMich DL：optimizer、learning rate schedule。
- 需要人工补充：学习率过大震荡、过小收敛慢的图示和调参策略。

### [[normalization]]

- 推荐文件名：normalization.md
- 来源：Machine Learning
- 优先级：B
- 为什么重要：normalization 是机器学习数据预处理的通用概念，当前笔记中既出现在特征放缩，也出现在推荐系统均值归一化。
- 核心问题：为什么要改变数据尺度或中心位置？
- 应该包含的内容：最大值归一化；均值归一化；Z-score；推荐系统均值归一化；与 regularization 的区别。
- 相关公式 / 算法：$\frac{x-\bar{x}}{max-min}$；$\frac{x-\bar{x}}{\sigma}$；评分矩阵减去 $\mu_i$。
- 相关课程连接：
  - CS61A：数据变换。
  - CS61B：批量处理数据集合。
  - CSAPP：数值范围和浮点精度。
  - UMich DL：input normalization、batch normalization 的前置概念。
- 需要人工补充：normalization、standardization、feature scaling 的命名边界。

### [[k-means]]

- 推荐文件名：k-means.md
- 来源：Machine Learning
- 优先级：B
- 为什么重要：K-means 是无监督学习中最基础的聚类算法，目标函数和迭代过程都清晰。
- 核心问题：没有标签时，如何按距离结构把数据分组？
- 应该包含的内容：聚类中心；样本分配；中心更新；失真函数；初始化；elbow method。
- 相关公式 / 算法：$J=\frac{1}{m}\sum^m_{i=1}\lVert x^{(i)}-\mu_{c^{(i)}} \rVert^2$。
- 相关课程连接：
  - CS61A：迭代更新过程。
  - CS61B：集合、最近邻搜索、聚类数据结构。
  - CSAPP：距离计算和批量矩阵运算性能。
  - UMich DL：无监督表示学习的前置概念。
- 需要人工补充：K-means++ 和距离度量选择。

### [[principal-component-analysis]]

- 推荐文件名：principal-component-analysis.md
- 来源：Machine Learning
- 优先级：B
- 为什么重要：PCA 是理解降维、投影、重构和可视化的核心工具。
- 核心问题：如何在尽量保留信息的同时降低特征维度？
- 应该包含的内容：主成分；最大化投影方差；最小化重构误差；投影；重构；归一化预处理。
- 相关公式 / 算法：投影到主成分；用投影长度乘单位向量重构；通用矩阵公式需要补充。
- 相关课程连接：
  - CS61A：抽象和信息压缩。
  - CS61B：高维数据表示。
  - CSAPP：矩阵运算和数值计算。
  - UMich DL：embedding、representation、可视化。
- 需要人工补充：协方差矩阵、特征向量、SVD 和 explained variance。

### [[anomaly-detection]]

- 推荐文件名：anomaly-detection.md
- 来源：Machine Learning
- 优先级：B
- 为什么重要：异常检测是无监督或半监督场景中的重要应用，和密度估计、特征工程、评估方法都相关。
- 核心问题：如何识别低概率或不寻常的数据点？
- 应该包含的内容：密度估计；高斯模型；阈值 $\epsilon$；dev/test 评估；与监督分类的区别；特征选择。
- 相关公式 / 算法：$p(\vec{x})=\prod^n_{i=1}p(x_i;\mu_i,\sigma_i^2)$；$p(x_{test})<\epsilon$。
- 相关课程连接：
  - CS61A：概率判断函数。
  - CS61B：异常样本集合和检索。
  - CSAPP：数值下溢和概率乘积。
  - UMich DL：异常检测和数据分布。
- 需要人工补充：多元高斯模型和评价指标细节。

### [[recommender-system]]

- 推荐文件名：recommender-system.md
- 来源：Machine Learning
- 优先级：B
- 为什么重要：推荐系统连接协同过滤、内容过滤、embedding、向量相似度和大规模检索排序。
- 核心问题：如何预测用户对未见物品的偏好？
- 应该包含的内容：用户 item 评分矩阵；协同过滤；均值归一化；内容过滤；相似物品查找；检索与排序。
- 相关公式 / 算法：协同过滤 cost function；$v_u^{(j)}\cdot v_m^{(i)}$；向量差 L2 范数平方。
- 相关课程连接：
  - CS61A：映射关系和函数组合。
  - CS61B：哈希表、图、检索、排序。
  - CSAPP：大规模系统性能和预计算。
  - UMich DL：embedding、two-tower model、ranking。
- 需要人工补充：召回、排序、负采样和线上评估。

### [[collaborative-filtering]]

- 推荐文件名：collaborative-filtering.md
- 来源：Machine Learning
- 优先级：B
- 为什么重要：协同过滤是推荐系统的核心算法之一，展示了如何从评分关系中学习潜在特征。
- 核心问题：没有显式 item 特征时，如何只从用户评分学习偏好和物品表示？
- 应该包含的内容：$r(i,j)$；$y^{(i,j)}$；用户参数；item 特征；联合学习；冷启动问题。
- 相关公式 / 算法：$J(w,b,x)=\frac12\sum_{(i,j):r(i,j)=1}(w^{(j)}\cdot x^{(i)}+b^{(j)}-y^{(i,j)})^2+\cdots$。
- 相关课程连接：
  - CS61A：二维关系映射。
  - CS61B：稀疏矩阵、图关系、检索。
  - CSAPP：稀疏数据和矩阵计算性能。
  - UMich DL：embedding 和 representation learning。
- 需要人工补充：矩阵分解视角和旋转不变性的更清晰解释。

### [[reinforcement-learning]]

- 推荐文件名：reinforcement-learning.md
- 来源：Machine Learning
- 优先级：B
- 为什么重要：强化学习把学习问题从静态预测扩展到序列决策，是机器人、VLA 和智能体系统的重要基础。
- 核心问题：智能体如何通过奖励学习长期更好的行动策略？
- 应该包含的内容：状态；动作；奖励；return；policy；Q-function；Bellman Equation；DQN。
- 相关公式 / 算法：$\pi:s\to a$；$G_t=\sum_{k=0}^{\infty}\gamma^kR_{t+k+1}$；$Q(s,a)=R(s)+\gamma\max_{a'}Q(s',a')$。
- 相关课程连接：
  - CS61A：状态转移、递归决策。
  - CS61B：图搜索、状态空间。
  - CSAPP：仿真和训练系统性能。
  - UMich DL：deep RL、policy/value methods。
- 需要人工补充：agent-environment loop、$V(s)$、model-free 与 model-based 的区别。

### [[policy]]

- 推荐文件名：policy.md
- 来源：Machine Learning
- 优先级：B
- 为什么重要：policy 是强化学习中从状态到动作的核心对象，也是序列决策的直接产物。
- 核心问题：在当前状态下应该选择哪个动作？
- 应该包含的内容：$\pi:s\to a$；最优策略 $\pi^*$；policy 与 value function 的区别；epsilon-greedy。
- 相关公式 / 算法：$\arg_a \max Q(s,a)$；$1-\epsilon$ 选择最优动作，$\epsilon$ 随机探索。
- 相关课程连接：
  - CS61A：策略函数和条件选择。
  - CS61B：状态空间中的动作选择。
  - CSAPP：策略执行的系统成本。
  - UMich DL：policy learning、actor-critic 的前置概念。
- 需要人工补充：随机策略和确定性策略的定义。

### [[q-learning]]

- 推荐文件名：q-learning.md
- 来源：Machine Learning
- 优先级：B
- 为什么重要：Q-learning 连接 Bellman 方程、价值函数近似、DQN 和探索策略，是深度强化学习的重要入口。
- 核心问题：如何学习每个状态动作对的长期价值？
- 应该包含的内容：Q-function；Bellman target；DQN；replay buffer；mini-batch；soft update；epsilon-greedy。
- 相关公式 / 算法：$Q(s,a)=R(s)+\gamma\max_{a'}Q(s',a')$；$x=(s,a)$；$y=R(s)+\gamma\max_{a'}Q(s',a')$。
- 相关课程连接：
  - CS61A：递归定义和固定点迭代。
  - CS61B：图上的动态规划和状态搜索。
  - CSAPP：训练循环和内存 buffer 性能。
  - UMich DL：DQN、deep RL。
- 需要人工补充：tabular Q-learning 更新式、target network、off-policy 概念。

## 3. 低优先级概念 C

- [[softmax]]
  - 推荐文件名：softmax.md
  - 为什么暂时是 C：当前可以先放在 [[activation-function]]、[[classification]] 和 [[loss-function]] 中整理。
  - 未来什么时候需要整理：开始系统学习多分类神经网络或视觉分类模型时。

- [[precision-recall]]
  - 推荐文件名：precision-recall.md
  - 为什么暂时是 C：它重要，但属于分类评估专题，不影响主干概念搭建。
  - 未来什么时候需要整理：处理类别不平衡、医学诊断、异常检测或检索排序任务时。

- [[decision-tree]]
  - 推荐文件名：decision-tree.md
  - 为什么暂时是 C：当前课程主线优先是线性模型、神经网络和无监督学习；决策树可后置。
  - 未来什么时候需要整理：复习结构化数据建模、随机森林或 XGBoost 时。

- [[unsupervised-learning]]
  - 推荐文件名：unsupervised-learning.md
  - 为什么暂时是 C：可以先由 [[k-means]]、[[principal-component-analysis]] 和 [[anomaly-detection]] 承载具体内容。
  - 未来什么时候需要整理：需要总览无标签学习范式时。

- [[clustering]]
  - 推荐文件名：clustering.md
  - 为什么暂时是 C：当前聚类内容主要集中在 K-means，可先抽 [[k-means]]。
  - 未来什么时候需要整理：学习层次聚类、DBSCAN 或表示学习聚类时。

- [[feature-engineering]]
  - 推荐文件名：feature-engineering.md
  - 为什么暂时是 C：笔记有线性回归和异常检测中的特征工程线索，但还不是当前索引骨架的第一层。
  - 未来什么时候需要整理：做实际项目、错误分析或异常检测特征设计时。

- [[vectorization]]
  - 推荐文件名：vectorization.md
  - 为什么暂时是 C：它是实现效率主题，可先附在 [[linear-regression]] 和 [[forward-propagation]] 中。
  - 未来什么时候需要整理：复习 NumPy、矩阵乘法、GPU 或 CSAPP 性能优化时。

- [[computation-graph]]
  - 推荐文件名：computation-graph.md
  - 为什么暂时是 C：index.md 有计算图和反向传播线索，但内容还不够完整。
  - 未来什么时候需要整理：系统学习自动微分、PyTorch 或 TensorFlow 内部机制时。

- [[tensorflow]]
  - 推荐文件名：tensorflow.md
  - 为什么暂时是 C：当前只是实现工具线索，不是长期理论骨架。
  - 未来什么时候需要整理：需要集中整理 `Sequential`、`Dense`、`compile`、`fit` 和 `GradientTape` 时。

- [[agent-environment]]
  - 推荐文件名：agent-environment.md
  - 为什么暂时是 C：index.md 已标明当前只有碎片依据，需要补成强化学习交互框架。
  - 未来什么时候需要整理：深入强化学习、机器人控制或 VLA agent loop 时。

- [[return]]
  - 推荐文件名：return.md
  - 为什么暂时是 C：当前可先放入 [[reinforcement-learning]] 或 [[q-learning]]。
  - 未来什么时候需要整理：学习 discount factor、value function 或 policy optimization 时。

- [[state-action-reward]]
  - 推荐文件名：state-action-reward.md
  - 为什么暂时是 C：它是 RL 基础词汇，可先并入 [[reinforcement-learning]]。
  - 未来什么时候需要整理：构建强化学习术语表或环境接口时。

- [[content-based-filtering]]
  - 推荐文件名：content-based-filtering.md
  - 为什么暂时是 C：当前推荐系统主卡可以先覆盖它。
  - 未来什么时候需要整理：深入 two-tower model、embedding 或大规模推荐系统时。

- [[data-augmentation]]
  - 推荐文件名：data-augmentation.md
  - 为什么暂时是 C：index.md 有 OCR 数据增强线索，但属于项目优化专题。
  - 未来什么时候需要整理：学习计算机视觉、泛化提升或数据合成时。

- [[transfer-learning]]
  - 推荐文件名：transfer-learning.md
  - 为什么暂时是 C：当前笔记覆盖概念，但它依赖神经网络和特征表示理解。
  - 未来什么时候需要整理：进入深度视觉模型、预训练模型或微调时。

## 4. 推荐创建顺序

1. [[supervised-learning]]
2. [[linear-regression]]
3. [[cost-function]]
4. [[loss-function]]
5. [[gradient-descent]]
6. [[feature-scaling]]
7. [[logistic-regression]]
8. [[classification]]
9. [[decision-boundary]]
10. [[regularization]]
11. [[overfitting]]
12. [[bias-variance]]
13. [[train-dev-test-split]]
14. [[neural-network]]
15. [[forward-propagation]]

备选的下一批顺序：[[backpropagation]]、[[optimization]]、[[k-means]]、[[principal-component-analysis]]、[[anomaly-detection]]、[[recommender-system]]、[[reinforcement-learning]]、[[q-learning]]。

## 5. 跨课程连接候选

### [[gradient-descent]]

- 连接到 CS61A：迭代改进、函数抽象、通过重复更新逼近目标。
- 连接到 CS61B：大规模样本集合上的迭代算法和数据组织。
- 连接到 CSAPP：矩阵运算性能、向量化、缓存和浮点误差。
- 连接到 UMich DL：神经网络训练、optimizer、mini-batch。
- 连接理由：梯度下降既是数学优化概念，也是需要高效实现的训练循环。

### [[optimization]]

- 连接到 CS61A：状态更新、递归或迭代求解。
- 连接到 CS61B：算法复杂度、批处理数据结构。
- 连接到 CSAPP：程序性能、并行计算、数值稳定。
- 连接到 UMich DL：Adam、SGD、训练动态、自动微分。
- 连接理由：优化把目标函数、数据规模和硬件执行连接在一起。

### [[cost-function]]

- 连接到 CS61A：把问题转成可计算函数。
- 连接到 CS61B：对数据集合求和、聚合和维护统计量。
- 连接到 CSAPP：高效计算大规模 loss/cost。
- 连接到 UMich DL：loss design 和训练目标。
- 连接理由：cost function 是不同模型共享的目标表达。

### [[loss-function]]

- 连接到 CS61A：单样本误差函数。
- 连接到 CS61B：逐样本计算后聚合为总体目标。
- 连接到 CSAPP：log、exp、浮点下溢和数值稳定。
- 连接到 UMich DL：cross entropy、softmax loss、regression loss。
- 连接理由：loss 是反向传播和训练信号的直接来源。

### [[regularization]]

- 连接到 CS61A：约束条件和惩罚项的抽象表达。
- 连接到 CS61B：模型复杂度与数据规模的权衡。
- 连接到 CSAPP：模型规模会影响内存和计算成本。
- 连接到 UMich DL：weight decay、dropout、generalization。
- 连接理由：regularization 是从训练表现走向泛化表现的关键。

### [[bias-variance]]

- 连接到 CS61A：抽象过粗或过细都会导致问题。
- 连接到 CS61B：数据规模、模型容量和算法选择。
- 连接到 CSAPP：资源约束会限制模型容量和实验规模。
- 连接到 UMich DL：generalization diagnostics、model selection。
- 连接理由：bias-variance 是决定下一步工程动作的诊断框架。

### [[backpropagation]]

- 连接到 CS61A：函数组合、链式求值、递归依赖。
- 连接到 CS61B：计算图中的依赖关系和反向遍历。
- 连接到 CSAPP：自动微分的内存保存、矩阵运算和性能。
- 连接到 UMich DL：深度神经网络训练核心。
- 连接理由：backpropagation 同时是数学链式法则、图算法和系统实现问题。

### [[forward-propagation]]

- 连接到 CS61A：多函数组合形成整体计算。
- 连接到 CS61B：图或层结构中的数据流。
- 连接到 CSAPP：矩阵乘法、向量化和内存布局。
- 连接到 UMich DL：模型推理和网络结构设计。
- 连接理由：forward propagation 是神经网络 computation flow 的正向部分。

### [[linear-regression]]

- 连接到 CS61A：线性函数和模型抽象。
- 连接到 CS61B：特征数组、矩阵和数据集。
- 连接到 CSAPP：线性代数计算的数值和性能问题。
- 连接到 UMich DL：线性层、仿射变换和回归任务。
- 连接理由：线性回归是理解参数、特征和目标函数的最小完整模型。

### [[feature-scaling]]

- 连接到 CS61A：数据变换函数。
- 连接到 CS61B：批量数据预处理管道。
- 连接到 CSAPP：数值范围、浮点精度和运算稳定性。
- 连接到 UMich DL：输入归一化和训练稳定性。
- 连接理由：特征表示会直接影响优化路径和训练效率。

### [[neural-network]]

- 连接到 CS61A：函数组合和抽象层。
- 连接到 CS61B：图结构、节点和边的数据流类比。
- 连接到 CSAPP：矩阵运算、并行加速、内存访问。
- 连接到 UMich DL：深度学习所有后续主题的基础。
- 连接理由：神经网络同时涉及数据表示、计算图、优化和系统性能。

### [[recommender-system]]

- 连接到 CS61A：从 `(user_id, item_id)` 到评分的函数映射。
- 连接到 CS61B：图关系、哈希索引、检索和排序。
- 连接到 CSAPP：大规模候选召回、预计算和服务性能。
- 连接到 UMich DL：embedding、two-tower model 和 ranking。
- 连接理由：推荐系统把特征表示、相似度计算和大规模工程连接起来。

### [[q-learning]]

- 连接到 CS61A：递归价值定义和策略函数。
- 连接到 CS61B：状态图、搜索和动态规划思想。
- 连接到 CSAPP：replay buffer、训练循环和仿真性能。
- 连接到 UMich DL：DQN 和深度强化学习。
- 连接理由：Q-learning 是序列决策、价值函数和神经网络近似的交汇点。

## 6. 不要做的事

本 TODO 不创建具体 concept 文件，不生成 mistakes，不修改任何原始笔记，不修改 `index.md`，不逐文件总结，也不把概念 TODO 写成普通目录清单。
