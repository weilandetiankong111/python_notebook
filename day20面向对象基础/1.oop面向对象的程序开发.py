# ### oop 面向对象的程序开发

# (1) 类的定义

# 1
class Car:
	pass
	
# 2 推荐
class Car():
	pass
	
# 3.
class Car(object):
	pass
	
	
# (2)类的实例化
class Car():
	pass
	
obj = Car()
print(obj)

# (3)类的基本结构
"""
类中两样东西:
	(1)成员属性
	(2)成员方法
"""
class Car():
	# 成员属性
	color = "白色"
	# 成员方法
	def didi():
		print("小车会嚓嚓的叫")
		

# 语法上不报错,但是严禁使用,破坏了类中的结构,不要裸露的把判断和循环直接写在类中,而是用方法包起来
class Car():
	if 5 ==5 :
		print(11223344)
		
# (4)类的命名
"""类的命名 : 推荐使用大驼峰命名法,每个单词的首字母都要大写"""
"""
mycar => MyCar
zhangbaozhang => ZhangBaoZhang
"""
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		