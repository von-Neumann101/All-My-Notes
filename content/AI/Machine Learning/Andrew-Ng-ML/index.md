# Machine Learning Index

## 1. 课程主线

这组笔记的主线是从“给定输入和正确答案，学习映射”开始，逐步扩展到更复杂的模型、更系统的优化与泛化诊断，再进入无标签结构发现和序列决策。

监督学习部分先建立最基础的预测框架：用输入特征 $x$ 预测目标 $y$。线性回归把预测写成 $f_{w,b}(x)=wx+b$ 或多特征形式 $\boldsymbol{w}\boldsymbol{x}+b$，再通过平方误差代价函数衡量预测和真实值的差距。梯度下降负责最小化代价函数，特征放缩、向量化、特征工程和多项式特征则是在实际训练中让优化更稳定、让模型表达能力更合适的工具。

在分类问题中，笔记从线性回归过渡到逻辑回归：模型不再直接输出连续预测值，而是用 sigmoid 把线性函数转成 $P(y=1|\boldsymbol{x};\boldsymbol{w},b)$。决策边界来自 $\boldsymbol{w}\boldsymbol{x}+b=0$，损失函数也从平方误差转向更适合分类的交叉熵形式。过拟合问题引出增加数据、特征选择和正则化，其中正则化不是删除特征，而是惩罚过大的权重。

深度学习部分把逻辑回归推广为神经网络中的一个神经元。神经网络通过多层神经元和非线性激活函数学习中间特征，前向传播用矩阵乘法高效计算每一层激活值，反向传播则从右向左计算参数对代价函数的偏导，并用于梯度下降。这里的核心链条是：模型结构决定前向计算，损失函数定义训练目标，优化算法更新参数，正则化和数据划分决定模型能否泛化。

泛化能力的讨论贯穿深度学习笔记后半部分。训练集、dev 集和测试集分别用于拟合参数、选择模型和估计泛化误差；偏差与方差用来诊断欠拟合和过拟合；学习曲线、错误分析、数据增强、迁移学习和 MLOps 则把模型训练放进一个完整的机器学习项目循环中。

无监督学习部分从“没有标签，只寻找结构”出发。K-means 通过重复分配最近聚类中心和更新中心来最小化失真函数；PCA 寻找保留方差最多的低维主成分，并通过投影和重构理解有损压缩；异常检测使用密度估计和高斯模型判断低概率样本；推荐系统则从用户和物品的评分关系中学习特征向量，用协同过滤或内容过滤完成预测与排序。

强化学习部分把机器学习从静态输入输出映射推进到序列决策。模型学习的不是单个样本的正确答案，而是在状态 $s$ 下选择动作 $a$ 的策略 $\pi:s\to a$，目标是最大化折扣回报 $G_t$。Q 函数、Bellman 方程、DQN、epsilon-greedy、replay buffer、mini-batch 和 soft update 共同构成了从当前奖励到长期价值最大化的学习框架。

## 2. 核心概念列表

### 监督学习

- [[supervised-learning]]：已覆盖。监督学习被定义为在给定正确答案的情况下建立输入到输出的映射，包含回归和分类。
- [[linear-regression]]：已覆盖。包含单变量和多特征假设函数、向量化、正规方程线索。
- [[cost-function]]：已覆盖。平方误差代价函数、逻辑回归损失、K-means 失真函数和推荐系统 cost function 都有涉及。
- [[gradient-descent]]：已覆盖。包含通用更新规则、线性回归梯度下降、逻辑回归梯度，以及 batch 梯度下降。
- [[feature-scaling]]：已覆盖。包含最大值归一化、均值归一化和 Z-score 归一化。
- [[logistic-regression]]：已覆盖。包含 sigmoid、概率解释、分类场景、决策边界和交叉熵损失。
- [[classification]]：已覆盖。包含二分类、多分类、多标签分类、skewed data set 中的 precision 和 recall。
- [[decision-boundary]]：已覆盖。包含 $f_{\boldsymbol{w},b}(\boldsymbol{x})\ge 0.5$ 与 $\boldsymbol{w}\boldsymbol{x}+b\ge 0$ 的关系。
- [[regularization]]：已覆盖。包含线性回归、逻辑回归和神经网络中的 L2 正则化线索。
- [[bias-variance]]：已覆盖。包含 train/dev/test、模型选择、学习曲线、高偏差和高方差诊断。
- [[train-dev-test-split]]：已覆盖。笔记明确给出训练集、交叉验证集/dev 集、测试集的用途。
- [[decision-tree]]：已覆盖。包含熵、信息增益、递归划分、随机森林和 XGBoost。

