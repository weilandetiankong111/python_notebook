# ### 列表类型 list
"""特征: 可获取,可修改,有序"""
# 1.定义一个空列表
listvar = []
print( listvar , type(listvar))

# 定义普通列表
listvar = [98,6.9,True,12-90j,"赵万里"]

# 2.获取列表中的元素
# 正向索引   0  1   2     3      4
listvar =   [98,6.9,True,12-90j,"赵万里"]
# 逆向索引  -5  -4  -3     -2      -1

res = listvar[2]
res = listvar[-2]
print(res)

# 通用写法
# len 获取容器类型数据中元素个数
length = len(listvar)
res = listvar[length-1]
print(res)

# 简写
res = listvar[len(listvar)-1]
print(res)

# python逆向索引的特点,瞬间得到列表中最后一个元素
print(listvar[-1])

# 3.修改列表中的元素
listvar = [98,6.9,True,12-90j,"赵万里"]
listvar[3] = "大象"
print(listvar)

# ### 元组类型 tuple
"""特征: 可获取,不可修改,有序"""
# 定义一个元组
tuplevar = ("梦好心","王伟","安晓东","孙坚")
print(tuplevar , type(tuplevar))

# 获取元组中的元素
# 正向索引   0          1       2       3      
tuplevar = ("梦好心","王伟","安晓东","孙坚")
# 逆向索引    -4       -3      -2      -1

print(tuplevar[2])
print(tuplevar[-1])

# 修改元组中的元素 : 元组中的值不能修改
# tuplevar[0] = "萌不好心"  error

# 注意点
"""逗号才是区分是否是元组的标识符"""
tuplevar = (8.9,)
tuplevar = 8.1,
print(tuplevar)
print(type(tuplevar))

# 定义空元组
tuplevar = ()
print(type(tuplevar))

# ### 字符串类型
"""特征: 可获取,不可修改,有序"""
# 正向索引   0 1 2 3 4 5 6 7 8
strvar =    "看你,我就心跳加速"
# 逆向索引  -9-8-7-6-5-4-3-2-1

# 获取字符串中的元素
print(strvar[3])
print(strvar[-6])

# 不能修改字符串中的元素
# strvar[3] = "你" error 

print("<===============>")
strvar = ""   # 单纯定义一个字符串类型
print(strvar)
print(type(strvar))
strvar = "   " # 字符串中含有3个空格字符
print(strvar[0])
print(type(strvar))




