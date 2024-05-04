# a
with open("a1.txt",mode="r",encoding="utf-8") as fp:
    print(fp.read())
# b
with open("a1.txt",mode="a+",encoding="utf-8") as fp:
    fp.write("\n\t信不信由你，反正我信了")
    
# c
with open("a1.txt",mode="a+",encoding="utf-8") as fp:
    print(fp.read())
    fp.write("\n\t信不信由你，反正我信了")
    
# d
strvar ="""    
    每天坚持一点，
	每天努力一点，
	每天多思考一点，
	慢慢你会发现，
	你的进步越来越大。
"""
with open("a1.txt",mode="w+",encoding="utf-8") as fp:
    fp.write(strvar)
    
# e
with open("a2.txt",mode="r+",encoding="utf-8") as fp:
    lst = fp.readlines()    
    print(lst) # ['\t键盘敲烂,\n', '\t月薪过万.\n', '\t键盘落灰,\n', '\t狗屎一堆.\n']
    lst.insert(-2,"\t年薪百万\n")
    
with open("a3.txt",mode="w+",encoding="utf-8") as fp:
    fp.writelines(lst)
    
# #####################################
# a
with open("a4.txt",mode="r+",encoding="utf-8") as fp:
    print(fp.readable())
    print(fp.writable())
    
# b
with open("a4.txt",mode="r",encoding="utf-8") as fp:
    for i in fp:
        print(i)

# c
with open("a4.txt",mode="r",encoding="utf-8") as fp:
    lst = fp.readlines()
    for i in lst:
        print(i)
    
# d
with open("a4.txt",mode="r",encoding="utf-8") as fp:
    print(fp.read(4))
    
# e
with open("a4.txt",mode="r",encoding="utf-8") as fp:
    print(fp.readline().strip())
    
# f
print("<====>")
with open("a4.txt",mode="r",encoding="utf-8") as fp:
    lst = fp.readlines()
    for i in lst[-2:]:
        print(i)
    
# g
with open("a4.txt",mode="a+",encoding="utf-8") as fp:
    fp.write("\n老男孩教育")
    fp.seek(0)
    print(fp.read())
    
# h
with open("a4.txt",mode="r+",encoding="utf-8") as fp:
    fp.truncate(24)
    
    
# #####################################
"""
[
'\tapple 10 3\n', 
'\ttesla 100000 1\n', 
'\tmac 3000 2\n', 
'\tlenovo 30000 3\n', 
'\tchicken 10 3'
]
"""
print("><======================?")
lst_new = []
total = 0
with open("a5.txt",mode="r+",encoding="utf-8") as fp:
    lst = fp.readlines()
    # print(lst)
    for i in lst:
        # 定义空字典
        dic = {}
        # 取出字符串两边的空白
        lst = i.strip().split()
        print(lst)
        # 拼装字典
        dic["name"] = lst[0]
        dic["price"] = int(lst[1])
        dic["amount"] = int(lst[2])
        
        # 累计当前商品的价格总数
        res = dic["price"] * dic["amount"]
        # 累计所有的商品价格总数
        total += res
        # 把当前商品的信息字典追加到列表中
        lst_new.append(dic)
    
print(total)
print(lst_new)
"""
[
{'name': 'apple', 'price': 10, 'amount': 3}, 
{'name': 'tesla', 'price': 100000, 'amount': 1}, 
{'name': 'mac', 'price': 3000, 'amount': 2}, 
{'name': 'lenovo', 'price': 30000, 'amount': 3}, 
{'name': 'chicken', 'price': 10, 'amount': 3}
]
"""

# 4.
def func(container):
    return len(container)
res = func((1,2,3,4))
print(res)

# 5.
def func(container):
    # 方法一
    # for i in range(1,len(container),2):
        # print(container[i])
        
    # 方法二
    for i in container[1::2]:
        print(i)
        
func([11,22,33,44,55,666])

# 6.
def func(container):
    """
    # 方法一
    strvar = ""
    for i in container:
        strvar += str(i) + "_"
    return strvar.rstrip("_")
    """
    
    # 方法二
    lst_new = []
    for i in container:
        lst_new.append(str(i))
    return "_".join(lst_new)
    

container = [1,2,3,4,5]
res = func(container)
print(res)


# 7
strvar = "k:1|k1:2|k2:3|k3:4" 

def func(strvar):
    '''
    # 方法一
    lst = strvar.split("|")
    print(lst) # ['k:1', 'k1:2', 'k2:3', 'k3:4']
    dic = {}
    for i in lst:
        k,v = i.split(":")
        dic[k] = v
        """
        ['k', '1']
        ['k1', '2']
        ['k2', '3']
        ['k3', '4']
        """
    return dic
    '''
    # 方法二
    lst = strvar.split("|")
    lst_new = []
    for i in lst:
        lst_new.append(i.split(":"))
    return dict(lst_new)
    
    
print(func(strvar))
    
# 8
li= [11,22,33,44,55,66,77,88,99,90]
lst1 = []
lst2 = []
dic = {"k1":None,"k2":None}
def func(li):
    for i in li:
        if i > 66:
            lst1.append(i)
        elif i < 66:
            lst2.append(i)
    dic["k1"] = lst1
    dic["k2"] = lst2
    return dic
        
res = func(li)
print(res)  

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    