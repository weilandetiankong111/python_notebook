# ### 正则表达式 - 匹配多个字符

# (1) 量词
import re
'''1) ? 匹配0个或者1个a '''
print(re.findall('a?b','abbzab abb aab'))   #  ab b  ab ab b ab

'''2) + 匹配1个或者多个a '''
print(re.findall('a+b','b ab aaaaaab abb')) # ab aaaaaab ab

'''3) * 匹配0个或者多个a '''
print(re.findall('a*b','b ab aaaaaab abbbbbbb')) # b ab aaaaaab ab b b b b b b 

'''4) {m,n} 匹配m个至n个a '''
# 1 <= a <= 3 
print(re.findall('a{1,3}b','aaab ab aab abbb aaz aabb')) #aaab ab aab ab aab
# {2}  代表必须匹配2个a
print(re.findall('a{2}b','aaab ab aab abbb aaz aabb')) # aab aab aab
# {2,} 代表至少匹配2个a
print(re.findall('a{2,}b','aaab ab aab abbb aaz aabb')) # aaab aab aab


# (2) 贪婪匹配 和 非贪婪匹配
"""
贪婪匹配  : 默认向更多次匹配  (回溯算法)
非贪婪匹配: 默认向更少次匹配  (配合?号使用)    

回溯算法 : 从左向右进行匹配,直到找到最后一个,再也没有了,回头,返回上一个找到的内容
. 除了\n,匹配所有字符

非贪婪写法: 量词 + ? 

"""

# 贪婪匹配(模式)
strvar = "刘能和刘老根和刘罗锅111子222子"
lst = re.findall("刘.",strvar)
print(lst) # lst = re.findall("刘.?",strvar)

lst = re.findall("刘.?",strvar)
print(lst) # lst = re.findall("刘.?",strvar)

lst = re.findall("刘.+",strvar)
print(lst) # ['刘能和刘老根和刘罗锅111子222子']

lst = re.findall("刘.*",strvar)
print(lst) # ['刘能和刘老根和刘罗锅111子222子']

lst = re.findall("刘.{1,20}",strvar)
print(lst) # ['刘能和刘老根和刘罗锅111子222子']

lst = re.findall("刘.*子",strvar)
print(lst)

# 非贪婪匹配(模式)
lst = re.findall("刘.??",strvar)
print(lst) # ['刘', '刘', '刘']

lst = re.findall("刘.+?",strvar)
print(lst) # 刘能 刘老 刘罗

lst = re.findall("刘.*?",strvar)
print(lst) # ['刘', '刘', '刘']

lst = re.findall("刘.{1,20}?",strvar)
print(lst) # ['刘能', '刘老', '刘罗']

lst = re.findall("刘.*?子",strvar)
print(lst)


# (3) 边界符
"""
\b 本身是转义字符 退格,退到光标上一位
\b 在正则中还有边界符的意思

"word"
卡主左边界:\bw
卡主右边界:d\b
"""
strvar = "word old fuck"
# 右边界
lst = re.findall(r"d\b",strvar) # ['d', 'd']
lst = re.findall(r".*d\b",strvar) # ['word old']
lst = re.findall(r".*?d\b",strvar) # ['word old']
print(lst) 

# 左边界
lst = re.findall(r"\bw",strvar)
lst = re.findall(r"\bw.*",strvar)
lst = re.findall(r"\bw.*?",strvar)
lst = re.findall(r"\bw.*? ",strvar) # 空格在正则表达式中,不能随意加,是参与匹配的.
lst = re.findall(r"\bw\S*",strvar)

print(lst)

# (4) ^ $的使用
"""
^ 写在在字符串的开头,表达必须以某个字符开头
$ 写在在字符串的结尾,表达必须以某个字符结尾
当使用了^ $ 代表要把该字符串看成一个整体
"""

strvar = "大哥大嫂大爷"
print(re.findall('大.',strvar))  # ['大哥', '大嫂', '大爷']
print(re.findall('^大.',strvar)) # ['大哥']
print(re.findall('大.$',strvar)) # ['大爷']
print(re.findall('^大.$',strvar))# []
print(re.findall('^大.*?$',strvar))   # ['大哥大嫂大爷']
print(re.findall('^大.*?大$',strvar)) # []
print(re.findall('^大.*?爷$',strvar)) # ['大哥大嫂大爷']


print(re.findall('^g.*? ' , 'giveme 1gfive gay')) # giveme 
print(re.findall('five$' , 'aassfive')) # [five]
print(re.findall('^giveme$' , 'giveme')) # ['giveme']
print(re.findall('^giveme$' , 'giveme giveme')) # []
print(re.findall('giveme' , 'giveme giveme')) # ['giveme', 'giveme']
print(re.findall("^g.*e",'giveme 1gfive gay')) # ['giveme 1gfive']



