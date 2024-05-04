
# ### Number 类型的强制转换 (int float complex bool)

# int 强制把数据变成整型
"""int float bool 纯数字字符串"""
var1 = 13
var2 = 5.67
var3  = True
var4 = "123456"
var5 = "123abc"
var6 = 3+5j

res = int(var2)
res = int(var3) # True  => 1
res = int(False)# False => 0
res = int(var4)
# res = int(var5) error
# res = int(var6) error
print(res , type(res))

# float 强制把数据变成小数
"""int float bool 纯数字字符串"""
res = float(var1)
res = float(var3) # True  => 1.0
res = float(False)# False => 0.0
res = float(var4) # 123456.0 
print(res , type(res))

# complex 强制把数据变成复数
"""int float bool 纯数字字符串 complex"""
res = complex(var1) # 添加0j 表达复数
res = complex(var2)
res = complex(var3)  # True => 1+0j
res = complex(False) # False => 0j
res = complex(var4)  # 123456+0j
print(res , type(res))

# bool 强制把数据变成布尔型 (布尔型为假的十中情况)
"""布尔型可以强转一切数据类型"""
""" 0 , 0.0 , False , 0j '' [] () set() {} None """
res = bool(None)
print(res , type(res))

# 初始化变量时,不清楚用什么值,无脑写上None
"""None 代表空的,代表什么也没有,一般用于初始化变量"""
a =None
b =None


"""
默认转换成当前数据类型的一个值
int() float() complex() bool()
"""
res = bool() 
print(res , type(res))



# 额外的扩展
"""
strvar = "123"
strvar = "3.134"
strvar = "5+3j"
# res = int(strvar)
# print(res,type(res))

# res = float(strvar)
# print(res,type(res))

# res = complex(strvar)
# print(    res,type(res)    )
"""






























