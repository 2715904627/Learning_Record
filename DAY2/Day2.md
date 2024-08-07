# Day2

### ·OS learning, Assembly language

### ·videos：滴水三期，01-14(数据宽度，逻辑运算)

### ·books: x86汇编语言 从实模式到保护模式 (李忠 王晓波 余洁) \汇编语言（第4版） (王爽) 

##### 数据宽度

###### 计算机上的数据是有长度限制的

数学上的数没有长度限制，可以表示出来无限数，但是计算机由于硬件限制，只能尽可能的存储数据，计算机中的数据是有宽度的。

由于存储的需求，计算机有各种各样的容器来存储数据。

宽度以位来表示，相对物理/数学单位来讲没那么严谨。不同容器能存储不同宽度的数据，最基础的容器是字，即bit

在字之上，有更大范围的表示方式，如:

​	1byte = 8bit = 8位

​	1word = 16bit = 16位

​	1dword = 32bit = 32位

现代操作系统最大位数常为64位，也有32位

###### 计算机存储的数据只是字符，具体的意义由人定义

如一个byte中存储的数据，11111111，它表示的到底是-1，还是15，全由人自己定义，计算机只起到存储的作用

通常，定义有符号数、无符号数等表示。

###### 在有符号的情况下，正负数的关系像是钟表

![image-20240708000637487](C:\Users\Tlaloc\AppData\Roaming\Typora\typora-user-images\image-20240708000637487.png)

如图所示，像切蛋糕一样把正负数切开，F和0衔接（最大的负数和最小的正数），7、8像是磁铁的同级，相互排开

这样分的好处是，所有的负数第一位都是1，而所有的正数第一位都是0，方便后续的操作

如果数据溢出，那么最高位的进位会被丢弃，只保留原本的位，比如，FF+01 = 00，如果把图倒过来看，就像是23点往前走了一小时到了0点，很像钟表。

##### 逻辑运算

###### cpu如何计算2+3？

常用的逻辑运算：or and not xor

在二进制运算的数学意义上，不考虑进位的话：

​	0 + 0 = 0

​	1 + 1 = 0

​	0 + 1 = 1

​	1 + 0 = 1

通过这种真值表的表达，在cpu的加法中，采用xor这种逻辑门

但是这没有考虑进位的情况，而在进位的表示上，只有1 + 1会产生进位，别的情况下都没有，也就有了如下真值表：

​	0 + 0 = 0

​	1 + 1 = 1

​	0 + 1 = 0

​	1 + 0 = 0

这和and运算不谋而合，如果将两数与过后左移一位，再和xor结果相加，就能实现进位

所以基本的逻辑是，将两个数先进行xor运算，得到结果先保存。再进行and运算，得到结果左移一位，如果为0，则表示没有进位，那么原来结果为最终结果，如果不为0，则与原结果再按原步骤相加，直到没有进位。

以2 + 3为例：

2 + 3

X(寄存器)：0010			      X(寄存器)：0001

Y(寄存器)：0011			      Y(寄存器)：0100

先xor：				     先xor：

​	0010					0001

xor     0011				xor     0100

=============			       =============

​	0001					0101

R(寄存器)：0001			      R(寄存器)：0101

再and：				     再and：

​	0010					0001

and     0011				and     0100

=============			       =============

​	0010					0000

左移：0100				  左移：0000

有进位				      无进位

​					   则R中结果为最终结果：0101



###### 如果想获取某个值的第N位的值是多少？

利用and运算，在相应位设置1，其他位设置0即可，or操作同理

例如：8F 第五位

​	10001111

and     00001000

=================

​	00001000

则第五位值为1





###### 最简单的加密算法：

给出密钥，按相应位数依次异或即可

例：

2015   密钥：54

​	0010000000010101

xor     0101010001010100

=========================

​	0111010001000001



解密：

​	0111010001000001

xor     0101010001010100

=========================

​	0010000000010101

2015







##### 通用寄存器

###### 32位通用寄存器

| 寄存器 |               主要用途               | 编号 |
| ------ | :----------------------------------: | :--: |
| EAX    |                累加器                |  0   |
| ECX    |                 计数                 |  1   |
| EDX    |               I/O指针                |  2   |
| EBX    |            DS段的数据指针            |  3   |
| ESP    |               堆栈指针               |  4   |
| EBP    |            SS段的数据指针            |  5   |
| ESI    |  字符串操作的源指针；SS段的数据指针  |  6   |
| EDI    | 字符串操作的目标指针；ES段的数据指针 |  7   |



###### 最简单的汇编指令

MOV

基本格式：汇编指令 目标操作数，源操作数

例：MOV EAX,0X1 （记得标注数据进制）

结果：EAX 00000001