和之前的LinkedList不一样的是，这次的列表是基于Array的
之前的LinkedList中，get比getLast慢很多，因为getLast只需要访问哨兵节点的next就行，但是get需要遍历
我们考虑一个和双向链表很像的，但是get更快的，基于Array的List——AList
不要让用户知道如何实现的
![[Pasted image 20260323164745.png]]
空列表是prev是next的哨兵节点
#数组 #列表 #抽象