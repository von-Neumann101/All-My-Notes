## 简介
Image Classification: A core CV task
**图片**作为输入，**固定标签集中的标签**作为输出
计算机看到的是一个巨大的矩阵(e.g. 800 x 800 x 3)
![[Pasted image 20260311082819.png|126]]
挑战：如果对于同一个猫，稍微换一种角度，矩阵都会大不相同。不同的猫更不一样了。如果我们想识别不同种的猫，如何提高鲁棒性。背景干扰。光照干扰。动作。遮挡
[[Deep Learning/DeepLearning for CV/L12 Object Detection/note|目标检测]]：
![[Pasted image 20260311083539.png]]

Hard-code难以解决分类 -> Machine Learning
这是一种Data-Driven而非Knowledge-Driven方法（无法通过类似传统编程手段解决）
```py
def train(image, labels):
	return model

def predict(model, test_images):
	return test_labels 
```
MNIST：手写数字数据
**CIFAR10：彩色多类别小图片数据**
CIFAR100
**ImageNet：超级图片数据集**（物体）
MIT Places（场景）
Omniglot：少量示例（非常鲁棒性的学习）
## 算法
### 1.Nearest Neighbor
#### 内容
train->记住所有的数据与标签 $O(1)$
predict->取新图像与训练集每个图像比较相似度，返回最大相似度图片对应的Label$O(n)$
L1-距离：每个分量差的绝对值
![[Pasted image 20260311090225.png|553]]
注意复杂度，这实际上很不好，因为我们不需要训练很快，但是我们需要预测很快

效果（对于摘了近视眼镜的人来说很像）：
![[Pasted image 20260311090708.png|452]]

决策边界（对于最简单情况）：
![[Pasted image 20260311090859.png|573]]
噪声影响大，鲁棒性不高。我们考虑K-Nearest Neighbor
#### 优化
类似于随机森林算法，我们取相似度排名前K个，然后选择标签众数作为该图的Label
![[Pasted image 20260311091452.png|284]]
可能会出现平局（2 dog & 2 cat）

使用不同的距离度量
![[Pasted image 20260311091806.png|553]]
可以看出最临近算法可以用于各种数据上，通过不同的“距离度量”（KL散度）

#### 设置超参数
dev集选择超参数
升级：将数据集分为多个部分，遍历每个小部分做dev集，其余训练集（缺点是太昂贵）
![[Pasted image 20260311092640.png|521]]

![[Pasted image 20260311092829.png|361]]
#### 特点
K-Nearest Neighbor没有假设其可近似的函数类型，所以当Data趋于无穷时，几乎可以拟合非病态函数的所有函数
![[Pasted image 20260311093020.png|293]]（如果有无穷个点，绿线就能覆盖蓝线了）
**维度灾难**：需要指数级上升的数据量以达到上述效果
#### 缺点
![[Pasted image 20260311093633.png]]
第一张图和剩下三张图的相似度是一样的
说白了，K-Nearest Neighbor算法无法捕捉有语义或有意义的特点

**但是，使用CNN计算的“特征”进行最临近算法很有效**（添加语义）：
![[Pasted image 20260311093842.png]]
说明其在语义上理解图片
#K邻近算法 #图像分类