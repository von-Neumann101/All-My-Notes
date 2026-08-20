## hashCode and Equals
Hash在某些情况下，不一定总是能常数时间（只是平均意义），最好的情况当然是每个桶都均匀的放置元素，最坏的情况和BST类似
默认Hash码使用内存地址
![[Pasted image 20260402163858.png|234]]
每次运行都会不同（取内存地址，这是随机的）
如果我们取Hash Code始终等于0，我们得到一个类似链表的结构，复杂度退化为线性（最坏情况）
![[Pasted image 20260402164032.png|348]]
如果Hash Code就是返回Label，程序会自动取模
![[Pasted image 20260402164351.png|208]]
显然，对于存入的元素，我们要尽可能的让其均匀分布在桶中
> [!hashCode]
> 为什么Java给我们权限重写HashCode呢？
> 假如我们有不同RGB的0，我们的equals函数认为只要数字一样，RGB不同的也是一种元素
> 由于这n个元素实际上不是一个元素（内存地址不同），我们取hashcode有可能会进入错误的桶中，再用equals你就找不到了（或者说如果HashCode不同，equals都不会调用）
> HashSet的contains先用hashCode()找，再用equals()判断是否相等
> 或者说 hashCode决定去哪个桶找，而equals决定桶里哪个是我
> 上面的图，y轴就是HashCode，x轴就是equals

^ae4717

所以我们让equals只在意字面量，HashCode返回字面量

Java中，任何重写equals的方法都有对应的HashCode
## 可变键的风险
String是不可变的，每次进行所谓的拼接，都是创建一个新字符串
![[Pasted image 20260404112820.png]]List的hashCode是基于内容的，你如果add以后，“键”(hashCode)就改变了（因为List的hashCode是看内容的），原来他在A桶，修改完以后应该放B桶，但是hashSet不会重新分桶，等于说你查`[0, 1, 7]`的时候hashCode会把你带到B桶，但实际上`[0, 1, 7]`还在A桶
#Java #哈希