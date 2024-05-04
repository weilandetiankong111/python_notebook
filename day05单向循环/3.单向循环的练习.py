# ### 单向循环的练习

# (1)打印 一行十个小星星* help(print)
# help 查看某个方法的文档
help(print)

"""
# print("*",end='')
# print("*",end='')
# print("*",end='')
# print("*",end='')
# print("*",end='')
# print("*",end='')
# print("*",end='')
# print("*",end='')
# print("*",end='')
# print("*",end='')
"""
i = 0
while i<10:	
	# end='' 打印时,尾部默认不加换行
	print("*",end='')	
	i += 1
# 默认换行
# print()

# (2)通过打印一个变量的形式,展现一行十个小星星
print("<======>")
i = 0
strvar = ""
while i < 10:
	# 写上循环的逻辑
	strvar += "*" # strvar = strvar + "*"
	i +=1
print(strvar)
"""
strvar += "*" => strvar = "*"
strvar += "*" => strvar = "*" + "*"  = "**"
strvar += "*" => strvar = "**" + "*" = "***"
...
strvar += "*" => strvar = "********" + "*" = "*********"
"""

# (3)一行十个换色的星星 ★☆★☆★☆★☆★☆
"""
# 方法一
i = 0
while i < 5:
	print("★☆",end="")
	i+=1
"""

# 方法二
i = 0
while i < 10:
	if i % 2 == 0 :
		print("★",end="")
	else:
		print("☆",end="")
	i+=1

print("<=============>")
# 方法三
i = 0
strvar = ""
while i < 10:
	if i % 2 == 0 :
		strvar += "★"
	else:
		strvar += "☆"
	i+=1
print(strvar)
"""
***公式: 任意数 和 n 进行取余,余数的范围: 0 ~ (n-1)***
0 % 2 = 0
1 % 2 = 1
2 % 2 = 0
3 % 2 = 1
被除数 % 2 => 0 或者 1

0 % 5 = 0 
1 % 5 = 1
2 % 5 = 2
3 % 5 = 3
4 % 5 = 4
5 % 5 = 0 
6 % 5 = 1
7 % 5 = 2
被除数 % 5 => 0 或者 1,2,3,4
"""

# (4)用一个循环,打印十行十列小星星
"""
★★★★★★★★★★
★★★★★★★★★★
★★★★★★★★★★
★★★★★★★★★★
★★★★★★★★★★
★★★★★★★★★★
★★★★★★★★★★
★★★★★★★★★★
★★★★★★★★★★
★★★★★★★★★★
"""
# 方法一
i = 0 
while i < 100:
	
	# 逻辑写在这里
	print("*" , end="")
	# 打印换行 (在9 19 29 .. 99 )
	if i % 10 == 9:
		print()
	i += 1 


"""
0123456789
**********
10111213141516171819
**********
20212223242526272829
**********

...
90919293949596979899
**********
9 19 29 39 49 59 69 79 89 99
9 % 10  = 9
19 % 10 = 9
29 % 10 = 9
...
99 % 10 = 9

"""


print("<======>")
# 方法二
i = 1
while i <= 100:
	
	# 逻辑写在这里
	print("*" , end="")
	# 打印换行 (在9 19 29 .. 99 )
	if i % 10 == 0:
		print()
	i += 1 
"""
12345678910
**********
11121314151617181920
**********
21222324252627282930
**********

...
919293949596979899100
**********
10 20 30 ... 100
"""

# (5) 一个循环实现十行十列,格列换色的小星星
"""
★☆★☆★☆★☆★☆
★☆★☆★☆★☆★☆
★☆★☆★☆★☆★☆
★☆★☆★☆★☆★☆
★☆★☆★☆★☆★☆
★☆★☆★☆★☆★☆
★☆★☆★☆★☆★☆
★☆★☆★☆★☆★☆
★☆★☆★☆★☆★☆
★☆★☆★☆★☆★☆
"""

i = 0 
while i < 100:
	
	# (1)打印星星
	if i % 2 == 0 :
		print("★",end="")
	else:
		print("☆",end="")
	
	# (2)打印换行 (在9 19 29 .. 99 )
	if i % 10 == 9:
		print()
	
	i += 1 

# (6)一个循环实现十行十列,隔行换色的小星星
"""
★★★★★★★★★★
☆☆☆☆☆☆☆☆☆☆
★★★★★★★★★★
☆☆☆☆☆☆☆☆☆☆
★★★★★★★★★★
☆☆☆☆☆☆☆☆☆☆
★★★★★★★★★★
☆☆☆☆☆☆☆☆☆☆
★★★★★★★★★★
☆☆☆☆☆☆☆☆☆☆

*** 公式:任意数和n进行地板除,会出现n个相同的数
0 // 10 = 0
1 // 10 = 0
2 // 10 = 0
..
9 // 10 = 0
0 ~ 9 // 10 => 0 (10个相同的0)

10 // 10 = 1
11 // 10 = 1
12 // 10 = 1
...
19 // 10 = 1
10 ~ 19 // 10 => 1 (10个相同的1)

.... 以此类推
20 ~ 29 // 10 => 2 (10个相同的2)
30 ~ 39 // 10 => 3 (10个相同的3)
40 ~ 49 // 10 => 4 (10个相同的4)
...
90 ~ 99 // 10 => 9 (10个相同的9)

0~ 100 会出现10个相同的0,1,2 , 3 ... 9 

0 // 3 0
1 // 3 0
2 // 3 0
3 // 3 1
4 // 3 1
5 // 3 1 
"""

""""""

# 方法一
i = 0 
while i < 100:
	
	# (1)打印星星
	if i // 10 % 2 == 0:
		print("★",end="")
	else:
		print("☆",end="")

	# (2)打印换行 (在9 19 29 .. 99 )
	if i % 10 == 9:
		print()
	
	i += 1 

# 方法二
print("<=================>")
i = 10
while i < 110:
	# 打印星星 
	num = int(str(i)[-2])
	if num % 2 == 0 :
		print("★",end="")
	else:
		print("☆",end="")
	# 打印换行
	if i % 10 == 9:
		print()
	i+=1

"""
10 ~ 100 101 102 103 110...

10 ~ 19 => 1
20 ~ 29 => 2
30 ~ 39 => 3
90 ~ 99 => 9
100 ~ 109 => 0
"""
