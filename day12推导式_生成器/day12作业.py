# 1.用推导式写如下程序
(1)构建如下列表：[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
(2)lst = ['alex', 'WuSir', '老男孩', '神秘男孩'] 将lst构建如下列表:['alex0', 'WuSir1', '老男孩2', '神秘男孩3']
(3)构建如下列表：[(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
(4)求出50以内能被3整除的数的平方，并放入到一个列表中。
(5)M = [[1,2,3],[4,5,6],[7,8,9]], 把M中3,6,9组成新列表
(6)构建如下列表：['python1期', 'python2期', 'python3期', 'python4期', 'python6期', 'python7期', 'python8期', 'python9期', 'python10期']
(7)过滤掉长度小于3的字符串列表 , 并转换成大写字母
(8)除了大小王,里面有52项,每一项是一个元组,请返回如下扑克牌列表[('红心'，'2'),('草花'，'J'), …('黑桃'，'A')] 

# 2.用推导式写如下程序
lst1 = {
		'name':'alex',
		'Values':[
			{'timestamp': 1517991992.94,'values':100,},			 
			{'timestamp': 1517992000.94,'values': 200,},			
			{'timestamp': 1517992014.94,'values': 300,},			 
			{'timestamp': 1517992744.94,'values': 350},			 
			{'timestamp': 1517992800.94,'values': 280}			 
		]
	}
将lst1 转化成如下lst2:
lst2 = [
	[1517991992.94, 100], 
	[1517992000.94, 200], 
	[1517992014.94, 300], 
	[1517992744.94, 350], 
	[1517992800.94, 280]
]

# 3.读取一个文件所有内容,通过生成器调用一次获取一行数据.
# 4.将普通求和函数改写成yield写法
def add(a,b):                     
    return a + b