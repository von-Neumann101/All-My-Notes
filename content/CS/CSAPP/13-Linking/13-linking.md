系统如何构建程序？
# Linking
## Linking
![[Pasted image 20260825101407.png|660]]
此处`main.c`里声明了一个函数体为空的函数，是为了告诉编译器“它的定义在其他模块中，先允许我调用它。”

如果在终端输入：
```bash
linux> gcc -Og -o prog main.c sum.c 
linux> ./prog
```
整个过程是：
![[Pasted image 20260825101531.png|440]]

这么做有两点好处：
- 模块化
- 效率：更改一个模块里的代码，不必要重新编译其他模块
## Linkers
链接器执行的主要任务有两个：
1. 符号解析：
   **符号定义**(`void swap();{......}`)、**符号引用**(`swap();`)——我们可以称定义的名称为**符号**
   符号定义被汇编器存储在object文件的**符号表**（一个**结构体数组**，包含这个符号的名称、大小、位置）中
   ![[Pasted image 20260906101237.png|462]]
   **符号解析**是指在链接过程中，链接器将每一个符号引用和**恰好一个**符号定义连接（多个模块之间的重名情况，使得Linkers需要决定到底使用哪个）
2. 重定位：
   将所有的模块**合并**为一个单一的可执行object文件
   在重定位之前，object文件里函数和数据的地址**是他们在模块中的偏移量**。Linkers需要决定每个符号最终在程序执行时位于内存的哪个位置，然后将这些**绝对内存位置绑定到符号上**。然后**更新所有的引用**，使得其指向正确的位置
### Three Kinds of Object Files (Modules)
![[Pasted image 20260825105237.png|488]]
`.o`是需要被 *链接* 以后才能执行的文件；`a.out`是可执行文件；`.so`后面讨论
### Executable and Linkable Format (ELF)
ELF是object文件的标准的二进制格式——上述的三种类型使用相同的一般格式

![[Pasted image 20260825110720.png|235]]
- ELF header：定义了如字长、字节序、文件类型(`.o`, `a.out`, `.so`)等信息
- Segment header table：只为可执行文件定义，**指示代码的不同段在内存的位置**（栈的位置，代码位置）
- .text section：代码（只读）
- .rodata section：只读数据，比如switch的跳表
- .data section：包含所有已初始化全局变量的
- .bss section：**定义**了未显式初始化，或者初始化为 0 的全局变量和 `static` 变量（不占空间）

