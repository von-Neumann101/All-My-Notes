假设我们有一个集合存储了sam, sad, sap, same, a, awls字符串
我们要构建一个高效的表示
![[Pasted image 20260411185124.png|427]]
# Trie（字典树）
## Trie Set
每个节点只存一个字符，我们用路径来代表字符串（节点可以被共享）
![[Pasted image 20260411185953.png|194]]
这有一个问题，如果我们只找路径的话，会存在不在Set里的单词(aw)，我们可以通过标记每个单词的结尾以标定一个单词
![[Pasted image 20260411190403.png|188]]
Add & Contains最开始有点像HashSet，我们首位比较，然后比较下一位，一直比较直到不匹配了，我们创建一个新分支（我们一共要比较L次——L是单词长度）
这其实很像嵌套的HashMap
常数时间需要字符串不能是任意长

字典树最强大的地方在于其可以快速得到字符串子集
我们可以找一个字符串的最长前缀：例如sample就是sam
或者可以找所有包含某个前缀的值：例如sa就是sad, sam, same, sap

## Trie Maps
![[Pasted image 20260413083027.png|413]]
我们在单词结尾节点放置value，就能实现trie map
# 实现
![[Pasted image 20260413083509.png|415]]
我们这里有一个特殊的类——DataIndexedCharMap。我们用于把数字(ASCLL)映射为字符，这也是R=128的目的。同时，这也表示了Trie存储数据的特殊性
![[Pasted image 20260413083734.png]]
现实是这样的
![[Pasted image 20260413084056.png|322]]
因为我们在next里存储了一个数字转字母的字典，我们实际上在边上就已经有值了，所以我们压根不需要每个节点里label，label隐含在DataIndexedCharMap中。

这也导致了一个问题，我们的数据结构里会有大量的空链接
![[Pasted image 20260413085438.png|366]]
# 改进
lazysize，我们使用Hash Map作为DataIndexedCharMap
![[Pasted image 20260413085625.png|216]]
或者是BST
![[Pasted image 20260413085710.png|235]]
#Trie #树 #哈希