### 深度学习

- [[neural-network]]：已覆盖。神经元、层、隐藏层、输出层、Dense Layer 都有涉及。
- [[activation-function]]：已覆盖。包含 sigmoid、ReLU、linear、softmax 以及为什么隐藏层不能只用线性激活。
- [[forward-propagation]]：已覆盖。包含矩阵乘法、$A^TW+B$、激活值计算和 TensorFlow 推理结构。
- [[backpropagation]]：已覆盖。笔记说明反向传播从右向左一次计算所有偏导，并被 `fit` 用于梯度下降。
- [[loss-function]]：已覆盖。包含二元交叉熵、SparseCategoricalCrossentropy、softmax loss 和逻辑回归损失。
- [[gradient-checking]]：需要人工补充。当前笔记有反向传播和自动微分，但没有明确讨论 gradient checking。
- [[optimization]]：已覆盖。包含梯度下降、Adam、TensorFlow GradientTape、mini-batch 和 soft update。
- [[regularization-in-neural-networks]]：部分覆盖，需要人工补充。笔记出现 `kernel_regularizer=L2(0.01)` 和大神经网络配合正则化的讨论，但缺少系统公式展开。
- [[softmax]]：已覆盖。包含多分类概率、softmax loss 和数值稳定性优化。
- [[precision-recall]]：已覆盖。用于 skewed data set，并讨论 F1-score。

### 无监督学习

- [[unsupervised-learning]]：已覆盖。定义为不给标签、从数据集中寻找结构。
- [[clustering]]：已覆盖。包含聚类与二分类的区别。
- [[k-means]]：已覆盖。包含最近中心分配、中心更新、失真函数、初始化和 elbow method。
- [[principal-component-analysis]]：已覆盖。包含降维、主成分、投影、重构和 scikit-learn 实现线索。
- [[anomaly-detection]]：已覆盖。包含密度估计、高斯模型、阈值 $\epsilon$、评估和特征选择。
- [[recommender-system]]：已覆盖。包含 per-item features、协同过滤、均值归一化、content-based filtering 和大规模检索排序。

### 强化学习