![[Pasted image 20260825110649.png|230]]
- .symtab section：符号表
- .rel .text/.data section：当Linkers识别有对符号的引用时，他会做一个记号以告知此处需要重定位
- .debug section：储存源代码行号和机器码的行号关联的信息
- Section header table：标淡紫色的所有section的起始位置
### Linker Symbol
对于Linkers来说，有三种不同类型的符号：
- Global：没有用`static`修饰的全局变量或者函数
- External：被某个模块引用，但是在其他模块中定义的Global symbols——[[13-linking#Linking|main.c调用的sum就是在引用External symbols]]
- Local：在模块内部定义和引用的符号（注意**Linkers不知道所谓的“局部变量”**，这是由编译器在运行时栈上管理的）。这里我们指用`static`修饰的全局变量或函数

> [!NOTE] C语言的 `static`
> 1. 隐藏：
>    用`static`修饰的变量和函数会**对其他源文件隐藏**。如果不用其修饰，全局变量和函数对其他源文件可见。`static`修饰函数只有这一个作用
> 2. 静态数据：
>    被`static`修饰的变量在程序刚运行时就初始化，且只初始化一次（默认初始化为0）
#### Local Symbols
![[Pasted image 20260825153629.png|215]]
这里的每一个静态变量`x`都只能在其定义的函数内作用。此外，`x`被`static`修饰以后，不会再被储存在栈中——而是.data（编译器会**在.data里声明空间**，并且给同名的变量取不一样的名字）
#### Example
![[Pasted image 20260825153427.png|625]]
#### Duplicate Symbol Definitions
如何解决符号重名的问题？我们先把符号分为两种：
- 强符号：函数名或已初始化的全局变量
- 弱符号：未初始化的全局变量
![[Pasted image 20260825155234.png|605]]
#### Linker’s Symbol Rules
![[Pasted image 20260825155409.png|593]]
规则2的意思是，链接时会把那个弱符号和强符号看为同一个符号（也就是说，变量只有一个）
**规则3可能引发问题**，`-fno-common`会使得出现多个弱符号时Linkers报错
#### Linker Puzzles
![[Pasted image 20260825160548.png|689]]
教材的P472~473给的例子要比这个好很多
##### Example
```c
/* foo5.c */
int y = 15212;
int x = 15213;       // 强符号，4 bytes

int main()
{
    f();
}
```

```c
/* bar5.c */
double x;

void f()
{
    x = -0.0;
}
```

**在编译`bar5.c`时，编译器在编译`f`时，就会生成移动8字节的机器代码**，而链接器使用的是在`foo5.c`里的强符号的定义，所以这里的`int x`和外部文件的`double x`指向的是相同内存的起始地址
所以在运行到`f();`时，会跳转到别的地方运行**移动8字节的机器代码，而这个代码的目标就是`x`**。然而这里的内存结构是
```text
|  x  |  y  |
 4字节  4字节
```
这会直接覆盖掉`y`
**类型决定访存宽度发生在编译期；链接期主要决定符号地址**。所以这里提供了一个抽象：所有最终参与重定位的符号定义，都必须来自 $E$ 中的目标文件
#### Global Variables
尽可能避免使用全局变量。如果必须要使用，尽量使用`static`修饰，并且在定义时初始化（如果使用外部全局变量，使用`extern`修饰——告知编译器这是由别的模块**定义**的）
### Relocation
刚刚Linkers已经把每个符号引用和唯一的符号定义绑定起来，现在要把所有的object文件组合起来

依旧是之前的例子：
![[Pasted image 20260826105506.png|239]]
除了`main.o`和`sum.o`，还有**程序开始前和结束后实际运行的系统代码**

Linkers决定某种顺序，并把他们**连续地**按照顺序放在一起（包括符号表之类的）
![[Pasted image 20260826105741.png|277]]

同时，Linker必须要决定程序被加载时，在哪里存储这些不同的符号——这里会给`main()`, `swap()`, `array`绝对内存地址
#### Relocation Entries
编译器并不知道链接器会给每个符号什么地址。所以编译器创建了给链接器的提示（红色），称为**重定位条目**
![[Pasted image 20260826110611.png|544]]
注意第三行，通常情况下一个数组的起始地址不会是`0x0`，这正是**编译器不知道地址导致的**，所以他只是把一个立即数放到`%edi`（传入的第一个参数）
最左边的那些数`0,4,9,e,...`是他们在这个模块的偏移量
红字前面的字母（数字）是地址的偏移量，是编译器命令链接器要Relocate的地址偏移量
```
bf 00 00 00 00 #bf是mov的字节表示，后面的0指的是地址
↑  ↑
9  a
```

Relocation结束的完整代码：
![[Pasted image 20260826113933.png]]
注意，`call`指令使用的是`%rip+偏移量`来跳转的，字节码是`05 00 00 00`是同样的原因
## Loading Executable Object Files
![[Pasted image 20260826114512.png|620]]
Linkers生成的object file可以直接被加载到内存中，而不用进一步修改
左边是ELF，右边是[[09-advanced#Memory Layout|内存的结构]]
在堆和栈之间的巨大空隙中，是共享库的区域（`.so`都加载到这个区域）

我们可以写一个大的`.c`文件，然后放上所有的函数，程序员只需要和自己的程序链接即可；或者一个函数一个文件。但这都不是好的想法
### Old-fashioned Solution: Static Libraries
`.a`(archive) 归档文件，**是`.o`文件的集合，每一个`.o`文件都写了一个函数**
### Creating Static Libraries
![[Pasted image 20260826145507.png|582]]
如果这里有任何一个函数发生变化了，需要重新编译那个函数的`.o`文件，并重新归档所有的`.o`文件

![[Pasted image 20260826145646.png|643]]
### Linking with Static Libraries

![[Pasted image 20260826145744.png|539]]
图示：（`libc.a`主要包含了诸如`printf();`之类的函数）
![[Pasted image 20260826145821.png|574]]

**链接器解析外部引用的算法**：
Linkers维护一个可重定位目标文件的集合$E$（此集合中的文件会被合并起来**形成可执行文件**），一个**被引用但是没有被定义的符号**集合$U$，一个在**前面**（Linkers按命令行的输入从左到右读取）输入文件中**已定义的符号**集合$D$
对于每个输入文件：
- 如果是`.o`文件，Linkers会把它添加到$E$，并修改$U$和$D$
- 如果是`.a`文件，Linkers会尝试匹配$U$中没有被解析的符号，如果该文件中某个成员目标文件$m$定义了该符号，则将$m$放入$E$中，并修改$U$和$D$
  对`.a`的每个文件都这么操作，直到$U$和$D$不再变化，**此时任何不包含在$E$中的成员都会被丢弃**

最终，如果$U$非空，那么程序报错。否则Linkers会合并并重定位$E$中的文件，构建可执行文件

![[Pasted image 20260906150505.png|653]]
思考这里的C选项

> [!NOTE] `vector.h`
> `#include "vector.h"`在预处理阶段会被展开为
> ```
> void addvec(int *x, int *y, int *z, int n);
void multvec(int *x, int *y, int *z, int n);
> ```
### Modern Solution: Shared Libraries
它们**包含的代码和数据在程序实际加载加载到内存时，或程序加载完实际运行时才被加载**。也被称作动态链接库(DLLs,`.so`文件)
共享库可以被多个进程同时使用
#### Dynamic Linking at Load-time
![[Pasted image 20260827113123.png|619]]
右上角的指令意思是把那两个函数编译、链接成一个动态链接库 `libvector.so`
经过链接器(Partially linked)也只是在符号表中加一个标记，表示当程序加载时需要解析这些函数的引用
**以运行时需要DLL（可以多个程序共用）为代价，换取了更小的文件大小**
#### Dynamic Linking at Run-time
![[Pasted image 20260827213835.png|651]]![[Pasted image 20260827214106.png|654]]
这里非常直接地体现了“**程序运行时才连接共享库**”。因为我们甚至没有

程序已经开始**执行`main`以后**，才执行这条语句：
```C
handle = dlopen("./libvector.so", RTLD_LAZY); //获得库的句柄
```
运行时寻找函数定义：
```C
addvec = dlsym(handle, "addvec");
```
**这里使用字符串`"addvec"`查找`libvector.so`的动态符号表，找`addvec`的运行地址，并保存到函数指针`addvec`**
> [!NOTE] `.h`文件 & `.so`
> 前者定义函数该怎么调用，类似于java的接口，只是规定了函数名、参数、返回值类型
> 后者则是有函数的具体实现
## Summary
![[Pasted image 20260827221215.png|530]]
# Case study: Library interpositioning 
**拦截来自库的函数调用**，可能是为了记录一些统计数据或者进行一些错误检查，然后才正式进行调用（同时我们不能改变源代码）
## Example Program
![[Pasted image 20260828100253.png|278]]
在程序运行时，且不动源代码的情况下，跟踪被分配和释放的内存块的地址及大小
### Compile-time Interpositioning
在源程序**被编译成机器代码之前**，通过预处理器**宏**，把对 `malloc`、`free` 的调用替换成自己编写的**包装函数**
![[Pasted image 20260828101449.png|568]]

![[Pasted image 20260828101817.png|616]]
```bash
linux> make intc 
gcc -Wall -DCOMPILETIME -c mymalloc.c
gcc -Wall -I. -o intc int.c mymalloc.o 
linux> make runc 
./intc 
malloc(32)=0x1edc010 
free(0x1edc010)
```
`-I`是让预处理器**在当前目录寻找头文件**，所以我们使用的是自己编写的`malloc.h`
### Link-­time Interpositioning
和编译期interpose的区别在于`malloc` 的引用在哪个阶段被改成包装函数
![[Pasted image 20260828103403.png|674]]
![[Pasted image 20260828103649.png|585]]
`gcc`是一个总的调度器(`cpp`, `cc1`, `as`, `ld`)，`--warp`是链接器`ld`的选项。所以要加上`-WL,`以表示后面用逗号分隔的参数转交给链接器

注意函数名字不是随便起的，必须是：
```text
__wrap_原函数名
__real_原函数名
```
第一个是包装函数，是最终实际调用的函数；而第二个是原状的函数
```text
malloc        → __wrap_malloc
__real_malloc → malloc
```
### Load/Run-­time Interpositioning
![[Pasted image 20260828110804.png|659]]
`RELD_NEXT`表示在下一个地方查找，找到的也就是原版的`malloc`（不一定是，因为可能加载了多个共享对象）
![[Pasted image 20260828112715.png|673]]
`(LD_PRELOAD="./mymalloc.so" ./intr)`设置这个环境变量意味着在**解决引用的时候首先在**这个位置查找
