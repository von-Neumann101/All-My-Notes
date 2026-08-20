上节课我们实现了IntList类，用于创建一个int列表（链表），但是我们发现每次都要通过 *递归* 往IntList的开头添加数字(`L = new IntList(15, L)`)这明显没有抽象屏障，所以我们把这些内容都封装到一个新类中——SLList
```java
public class IntNode {  
    public int item;  
    public IntNode next;  
  
    public IntNode(int item, IntNode next){  
        this.item = item;  
        this.next = next;  
    }  
}
```
```java
public class SLList {  
    public IntNode first;  
  
    public SLList(int x){  
        first = new IntNode(x, null);  
    }  
  
    public void addFirst(int x){  
        first = new IntNode(x, first);  
    }  
  
    public int getFirst(){  
        return first.item;  
    }  
  
    public static void main(String[] args){  
        SLList L = new SLList(10);  
        L.addFirst(10);
        L.addFirst(15);  
  
        System.out.println(L.getFirst());  
    }  
}
```
我们建立了抽象屏障：想象用户只是一个刚学Java的小学生，他不一定会用递归在LinkList的开头添加元素（他不需要考虑IntList的具体实现）
![[Pasted image 20260319082455.png]]
 虽然汽车的发动机是直接产生动力的，但是你不能直接让用户操作或者有权限直接操作发动机，必须把它设置为private
```java
public class SLList {  
    private class IntNode {  
        int item;  
        IntNode next;  
  
        IntNode(int item, IntNode next){  
            this.item = item;  
            this.next = next;  
        }   
    }  
  
    private IntNode first;  
  
    public SLList(int x){  
        first = new IntNode(x, null);  
    }  
  
    public void addFirst(int x){  
        first = new IntNode(x, first);  
    }  
    
	public void addLast(int x){  
	    IntNode p = first;  
	    while(p.next != null){  
	        p = p.next;  
	    }  
	    p.next = new IntNode(x, null);  
	}
	
    public int getFirst(){  
        return first.item;  
    }  
}
```
我们不能让别人随便操作IntNode，但是又要SLList访问，于是我们设置内部类，再变为private，这样别人永远无法修改他
或者公共类但是返回IntNode对象，其他private也可以
如果你的内部类没有使用到外部类的任何东西，就可以设为static

![[Pasted image 20260319090727.png|307]]
想要实现抽象——size是一个“属性”，又要不改变指针指向的位置

但是最好的方法是创建一个size属性，每次在调用函数的时候++（空间换时间)

我们不想要特殊判断，我们要程序对null和其他IntNode的处理方式一样（L4.SLList_pro）——哨兵节点
#链表 #Java #抽象
