# ### 生成器函数
"""
# yield 类似于 return
共同点在于:执行到这句话都会把值返回出去
不同点在于:yield每次返回时,会记住上次离开时执行的位置 , 下次在调用生成器 , 会从上次执行的位置往下走
		   而return直接终止函数,每次重头调用.
yield 6 和 yield(6) 2种写法都可以 yield 6 更像 return 6 的写法 推荐使用
"""

# (1) 基本语法
def mygen():
    print("111")
    yield 1
    
    print("222")
    yield 2
    
    print("333")
    yield 3
   
# 初始化生成器函数  => 返回生成器对象 => 简称生成器
gen = mygen()

# 第一次调用
res = next(gen)
print(res)
# 第二次调用
res = next(gen)
print(res)
# 第三次调用
res = next(gen)
print(res)
# 第四次调用
"""
StopIteration error 
res = next(gen)
print(res)
"""
"""
# 第一次调用
print("111")  yield 1 保存当前第13行代码的状态,把1返回,并且等待下一次调用
# 第二次调用
从上一次保存的位置13行往下走, print("222") yield 2 保存当前第16行代码的状态,把2返回,并且等待下一次调用
# 第三次调用
从上一次保存的位置16行往下走, print("333") yield 3 保存当前第19行代码的状态,把3返回,并且等待下一次调用
# 第四次调用
因为没有更多的yield 返回数据,所有停止迭代.出现报错异常.
"""

# (2) 优化生成器代码
"""生成器应用的场景是在大数据的范围中使用,切记不可直接用for遍历所有,可能无法短时间内获取所有数据"""
def mygen():
    for i in range(1,101):
        yield i
# 初始化生成器函数 => 生成器
gen = mygen()
print("<=====>")
for i in range(30):
    num = next(gen)
    print("我的球衣号码是{}".format(num))

print("<=====>")
for i in range(40):
    num = next(gen)
    print("我的球衣号码是{}".format(num))


# (3) send的使用方式 (给上一个yield发送数据)
"""
# next和send区别:
	next 只能取值
	send 不但能取值,还能发送值
# send注意点:
	第一个 send 不能给 yield 传值 默认只能写None
	最后一个yield 接受不到send的发送值
"""
def mygen():
    print("start")
    
    res = yield "内部1"
    print(res,"<==内部==>")
    
    res = yield "内部2"
    print(res,"<==内部==>")
    
    res = yield "内部3"
    print(res,"<==内部==>")
    
    print("end")
    
# 初始化生成器函数 => 生成器
gen = mygen()
# 第一次调用生成器
"""
第一次调用生成器时,因为没有遇到yield保存的代码位置,
无法发送数据,默认第一次只能发送None
"""
res = gen.send(None)
print(res,"<==外部==>")

# 第二次调用生成器
res = gen.send("100")
print(res,"<==外部==>")

# 第三次调用生成器
res = gen.send("200")
print(res,"<==外部==>")

# 第四次调用生成器
"""
error
res = gen.send("300")
print(res,"<==外部==>")
"""
"""
使用send调用生成器,第一次发送时必须是None,因为还没有遇到yield保存的代码位置
res = gen.send(None)  走到mygen生成器函数中
print("start") 
res = yield "内部1"  执行第80行 ,保存退出,记录当前代码位置,将 "内部1" 返回
在98行接受数据  res = "内部1"  print(内部1,"<==外部==>")

第二次调用生成器
res = gen.send("100") 把100这个数据发送给上一次代码保存的位置80行进行接受. => 导致 80行 res = 100
打印81行  print(100 ,"<==内部==>")
执行83行  res = yield "内部2"  保存退出,记录当前代码位置,将 "内部2" 返回
执行102行 res = gen.send("100") => "内部2" print("内部2","<==外部==>")

....
依次类推 ... 
到第四次调用时, 因为没有更多的yield 返回数据,gen.send(300)无法接受到返回值,所以出现停止迭代 StopIteration的报错,程序终止;
"""

# (4) yield from 的使用
"""将一个可迭代对象变成一个迭代器返回	"""
def mygen():
    lst = ["张磊","李亚峰","刘一峰","王同培"]
    yield from lst
    
# 初始化生成器函数
gen = mygen()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen)) # StopIteration

# (5) 斐波那契数列
"""使用生成器分段获取所有内容,而不是一股脑的把所有数据全部打印"""
"""1 1 2 3 5 8 13 21 34 .... """

def mygen(maxval):
    a,b = 0,1
    i = 0
    while i < maxval:
        # print(b) 
        yield b
        a,b = b,a+b
        i += 1
# mygen(10)
gen = mygen(10)

# 第一次获取
for i in range(3):
    print(next(gen))

# 第二次获取
for i in range(5):
    print(next(gen))























