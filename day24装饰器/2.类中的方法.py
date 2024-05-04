# ### 类中相关方法
"""
(1)普通无参方法
(2)绑定方法: (1)绑定到对象 (2)绑定到类
(3)静态方法:无论是对象还是类调用静态方法,都不会默认传递任何参数
"""
class Dog():
	
	# 普通无参方法
	def tail():
		print("小狗喜欢摇尾巴")
	
	# 绑定到对象的方法
	def wang(self):
		print("小狗看到陌生人就叫")
		
	# 绑定到类的方法	
	@classmethod	
	def tian(cls):
		print(cls)
		print("小狗喜欢舔骨头")
		
	# 静态方法
	@staticmethod
	def jump(something):
		print("小狗喜欢接{}".format(something))
	
obj = Dog()
# 无参方法的调用
# obj.tail() #error
Dog.tail() #success


# 绑定到对象方法调用
obj.wang()
Dog.wang(obj)

# 绑定到类方法调用
"""无论对象还是类都可以调用,默认传递的是类"""
Dog.tian()
obj.tian()
print(obj.__class__)

obj.jump("飞盘")
Dog.jump("飞盘")
