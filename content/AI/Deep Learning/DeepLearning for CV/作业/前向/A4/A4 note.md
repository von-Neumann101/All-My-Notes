## permute & view & obj头
pred_obj输出的大小是(B, num_anchors, H, W)
注意，**我们在什么时候都不需要看BatchSize或者N**，这只是一个训练技巧，实际上我们按照一个一个样本输入训练的方法也可以
H和W不变是1x1卷积的特性

**obj 头不是给“整张图”打分，而是给每个 anchor 打分，我们在Feature Map的每一个位置都放置num_anchors个Anchor**

num_anchors是输出的通道大小，可以这么理解，对于每种Anchor，我们的obj头都会输出一张HxW的置信图，代表每种Anchor在该位置为obj的可能性
## FPN
Feature Pyramid Network
CNN的底层有较高分辨率而缺少语义，FPN可以让每一层都高分辨率高语义

其核心结构是：
1. Backbone提供多尺度（从中间层拿输出）
2. 把高语义的输出up-stream到下层（语义传播）
3. 横向连接
## meshgrid
行，列，拓展一个列表
## stack
dim=几，就是把因stack生成的维度放到第几位