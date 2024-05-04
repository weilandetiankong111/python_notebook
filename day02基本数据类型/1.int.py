# ### Number数字类型 (int float bool complex)
# int 整型 (正整型 0 负整型)

intvar = 100
print(intvar)

# type 获取值得类型
res = type(intvar)
print(res)

# id   获取值得地址
res = id(intvar)
print(res)

# 二进制整型
intvar = 0b110
print(intvar)
print( type(intvar) )
print(     id(intvar)    )

# 八进制整型
intvar = 0o127
print(intvar)
print(type(intvar))
print(id(intvar))

# 十六进制
intvar = 0xff
intvar = 0XFF
print(intvar)
print(type(intvar))
print(id(intvar))
"""
二进制 1 + 1 = `10
八进制 7 + 1  = 10
十六进制 f + 1 = 10
"""