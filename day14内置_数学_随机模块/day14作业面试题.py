# 1.结果
def extendList(val,list=[]):
    list.append(val)
    return list
list1 = extendList(10)   
print(list1)  
list2 = extendList(123 , []) 
print(list2)  
list3 = extendList('a')   
print(list3) 

# 2.res是多少?
def func():
	return [lambda x : i*x    for i in range(4)]
# res = [m(2) for m in func()]

# 3.打印结果是多少?
def add(a,b):                     
    return a + b
def test():                       
    for r in range(4): 
        yield r
g=test() 
for n in [2,10]:
	g=(add(n,i) for i in g)
print(list(g))
	
# 4.如何判断输入的数是质数( 1.通用方法完成 2.使用for .. else 完成 )