世界模型的重要特征在于可以进行**无监督训练**，具体来说，是可以在agent的**世界模型生成的梦境环境中**训练agent，训练出的策略可以很好地迁移回实际环境
# Architecture
![[Pasted image 20260728105450.png]]
整个Agent由三个模块组成——**V**ision Model、**M**emory Model、**C**ontroller
## VAE (V) Model
![[Pasted image 20260730085354.png]]
VAE用于把一帧映射到[[Latent Spaces and Network Architectures#Latent Spaces|Latent Space]]并把其中的向量映射回原来的帧，既可以降低维度以减少计算成本，也可以进行特征提取
## MDN-RNN (M) Model
![[Pasted image 20260730085930.png|470]]
M Model的作用的**预测未来**。由于环境的复杂性，RNN输出的是**概率密度函数**$p(z)$而**不是一个确定性的未来**——本文中使用**高斯分布的加权求和**作为其近似
RNN在建模$P_\tau(z_{t+1}\mid a_t,z_t,h_t)$，在给定当前时间步$t$的**动作**$a_t$和**历史状态**$h_t$后，通过当前的视觉特征$z_t$预测未来的视觉特征$z_{t+1}$的**分布**。同时我们调整**温度**$\tau$控制模型的不确定性
> [!NOTE] 高斯分布加权求和
> Contents

## Controller (C) Model
C Model负责产生决策，以最大化Agent在此期间的预期累计奖励
本文中刻意使C Model尽可能简单——**单层线性模型**$a_t=W_c[z_th_t]+b_c$
# Interact with Environment
![[Pasted image 20260730091327.png]]
## Car Racing Experiment
![[Pasted image 20260730091608.png|489]]

**V Model**：
让Agent在环境中随机探索，然后随机取几帧作为训练数据（同时记录随机动作$a_t$）
![[Pasted image 20260730092143.png|231]]![[Pasted image 20260730092206.png|230]]
左右分别为原图和重建的图，可以看出重建的图在保留了图中重要的部分前提下，删去了大量无关细节。

**M Model**：
在V训练好以后，我们用其获得视觉特征$z_t$并开始训练M Model——这里用到了之前说的随机动作$a_t$（V Model训练的时候不需要的）

注意，无论是V还是M，他们对环境的决策以及奖励信号完全不了解。他们的任务仅仅是获得Latent Space向量以及对未来的预测。
### 流程
1. 以随机策略收集1000次rollout
2. 训练VAE
3. 训练MDN-RNN
4. *进化* Controller最大化预期累计奖励

# Dream
刚才的例子中，我们使用随机的rollout来训练C Model，如果这么做，世界模型和普通的强化学习又有什么区别呢？
注意到我们的M Model是可以生成$p(z_{t+1})$的，那么只需要每次对M Model的输出采样，就能得到一个Latent Space中的向量$z_{t+1}$（注意，通过VAE的Decoder就能得到一幅**人眼可以看到的图像**）
我们可以利用M Model生成一个梦境环境，并在梦境环境中训练Controller
## VizDoom Experiment
![[Pasted image 20260730093535.png|465]]
和东方一样，躲避子弹
### 流程
这里的M模型**还需要预测一个二元事件**$d_t$，表示Agent是否死亡（这一点的原因会在后面提到）
具体的训练流程和上面的Car Racing一样的，只是Controller在M提供的梦境环境中训练
### Training Inside of the Dream
M Model可以**学习游戏引擎**——游戏逻辑、敌人行为、物理以及 3D 图形渲染
比如，Agent选择向左移动，**M Model会学习将Agent向左移动**——而这本来是由游戏引擎负责的。这也是为什么一开始我们要求M Model预测Agent是否死亡，目的就是要模拟一个游戏引擎出来。
通过调整温度$\tau$我们可以让M Model生成随机性强（更难）的环境。下面会讲到**提高温度**能防止Controller**利用世界模型的缺陷**
## Transfer Policy to Actual Environment
![[Pasted image 20260730094715.png|650]]
左右分别是游戏截图和重建图
可以看到，虽然V Model没能完全捕捉到每帧的所有细节，但是Agent仍然可以利用学习到的策略在真实环境中决策（这可能是由于Latent Space中的向量包含了**一些人眼（就算用了Decoder）无法观察的信息**）
## Cheating the World Model
> 在我们的初步实验中，我们注意到我们的智能体发现了一种对抗性策略，以某种方式移动，使得在这个受 M 规则支配的虚拟环境中，怪物在部分运行过程中不会射出任何火球。即使有火球形成的迹象，智能体也会以灭火的方式移动。

通过提高$\tau$，我们能获得更加健壮的决策
![[Pasted image 20260730095211.png]]
# Iterative Training Procedure
在上面的两个实验中，任务相对简单，因此可以使用从随机策略收集的数据集训练一个合理的世界模型。然而，在更加困难的环境中，**使用随机策略会产生很多问题**（比如在MC中，玩家可能会卡在某个封闭的矿洞中，随机策略会导致玩家几乎永远被困在里面）。我们需要让Agent稍微有脑子地在环境中导航以后才开始收集数据。

我们使用**迭代训练**
1. 初始化M和C Model
2. 在环境中部署$N$次，Agent在这个过程中可能进行学习，并保存这一过程的动作$a_t$，观察$x_t$
3. 训练M Model来建模$P(x_{t+1},r_{t+1},a_{t+1},d_{t+1}\mid x_t,a_t,h_t)$，并训练C Model来优化M内部的预期奖励
4. 没有达到目标，返回(2)
## 不断改进的模型
### M
目前的方法中，M Model是对下一帧预测的模型，如果他表现不佳就说明Agent遇到了他不熟悉的环境。
解决这种问题的做法是调整M Model的损失函数以**鼓励其好奇心**，具体的做法是**在C Model的loss处减去M Model的loss**——这样Controller就会**特地往M Model表现不佳的地方跑，进而改进真实环境中的世界模型**
### C
> As you learn to do something like play the piano, you no longer have to spend working memory capacity on translating individual notes to finger motions — this all becomes encoded at a subconscious level.

杂技演员在走钢丝的时候并不会刻意调整怎么走路的。同样，我们还需要求M Model预测下一个事件步长的动作和奖励（尤其是动作）
这对于复杂困难的任务来说是必要的，M Model可以吸收C Model的简单决策，如此C Model就可以进行更加复杂的决策
#强化学习 #世界模型 #网络训练 