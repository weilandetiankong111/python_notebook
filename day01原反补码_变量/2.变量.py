# ### 变量 : 可以改变的量就是变量,实际上指代的是内存的一块空间
# (1) 变量的概念
rujia305 = "赵万里"
rujia305 = "孟凡伟"
rujia305 = "康玉中"
print(rujia305)

# (2)变量的声明
# 1
a = 100
b = 101
print(a)
print(b)

# 2
a,b = 200,201
# print(值1,值2,值3, ..... ) 一行打印所有变量
print(a , b)

# 3
a = b = 300
print(a, b)

# (3)变量的命名
"""
		  变量的命名
字母数字下划线,首字符不能为数字
严格区分大小写,且不能使用关键字
变量命名有意义,且不能使用中文哦
"""

# abc123 = 1
# 123abdc error
________1_ = 1
# ___@@_ = 2 error 
# a__________ = 90
# 1____ = 10 error


# 严格区分大小写
abc = 10
ABC = 11
print(abc) # 10
print(ABC) # 11

# 关键字 : 系统预设的相关属性和函数或者特殊意义的变量;
# 引入 模块(文件)
import keyword
# 模块.属性 (文件.变量)
print(keyword.kwlist)
"""
[
'False', 'None', 'True', 'and', 'as', 'assert', 
'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 
'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 
'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while',
 'with', 'yield'
 ]
"""
# 系统预设的相关关键字不能被替换覆盖,不要使用改名字作为变量名;
"""
print = 100
print(1)
"""

# 起名字要见名知意
mycar = "特斯拉"
youcar = "五菱宏光"
asldkfjaskldjfklasdjfklasjdklfjasdkl = "宝马" # 不推荐

# 中文命名变量不会报错的,但是严禁使用
中文 = "赵万里"
print(中文)

n =  "赵万里"
print(n)

"""
(1) 字符编码:
	中文命名的变量容易乱码;
		utf-8(万国码): 一个中文占用3个字节,字母数字其他符号占用1个字节
		gbk (国标码) : 一个中文占用2个字节,字母数字其他符号占用1个字节
(2) 占用空间:
	中文命名变量比英文命名变量占用更大的空间.
"""

# (4)变量的交换
a = 18
b = 19

# 通用写法
tmp = a
a = b
b = tmp
print(a,b)

# python特有
a = 18
b = 19
a,b = b,a
print(a,b)

# (5) 常量 : 永远不变的量(约定俗成:把每个字母都变成大写)
BIRTHDAY = "1010"
ID_CARD = 210205200010106688