- [[reinforcement-learning]]：已覆盖。包含状态、动作、奖励、价值函数和策略。
- [[agent-environment]]：部分覆盖，需要人工补充。笔记明确讨论环境随机性、动作改变状态和 replay tuple，但没有系统画出 agent-environment loop。
- [[state-action-reward]]：已覆盖。包含状态 $s$、动作 $a$、奖励 $R(s)$ 和 tuple $(s,a,R,s')$。
- [[return]]：已覆盖。包含折扣回报 $G_t$。
- [[policy]]：已覆盖。定义为 $\pi:s\to a$，目标是得到使 value 最大化的 $\pi^*$。
- [[q-learning]]：已覆盖。包含 Q-function、Bellman Equation、DQN target 和 epsilon-greedy。

## 3. 重要公式 / 算法 / 实现

### Linear Regression Hypothesis

- 名称：线性回归假设函数
- 解决的问题：用一个线性函数从输入特征预测连续目标值，例如房价预测。
- 核心公式或思想：
  - 单变量：$f_{w,b}(x)=wx+b=\hat{y}$
  - 多特征：$f_{\boldsymbol{w},b}(\boldsymbol{x})=\sum_{i=1}^n w_ix_i+b=\boldsymbol{w}\boldsymbol{x}+b$
- 相关概念链接：[[linear-regression]]、[[supervised-learning]]、[[feature-engineering]]

### Mean Squared Error / Cost Function

- 名称：平方误差代价函数
- 解决的问题：衡量线性回归预测值与真实值之间的整体误差，并作为优化目标。
- 核心公式或思想：
  - $J(w,b)=\frac{1}{2m}\sum_{i=1}^{m}(f_{w,b}(x^{(i)})-y^{(i)})^2$
  - 训练目标是最小化 $J(w,b)$。
- 相关概念链接：[[cost-function]]、[[linear-regression]]、[[gradient-descent]]

### Gradient Descent Update Rule

- 名称：梯度下降更新规则
- 解决的问题：沿代价函数下降最快的方向迭代更新参数。
- 核心公式或思想：
  - $w_{new}=w-\alpha\frac{\partial}{\partial w}J(w,b)$
  - $b_{new}=b-\alpha\frac{\partial}{\partial b}J(w,b)$
  - $w$ 和 $b$ 需要同时更新。
- 相关概念链接：[[gradient-descent]]、[[optimization]]、[[cost-function]]

### Linear Regression Gradient Descent

- 名称：线性回归的 batch 梯度下降
- 解决的问题：把平方误差代价函数对 $w,b$ 的偏导用于参数更新。
- 核心公式或思想：
  - $w_{new}=w-\alpha\frac{1}{m}\sum_{i=1}^{m}(f_{w,b}(x^{(i)})-y^{(i)})x^{(i)}$
  - $b_{new}=b-\alpha\frac{1}{m}\sum_{i=1}^{m}(f_{w,b}(x^{(i)})-y^{(i)})$
  - 笔记强调线性回归中 local minimum 等于 global minimum。
- 相关概念链接：[[linear-regression]]、[[gradient-descent]]

### Logistic Regression Sigmoid

- 名称：逻辑回归与 sigmoid
- 解决的问题：把线性函数转化为二分类概率。
- 核心公式或思想：
  - $g(z)=\frac{1}{1+e^{-z}}$
  - $f_{\boldsymbol{w},b}(\boldsymbol{x})=g(\boldsymbol{w}\boldsymbol{x}+b)=P(y=1|\boldsymbol{x};\boldsymbol{w},b)$
  - 当阈值取 0.5 时，决策边界对应 $\boldsymbol{w}\boldsymbol{x}+b=0$。
- 相关概念链接：[[logistic-regression]]、[[classification]]、[[decision-boundary]]

### Logistic Loss

- 名称：逻辑回归损失函数
- 解决的问题：避免分类任务中平方误差导致的非理想代价曲面，用交叉熵思想惩罚错误概率。
- 核心公式或思想：
  - 笔记给出的形式：$L(f_{\boldsymbol {w},b}(\boldsymbol{x}^{(i)}),y^{(i)})=-\log{(y^{(i)}+(-1)^{y^{(i)}-1}f_{\boldsymbol {w},b}(\boldsymbol{x}^{(i)})))}$
  - 直觉：若真实标签为 1，模型输出越接近 1 损失越小；若真实标签为 0，模型输出越接近 0 损失越小。
- 相关概念链接：[[loss-function]]、[[logistic-regression]]、[[classification]]

### Regularized Cost Function

- 名称：L2 正则化代价函数
- 解决的问题：缓解过拟合，让部分权重尽可能小，而不是直接删除特征。
- 核心公式或思想：
  - $J(w,b)=\frac{1}{2m}\sum_{i=1}^{m}(f_{w,b}(x^{(i)})-y^{(i)})^2+\frac{\lambda}{2m}\sum_{j=1}^{n}w_j^2$
  - 一般不对 $b$ 正则化。
  - 线性回归的更新中会出现权重衰减因子 $(1-\alpha\frac{\lambda}{m})$。
