深度学习对目标检测的影响(PASCAL VOC)
![[Pasted image 20260407095546.png|519]]
# R-CNN Training
**我们（人类）需要标注的数据只有GT boxes**
## Slow/Fast R-CNN Training
实际检测的时候，我们把区域提议的框分为三类，正中负
![[Pasted image 20260407100209.png|278]]
1. 阳性样本（和GT Boxes的IoU>0.5）——蓝色
2. 阴性样本（和GT Boxes的IoU<0.3）——红色
3. 中性样本（和GT Boxes的0.3<IoU<0.5，不好解释是阳性还是阴性，比如狗的脸）——灰色
训练的时候我们一般忽略中性框，因为这可能让CNN学到一些奇怪的东西
目标是训练CNN使得将Positive的区域分类为正样本，反之亦然

我们要输出提议区域的变换系数（非Background），以及区域的Object标签
![[Pasted image 20260407100805.png|418]]
这里我们的标注是Offline的，我们可以先运行区域提议算法，然后再训练CNN
注意这里，所有东西都有分类损失，但是只有正样本才能产生回归损失，这使得我们的损失函数有点复杂
由于机器学习假设训练时的输入和预测时的输入很相近，所以区域提议在非Faster的R-CNN里，其统计特性必须在测试时和训练时很相近
## Faster R-CNN Training

第一阶段，我们生成很多Anchor（大小固定，注意这里固定的意思是人为设置的），然后 **区域提议网络(RPN)** 把固定的Anchor转化为区域提议
第二阶段，我们将区域提议转化为最终输出的Object框
这两个阶段使用的损失函数和Slow/Fast R-CNN里的一样RPN有分类损失（是否是Background——二分类），回归损失（微调Anchor）

复习一下，区域提议网络判断是否是Background，并且略微修改Anchor，把这个当做区域提议送给我们的CNN
```
1. 输入图像  
2. 通过 backbone 得到 feature map  
3. 在 feature map 上生成 anchors  
4. ← 在这里：计算 anchor 和 GT 的 IoU  
5. 根据 IoU 分配标签（正 / 负 / 忽略）  
6. 用这些标签计算 loss
```
## Rol Pool
![[Pasted image 20260407110716.png|379]]
实际上，我们先前的对齐和实际的输入偏差较大，这是一个大问题
在反向传播中，这也是一个问题，因为我们强行的对齐（实际上我们用了高斯函数，这是不可导的），导致原坐标丢失（没有任何东西存储该信息量）
解决方法就是 **RoI Align**

> [!为什么RPN还能正常训练呢？] 为什么RPN还能正常训练呢？
> 先看看整体的运行流程：[[Deep Learning/DeepLearning for CV/L12 Object Detection/note#总结|note]]
> 我们注意到有两条独立的Loss流程
> L_RPN → RPN → backbone
> L_det → RoI → proposal → RPN
> 所以说，RoI pooling不影响RPN（反向传播）
> ![[Pasted image 20260407114509.png]]
> 虽说我们的Backbone本身就是已经训练好的模型了，但是只有RPN的梯度传递到那。
> 如果RoI可微分的话，我们能RoI上面的部分参与训练Backbone
### RoI Align
我们直接把GT box映射到
![[Pasted image 20260407112142.png]]
我们现在把映射到Feature map上的框，**完全均分**，然后我们在每个区域里均匀采样一些点（一般是4个）
![[Pasted image 20260407134003.png|287]]
$$f_{x,y}=\sum_{i,j}f_{i,j}\max(0,1-|x-i|)\max(0,1-|y-j|)$$
其中
$$i\in \{\left\lfloor x \right\rfloor+1,...,\left\lceil x \right\rceil+1\},\ j\in\{\left\lfloor y \right\rfloor+1,...,\left\lceil y \right\rceil+1\}$$
例子：
![[Pasted image 20260407135911.png|181]]
![[Pasted image 20260407135922.png|397]]
此为双线性差值
在1维的情况下是$f(x)=(1−(x−i))f(i)+(x−i)f(i+1)$
## Detection without Anchor: CornerNet
![[Pasted image 20260407141649.png]]
我们估计一个左上角Embedding向量和右下角Embedding向量，我们计算相似度，然后得到一个框

# Semantic Segmentation
![[Pasted image 20260407143244.png]]
语义分割并不分割一类的东西，注意两条牛的语义分割
## 工作
### 滑动窗口
![[Pasted image 20260407144005.png]]
### 全连接CNN
![[Pasted image 20260407144051.png|560]]
本质就是多分类问题，每个像素决定是哪一个类
为了获得较大的感受野，我们需要堆叠很多的卷积层，同时我们需要计算的类也很多

接下来我们考虑一个类似Encoder-Decoder的结构：
![[Pasted image 20260407144633.png|542]]
我们先进行下采样再进行*上采样*
#### UnPooling
##### 种类
**Bed of Nails**（不好）
![[Pasted image 20260407144834.png|267]]
**Nearest Neighbor**
![[Pasted image 20260407144929.png|266]]
**Bilinear Interpolation**
```
●        ●

       
●        ●
   变成
●  ●  ●  ●
●  ●  ●  ●
●  ●  ●  ●
●  ●  ●  ●
```
![[Pasted image 20260407151215.png|384]]
现在这些新的点我们都通过线性差值来算
注意我们实际上是八等分边（注意点的位置）
**Max Unpooling**
![[Pasted image 20260407151752.png]]
和Bed of Nails的区别是保留了一部分的信息
**Transposed Convolution**
很多名字：
![[Pasted image 20260407152922.png|161]]

先回顾一下卷积
![[Pasted image 20260407152110.png|395]]
![[Pasted image 20260407152141.png|395]]

上采样：
![[Pasted image 20260407152614.png|417]]
（本图来源于 *《动手学深度学习》* ）
重叠区域我们就把不同卷积核的值相加
1D的情况（注意output是一个5x1的矩阵），其第三行第一列是az+bx
![[Pasted image 20260407152814.png|323]]
![[Pasted image 20260407153253.png]]
这也是为什么这叫做**转置卷积**
##### 选择
一般在Encoder的地方使用了平均池化，我们在Decoder的位置使用双线性差值或者三线性插值
使用了Max pooling我们就使用Max Unpooling
## Things and Stuff
一般CV中，我们在区分这两者
![[Pasted image 20260407153931.png|334]]
**Instance Segmentation**
![[Pasted image 20260407154017.png]]
做法就是先目标检测，然后语义分割确定检测物体和哪些像素对应
我们在Fast R-CNN上加上一个模块即可
![[Pasted image 20260407154503.png]]
![[Pasted image 20260407154636.png]]
![[Pasted image 20260407154727.png]]
# 关键点检测
类似像动作捕捉里的骨架![[Pasted image 20260407154930.png|129]]
![[Pasted image 20260407155003.png]]![[Pasted image 20260407155023.png]]

这是一个源泉，往里面接不同的头可以干不同的事情
![[Pasted image 20260407155204.png]]
#语义分割 #目标检测 #RPN #FPN