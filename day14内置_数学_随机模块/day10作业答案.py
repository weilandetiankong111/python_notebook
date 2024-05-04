# # 1.定义函数:接收任意个参数,打印其中的最小值
def func(*args):
	lst = []
	for i in args:
		if isinstance(i , (float,int)):
			lst.append(i)
	print(lst)
	return lst[0]
res = func(-100,1,2,423,"sdf")
print(res)

# 2.定义函数:传入一个参数n，返回n的阶乘(5! = 5*4*3*2*1)
def func(n):
	total = 1
	for i in range(n,0,-1):
		total *= i
	return total
			
print(func(5))

# 3.写函数,传入函数中多个实参(均为可迭代对象如字符串,列表,元祖,集合等)
# # 将容器中的每个元素依次添加到新的列表中返回
#例:传入函数两个参数[1,2,3] (22,33)最终args为(1,2,3,22,33)
# 方法一
def func(*args):
	lst =[]
	for i in args:
		for j in i:
			lst.append(j)
	return lst

res = func([1,2,3],(5,6,7),"abc")
print(res)

# 方法二
def func(*args):
	return list(args)

res = func(*[1,2,3],*(5,6,7),*"abc")
print(res)


# 4.写函数，用户传入要修改的文件名，与要修改的内容，执行函数，修改操作
# 方法一
def func(filename,str1,str2):
	with open(filename,mode="r+",encoding="utf-8") as fp:
		strvar = fp.read()
		print(strvar)
		res = strvar.replace(str1,str2)
	
	with open(filename,mode="w+",encoding="utf-8") as fp:
		fp.write(res)

func("ceshi2.py","内置函数","外置函数")

# 方法二
def func(filename,str1,str2):
	with open(filename,mode="r+",encoding="utf-8") as fp:
		strvar = fp.read()
		res = strvar.replace(str1,str2)
		# print(fp.tell())
		fp.seek(0)
		# 清空
		fp.truncate()
		fp.write(res)

func("ceshi2.py","外置函数","内置函数")


# 5.写函数，计算传入字符串中【数字】、【字母】、【空格] 以及 【其他】的个数
# 方法一
def func(strvar):
	dic = {"num":0,"word":0,"space":0,"other":0}
	for i in strvar:
		if i.isdecimal():
			dic["num"] += 1 # dic["num"] = dic["num"] + 1
		elif i.encode().isalpha():
			dic["word"] += 1
		elif i.isspace():
			dic["space"] += 1
		else:
			dic["other"] += 1
	
	return dic
	


# strvar = input("请输入字符串")
# print(func(strvar))
"""
print("你".isalpha())

# 中文 => False
print("你".encode().isalpha())
# 字母 => True
print("a".encode().isalpha())
"""

# 方法二
def func(strvar):
	dic = {"num":0,"word":0,"space":0,"other":0}
	lst = []
	for i in range(97,123):
		lst.append(chr(i))
		lst.append(chr(i-32))
	for i in strvar:
		if i in "0123456789":
			dic["num"] += 1
		elif i in lst:
			dic["word"] += 1
		elif i == " ":
			dic["space"] += 1
		else :
			dic["other"] += 1
	return dic
# strvar = input("请输入字符串")
# print(func(strvar))

# 6.写函数，检查字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，返回处理后的结果.
	#例:参数为:dic = {"k1": "v1v1", "k2": [11,22,33,44]}

def func(dic):
	if isinstance(dic,dict):
		for k,v in dic.items():
			print(k,v)
			dic[k] = v[:2]
		return dic
		
	else:
		return "不是字典"
	
dic = {"k1": "v1v1", "k2": [11,22,33,44]}
print(func(dic))
print(func([1,23,42,34,23,4234]))


# 7传入多个容器类型数据,计算所有元素的个数
def func(*args):
	total = 0 
	for i in args:
		print(i)
		total += len(i)
	return total
res = func("123",[5,6,7],("你好","123423"))
print(res)

# 改造,不去判断字符串本身的长度
def func(*args):
	total = 0 
	for i in args:
		print(i)
		if isinstance(i,str):
			total += 1
		elif isinstance(i,(tuple,list,set,dict)):
			total += len(i)
	return total

res = func("123",[5,6,7],("你好","123423"))
print(res)

























