# ### 双向循环的专题练习

# 1.用两个循环完成十行十列的小星星
j = 0 
while j < 10:

	# 打印星星
	i = 0
	while i < 10:
		print("*",end="")
		i+=1
	
	# 打印换行
	print()

	j += 1

# 2.用两个循环完成十行十列隔列换色的小星星
"""
☆★☆★☆★☆★☆★
☆★☆★☆★☆★☆★
☆★☆★☆★☆★☆★
☆★☆★☆★☆★☆★
☆★☆★☆★☆★☆★
☆★☆★☆★☆★☆★
☆★☆★☆★☆★☆★
☆★☆★☆★☆★☆★
☆★☆★☆★☆★☆★
☆★☆★☆★☆★☆★
"""

i = 0
while i < 10:
	# 打印一行黑白相间的星星
	j = 0
	while j < 10:
		if j % 2 == 0:
			print("☆",end="")
		else:
			print("★",end="")
		j +=1

	# 打印换行
	print()	
	i+=1


# 3.用两个循环完成十行十列隔行换色的小星星
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
"""
"""
外层的循环i动的慢
内层的循环j动的快
外层的i动一次, 内层的循环动10次

"""
i = 0
while i < 10 :
	j = 0
	while j < 10:
		if i % 2 == 0:
			print("☆",end="")
		else:
			print("★",end="")
			
		j +=1
	print()
	i +=1

# 4.99乘法表
# 方向一
i = 1
while i <= 9:
	
	# 打印对应的表达式
	j = 1
	while j <= i:
		print("%d*%d=%2d " % (i,j,i*j) ,end="" )
		j+=1
	
	# 打印换行
	print()
	
	i +=1



# 方向二
i = 9
while i >= 1:

	# 打印对应的表达式
	j = 1
	while j <= i:
		print("%d*%d=%2d " % (i,j,i*j) ,end="" )
		j+=1
	
	# 打印换行
	print()

	i -= 1
print("<====================>")
# 方向三
i = 1
while i <= 9 :
	kongge = 9 - i
	# 打印空格
	while kongge > 0:
		print("       ",end="")
		kongge -= 1  

	# 打印表达式
	j = 1
	while j <= i:
		print("%d*%d=%2d " % (i,j,i*j) ,end="" )
		j+=1
	
	# 换行
	print()
	i +=1

print("<===============>")
# 方向四
i = 9
while i >= 1 :
	kongge = 9 - i
	# 打印空格
	while kongge > 0:
		print("       ",end="")
		kongge -= 1  

	# 打印表达式
	j = 1
	while j <= i:
		print("%d*%d=%2d " % (i,j,i*j) ,end="" )
		j+=1
	
	# 打印换行
	print()
	i -=1

# 求吉利数字 100 ~ 999 之间 找 111 222 333 123 456 654 321 ... 
"""
// 可以获取一个数高位
%  可以获取一个数低位
baiwei = 345 // 100
shiwei = 345 // 10 % 10
gewei  = 345 % 10
print(gewei)
"""

# 方法一
i = 100
while i <= 999:
	baiwei = i // 100
	shiwei = i // 10 % 10
	gewei = i % 10

	if shiwei == gewei  and shiwei == baiwei :
		print(i)
	# 123
	elif shiwei == gewei - 1 and shiwei == baiwei + 1:
		print(i)
	# 987
	elif shiwei == gewei + 1 and shiwei == baiwei - 1:
		print(i)
	i +=1

# 方法二
print("<====>")
i = 100
while i <= 999:
	strvar = str(i)
	# print(strvar, type(strvar))
	gewei = int(strvar[-1])
	shiwei = int(strvar[1])
	baiwei = int(strvar[0])
	if shiwei == gewei  and shiwei == baiwei :
		print(i)
	# 123
	elif shiwei == gewei - 1 and shiwei == baiwei + 1:
		print(i)
	# 987
	elif shiwei == gewei + 1 and shiwei == baiwei - 1:
		print(i)
	
	i +=1

# 方法三
print("<====>")
i = 100
while i <= 999:
	strvar = str(i)
	# print(strvar, type(strvar))
	gewei = int(strvar[-1])
	shiwei = int(strvar[1])
	baiwei = int(strvar[0])

	if 2 * shiwei == gewei + baiwei and (shiwei == gewei + 1 or shiwei == gewei -1 ):
		print(i)
	elif gewei == shiwei and shiwei == baiwei:
		print(i)
	
	i +=1

# 百钱买百鸡
# 公鸡一个五块钱，母鸡一个三块钱，小鸡三个一块钱，现在要用一百块钱买一百只鸡，问公鸡、母鸡、小鸡各多少只？
"""
穷举法:把数据拿出来一个一个试
x = [1,2]
y = [3,4]
z = [5,6]
x+y+z = 10
1 + 3 + 5 = 9
1 + 3 + 6 = 10 bingo
1 + 4 + 5 = 10 bingo
1 + 4 + 6 = 11
2 + 3 + 5 = 10 bingo
2 + 3 + 6 = 11
2 + 4 + 5 = 11
2 + 4 + 6 = 12
"""

"""
公鸡 : x  母鸡 : y  小鸡: z
鸡的数量:x + y + z = 100
鸡的价格:5 * x + 3 * y + 1/3*z = 100   
"""

x = 0
while x <= 20:
	
	y = 0
	while y <= 33:
		
		z = 0
		while z <= 100:
			
			if x+y+z == 100 and 5*x + 3 * y + 1/3*z == 100 :
				print(x,y,z)
			z += 1	
		
		y +=1
	
	x += 1





