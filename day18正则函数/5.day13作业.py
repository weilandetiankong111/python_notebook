# (选做)
# 1.可滑动的序列 自定义一个函数 根据参数n的值 , 变成对应个元素的容器 （zip）
"""
listvar = [1,2,3,4,5,6,7,8,9]
n = 2
listvar = [[1,2],[3,4],[5,6],[7,8]]
n = 3
listvar = [[1,2,3],[4,5,6],[7,8,9]]
n = 4
listvar = [[1,2,3,4],[5,6,7,8]]
"""

"""
lst1 = [1,3,5,7,9]
lst2 = [2,4,6,8]
zip(lst1,lst2)

"""
listvar = [1,2,3,4,5,6,7,8,9]
n = 2
lst1 = [1,3,5,7,9]
lst2 = [2,4,6,8]

# lst1 = listvar[0::2]  <=> [1,3,5,7,9]
# lst2 = listvar[1::2]  <=> [2,4,6,8]
print(lst2,"1111")
print(list( zip(lst1,lst2) ))

n = 3
lst1 = [1,4,7]
lst2 = [2,5,8]
lst3 = [3,6,9]

# lst1 = listvar[0::3]  <=> [1,4,7]
# lst2 = listvar[1::3]  <=> [2,5,8]
# lst3 = listvar[2::3]  <=> [3,6,9]
print(lst1,"2222")
print(list( zip(lst1,lst2,lst3) ))

n = 4
lst1 = [1,5]
lst2 = [2,6]
lst3 = [3,7]
lst4 = [4,8]

# lst1 = listvar[0::4]  <=> [1,5,9]
# lst2 = listvar[1::4]  <=> [2,6]
# lst3 = listvar[2::4]  <=> [3,7]
# lst4 = listvar[3::4]  <=> [4,8]
print(lst1,"3333")
print(list( zip(lst1,lst2,lst3,lst4) ))


print("<=============>")
n = 3
lst = [ listvar[i::n] for i in range(n) ]
print(lst) # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]


# zip(*lst) => zip([1,4,7],[2,5,8],[3,6,9])
it = zip(*lst)
print(list(it))


func = lambda n : zip(  *[ listvar[i::n] for i in range(n) ]   )
it = func(2)
# 把里面的元组强转成列表
print(list(map(list,it)))



# 2.青蛙跳台阶  (递归实现)
'''
一只青蛙要跳上n层高的台阶
一次能跳一级,也可以跳两级
请问这只青蛙有多少种跳上这个n层高台阶的方法?

n = 1   1 => 1
n = 2   2 => 1 1 | 2
n = 3   3 => 1 1 1 | 1 2 | 2 1 
n = 4   5 => 1 1 1 1 | 1 2 1 | 2 1 1 | 1 1 2 | 2 2
n = 5   8 => 1 1 1 1 1 | 1 1 1 2 |2 1 1 1 | 1 2 1 1  | 1 1 2 1 | 2 2 1 | 1 2 2 | 2 1 2 
'''
def func(n):
	if n == 1 or n == 2:
		return n
	return func(n-1) + func(n-2)
print(func(5))


# 3.递归反转字符串 "将14235 反转成53241" (递归实现)
# 把后面的字符往前挪动 方法一
strvar = "14235"
# lst.append(5)
# lst.append(3)
# lst.append(2)
# lst.append(4)
# lst.append(1)

# lth = 字符串的总长度  lst 要插入的列表
def func(lth,lst=[]):
	if lth == 0:
		return lst
	res = strvar[lth-1]
	lst.append(res)
	return func(lth-1)
	
lth = len(strvar)
lst = func(lth)
print(lst) # ['5', '3', '2', '4', '1']
print("".join(lst))

# 简写
def func(lth,lst=[]):
	if lth == 0:
		return "".join(lst)
	res = strvar[lth-1]
	lst.append(res)
	return func(lth-1)
print(func(lth))

# 把前面的字符往后挪动 方法二
strvar = "14235"
def func(strvar):
	if len(strvar) == 1:
		return strvar
	return func(strvar[1:])+strvar[0]
res = func(strvar)
print(res)

"""
递:
return func(4235) + 1
return func(235)  + 4
return func(35)   + 2
return func(5)    + 3
return 5

归:
return func(5)    + 3 => 5 + 3
return func(35)   + 2 => 5 + 3 + 2
return func(235)  + 4 => 5 + 3 + 2 + 4
return func(4235) + 1 => 5 + 3 + 2 + 4 + 1
return 5 + 3 + 2 + 4 + 1
"""




# 4.斐波那契数列用尾递归实现
a,b = 0,1
i = 0
n = 5
while i < n:
	print(b)
	a,b = b,a+b
	i +=1
	

a,b = 0,1
n = 5
while n > 0:
	print(b)
	a,b = b,a+b
	n -= 1

print("<==============>")
def func(n,a=0,b=1):
	if n == 1:
		return b
	return func(n-1,b,a+b)
	
print(func(6))