- 相关概念链接：[[regularization]]、[[overfitting]]、[[bias-variance]]

### Neural Network Forward Propagation

- 名称：神经网络前向传播
- 解决的问题：从输入特征逐层计算隐藏层和输出层的激活值，用于推理预测。
- 核心公式或思想：
  - 每个神经元类似一个逻辑回归单元。
  - 一层的向量化计算可以理解为 $A^TW+B$ 后再套激活函数。
  - 非线性激活函数使多层网络不退化为线性回归。
- 相关概念链接：[[neural-network]]、[[forward-propagation]]、[[activation-function]]

### Backpropagation

- 名称：反向传播
- 解决的问题：高效计算每个参数对代价函数 $J$ 的偏导，用于训练神经网络。
- 核心公式或思想：
  - 笔记强调反向传播只需要一次从右向左的计算，就可以得到所有参数的偏导。
  - TensorFlow 的 `model.fit` 会利用反向传播得到梯度下降需要的偏导项。
  - 具体链式法则公式需要人工补充。
- 相关概念链接：[[backpropagation]]、[[gradient-descent]]、[[neural-network]]

### K-means

- 名称：K-means 聚类
- 解决的问题：在没有标签的数据中，把样本分成 $K$ 个簇。
- 核心公式或思想：
  - 失真函数：$J(c^{(1)},...,c^{(m)},\mu_1,...,\mu_k)=\frac{1}{m}\sum^m_{i=1}\lVert x^{(i)}-\mu_{c^{(i)}} \rVert^2$
  - 固定中心时，把样本分配给最近中心。
  - 固定分配时，把中心更新为该簇样本均值。
  - 用不同初始化多次运行，选择代价函数最小的结果。
- 相关概念链接：[[k-means]]、[[clustering]]、[[unsupervised-learning]]

### PCA Projection / Reconstruction

- 名称：PCA 投影与重构
- 解决的问题：在尽量少损失信息的情况下减少特征维度，常用于可视化。
- 核心公式或思想：
  - PCA 寻找使投影后方差最大的主成分，也等价于最小化样本到主成分的距离。
  - Reconstruction 是从压缩维度的信息有损还原原始信息。
  - 笔记给出例子：点 $(2,3)$ 在 $l:y=x$ 主成分上的投影长度乘以单位向量 $[0.71,0.71]^T$ 即可重构。
  - 通用矩阵形式需要人工补充。
- 相关概念链接：[[principal-component-analysis]]、[[dimensionality-reduction]]

### Anomaly Detection Gaussian Model

- 名称：异常检测的高斯密度模型
- 解决的问题：通过低概率判断异常样本。
- 核心公式或思想：
  - 对于 $n$ 个特征：$p(\vec{x})=\prod^n_{i=1}p(x_i;\mu_i,\sigma_i^2)$
  - 若 $p(x_{test})<\epsilon$，则判断为异常。
  - 若某个特征值极端偏离，会让乘积中的一项很小，从而拉低整体概率。
- 相关概念链接：[[anomaly-detection]]、[[unsupervised-learning]]、[[feature-engineering]]

### Recommender System Cost Function

- 名称：协同过滤 cost function
- 解决的问题：从用户对物品的评分中同时学习用户参数和物品特征，并预测未评分项目。
- 核心公式或思想：
  - $J(w,b,x)=\frac12\sum_{(i,j):r(i,j)=1}(w^{(j)}\cdot x^{(i)}+b^{(j)}-y^{(i,j)})^2+\frac{\lambda}{2}\sum_{j=1}^{n_u}\sum_{k=1}^{n}(w_k^{(j)})^2+\frac{\lambda}{2}\sum_{i=1}^{n_m}\sum_{k=1}^{n}(x_k^{(i)})^2$
  - “联合”学习用户参数和 item 特征是协同过滤的关键。
  - 均值归一化用 $\mu_i$ 修正新用户评分全为 0 的问题。
- 相关概念链接：[[recommender-system]]、[[collaborative-filtering]]、[[regularization]]

### Content-based Recommendation

- 名称：基于内容的推荐
- 解决的问题：利用用户特征和物品特征计算匹配程度，缓解协同过滤的信息不足问题。
- 核心公式或思想：
  - 用深度学习从 $x_u^{(j)}$ 和 $x_m^{(i)}$ 得到 $v_u^{(j)}$ 和 $v_m^{(i)}$。
  - 用点积 $v_u^{(j)}\cdot v_m^{(i)}$ 作为评分或相似度预测。
  - 大规模系统中先检索候选，再排序。
- 相关概念链接：[[recommender-system]]、[[neural-network]]、[[embedding]]

### Bellman Update / Q-learning

- 名称：Bellman 方程与 Q-learning 目标
- 解决的问题：把当前奖励和未来最优价值结合起来，学习状态动作价值函数。
- 核心公式或思想：
  - $Q(s,a)=R(s)+\gamma \max_{a'}Q(s',a')$
  - 随机环境中：$Q(s,a)=R(s)+\gamma \mathbb{E}[\max_{a'}Q(s',a')]$
  - DQN target：$x=(s,a)$，$y=R(s)+\gamma\max_{a'}Q(s',a')$。
- 相关概念链接：[[q-learning]]、[[reinforcement-learning]]、[[return]]、[[policy]]

### TensorFlow / Implementation Notes

- 名称：TensorFlow 实现线索
- 解决的问题：用现成框架构建模型、计算梯度和训练参数。
- 核心公式或思想：
  - `Sequential([... Dense(...) ...])` 构建神经网络。
  - `model.compile(loss=...)` 指定损失。
  - `model.fit(X,Y,epochs=...)` 训练模型。
  - `tf.GradientTape()` 可用于自动微分。
- 相关概念链接：[[tensorflow]]、[[neural-network]]、[[optimization]]

## 4. 容易混淆点

- cost function vs loss function：loss function 通常描述单个样本的损失，cost function 通常是所有样本损失的平均或总和，再加上可能的正则化项。当前笔记在逻辑回归中先定义单样本 loss，再讨论 cost。
- gradient descent vs backpropagation：gradient descent 是用梯度更新参数的优化方法；backpropagation 是神经网络中高效计算这些梯度的方法。
- parameter vs hyperparameter：$w,b,x$ 等被训练更新的是参数；$\alpha,\lambda,K,\epsilon,\gamma$、树深度、神经元数量等由人为选择或调参的是超参数。需要人工补充更系统的定义。
- overfitting vs underfitting：过拟合在笔记中明确出现，表现为模型过度适应训练数据；underfitting 可对应高偏差，但当前笔记没有用该词系统展开，需要人工补充。
- bias vs variance：高偏差说明训练集本身拟合不好；高方差说明训练集和 dev/test 表现差距大。笔记用 $J_{train},J_{cv},J_{test}$ 和基准性能水平进行诊断。
- regularization vs normalization：regularization 惩罚权重，控制模型复杂度；normalization/feature scaling 改变特征尺度，让优化更稳定。
- linear regression vs logistic regression：线性回归输出连续值，适合回归；逻辑回归在线性函数外接 sigmoid 输出概率，适合分类。
- supervised learning vs unsupervised learning：监督学习有正确答案或标签；无监督学习不给标签，只在输入数据中寻找结构。
- PCA vs feature selection：PCA 创建新的低维轴来压缩信息；特征选择是保留或删除原始特征。笔记分别讨论了二者，但二者对比需要人工补充。
- anomaly detection vs supervised classification：异常检测把小概率事件视为可疑，适合未来异常不一定像已知异常的场景；监督分类更依赖正负样本都足够、有代表性。
- policy vs value function：policy 是从状态到动作的函数 $\pi:s\to a$；value/Q-function 衡量某状态或状态动作带来的长期价值。
- reward vs return：reward 是单步奖励；return 是折扣后的长期奖励总和 $G_t$。
- K-means vs classification：K-means 没有标签，目标是按距离结构分簇；classification 有标签，目标是预测离散类别。
- PCA vs linear regression：线性回归拟合输入到输出的关系；PCA 寻找保留信息的投影方向，不是在做监督拟合。
- multiclass vs multilabel classification：多分类通常用 softmax 在多个类别中选一个；多标签分类更像多个 sigmoid 分类器并行判断多个标签。
- collaborative filtering vs content-based filtering：协同过滤依赖用户 item 评分表学习潜在特征；内容过滤利用用户和 item 本身特征生成向量再做匹配。
- precision vs recall：precision 看模型判为正的样本中有多少真为正；recall 看所有真实正样本中有多少被找出。F1-score 用调和平均平衡二者。

## 5. 推荐复习顺序

### 第一轮：监督学习基础

- 应复习的核心概念：[[supervised-learning]]、[[linear-regression]]、[[cost-function]]、[[gradient-descent]]、[[feature-scaling]]
- 相关笔记入口：[[Machine_Learning]]
- 需要人工补充的部分：线性代数视角下的向量化、正规方程适用条件和数值稳定性。

### 第二轮：优化与泛化

- 应复习的核心概念：[[optimization]]、[[regularization]]、[[bias-variance]]、[[train-dev-test-split]]、[[learning-curve]]
- 相关笔记入口：[[Machine_Learning]]、[[Deep_learning]]
- 需要人工补充的部分：parameter vs hyperparameter 的系统整理、正则化强度和偏差方差的更具体关系。

### 第三轮：逻辑回归与分类

- 应复习的核心概念：[[logistic-regression]]、[[classification]]、[[decision-boundary]]、[[loss-function]]、[[precision-recall]]
- 相关笔记入口：[[Machine_Learning]]、[[Deep_learning]]
- 需要人工补充的部分：交叉熵的标准分段公式、最大似然与逻辑回归 cost function 的推导。

### 第四轮：神经网络与反向传播

- 应复习的核心概念：[[neural-network]]、[[activation-function]]、[[forward-propagation]]、[[backpropagation]]、[[softmax]]、[[regularization-in-neural-networks]]
- 相关笔记入口：[[Deep_learning]]
- 需要人工补充的部分：反向传播的链式法则公式、gradient checking、不同 optimizer 的数学细节。

### 第五轮：无监督学习、PCA、异常检测、推荐系统

- 应复习的核心概念：[[unsupervised-learning]]、[[clustering]]、[[k-means]]、[[principal-component-analysis]]、[[anomaly-detection]]、[[recommender-system]]
- 相关笔记入口：[[异常检测]]、[[Principal_Components Analysis]]、[[Recommender]]
- 需要人工补充的部分：PCA 的矩阵公式、协方差矩阵和 SVD；异常检测中多元高斯模型；推荐系统中的 embedding 视角。

### 第六轮：强化学习

- 应复习的核心概念：[[reinforcement-learning]]、[[agent-environment]]、[[state-action-reward]]、[[return]]、[[policy]]、[[q-learning]]
- 相关笔记入口：[[Reinforcement_Learning]]
- 需要人工补充的部分：agent-environment loop、state value function $V(s)$、Q-learning 与 DQN 的区别、target network 的标准表述。

### 第七轮：跨模块复盘

- 应复习的核心概念：[[loss-function]]、[[cost-function]]、[[gradient-descent]]、[[optimization]]、[[generalization]]、[[regularization]]、[[feature-engineering]]
- 相关笔记入口：[[Machine_Learning]]、[[Deep_learning]]、[[异常检测]]、[[Recommender]]、[[Reinforcement_Learning]]
- 需要人工补充的部分：不同模块中“目标函数”的统一视角，例如监督学习最小化误差、K-means 最小化失真、推荐系统最小化评分误差、强化学习最大化 return。

## 6. 可抽取到 concepts/ 的候选条目

| 概念名 | 推荐文件名 | 优先级 | 为什么值得长期保留 | 可能连接到的其他课程 |
|---|---|---:|---|---|
| [[supervised-learning]] | `supervised-learning.md` | A | 是回归、分类、神经网络训练的共同入口。 | CS61A 函数抽象；UMich DL |
| [[linear-regression]] | `linear-regression.md` | A | 最基础的参数化模型，连接假设函数、MSE 和梯度下降。 | CS61A；CSAPP 数值计算 |
| [[cost-function]] | `cost-function.md` | A | 贯穿线性回归、逻辑回归、K-means、推荐系统和神经网络。 | UMich DL；CS61A |
| [[gradient-descent]] | `gradient-descent.md` | A | 是从代价函数到参数更新的核心机制。 | UMich DL；CSAPP 性能优化 |
| [[logistic-regression]] | `logistic-regression.md` | A | 是分类、sigmoid、交叉熵和神经元模型的桥梁。 | UMich DL |
| [[regularization]] | `regularization.md` | A | 直接连接过拟合、权重惩罚、模型选择和泛化。 | UMich DL |
| [[bias-variance]] | `bias-variance.md` | A | 是诊断模型表现和决定下一步工作的关键框架。 | UMich DL |
| [[neural-network]] | `neural-network.md` | A | 深度学习的基础概念，连接层、激活、前向传播和训练。 | UMich DL |
| [[forward-propagation]] | `forward-propagation.md` | A | 是神经网络推理过程，也是理解矩阵化实现的基础。 | UMich DL；CSAPP 性能 |
| [[backpropagation]] | `backpropagation.md` | A | 是神经网络训练的核心，需要长期单独沉淀。 | UMich DL |
| [[train-dev-test-split]] | `train-dev-test-split.md` | A | 是模型选择和泛化评估的基本方法。 | UMich DL |
| [[k-means]] | `k-means.md` | A | 代表无监督聚类的核心算法，目标函数清晰。 | CS61B 聚类数据结构应用 |
| [[principal-component-analysis]] | `principal-component-analysis.md` | A | 连接降维、投影、重构和可视化。 | CSAPP 数值表示；UMich DL |
| [[anomaly-detection]] | `anomaly-detection.md` | A | 连接密度估计、高斯模型、阈值选择和特征工程。 | UMich DL |
| [[recommender-system]] | `recommender-system.md` | A | 连接协同过滤、内容过滤、embedding 和大规模检索排序。 | CS61B；UMich DL |
| [[reinforcement-learning]] | `reinforcement-learning.md` | A | 是从静态预测到序列决策的入口。 | UMich DL |
| [[q-learning]] | `q-learning.md` | A | 连接 Q-function、Bellman、DQN 和策略选择。 | UMich DL |
| [[activation-function]] | `activation-function.md` | B | 解释神经网络为什么需要非线性，以及 sigmoid、ReLU、softmax 的选择。 | UMich DL |
| [[softmax]] | `softmax.md` | B | 是多分类输出层和交叉熵损失的重要概念。 | UMich DL |
| [[precision-recall]] | `precision-recall.md` | B | 对类别不平衡问题比 accuracy 更有解释力。 | UMich DL |
| [[decision-tree]] | `decision-tree.md` | B | 笔记已覆盖熵、信息增益、随机森林和 XGBoost，可作为结构化数据模型入口。 | CS61B 树结构 |
| [[agent-environment]] | `agent-environment.md` | C | 当前笔记有碎片依据，但需要补成强化学习基本交互框架。 | UMich DL |
| [[gradient-checking]] | `gradient-checking.md` | C | 当前笔记缺失，但它是验证反向传播实现的重要工具。 | UMich DL |

## 7. 不要做的事

本索引没有逐文件总结，没有生成 mistake log，没有创建 `concepts/` 文件，也没有修改原始笔记。

需要人工补充的条目已经在对应位置标出，后续可以从这些条目中选择少数高优先级概念再拆成长期 concept 文件。
