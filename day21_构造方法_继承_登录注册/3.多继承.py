# ### 多继承

# (1) 基本语法
class Father():
	property = "风流倜傥,才华横溢,玉树临风,才高八斗,学富五车,英姿洒窗"
	def f_hobby(self):
		print("吃喝嫖赌抽,坑蒙拐骗偷,抽烟喝酒烫头")
	
class Mother():
	property = "倾国倾城,貌美如花,沉鱼落雁,闭月羞花,婀娜多姿,前凸后翘"
	def m_hobby(self):
		print("蹦野迪,社会摇,打麻将,网红勾引小鲜肉")
		
class Daughter(Father,Mother):
	pass
	
obj = Daughter()
print(obj.property)
obj.m_hobby()


# (2) 多继承的成员调用
print("<=================>")
class Father():
	property = "风流倜傥,才华横溢,玉树临风,才高八斗,学富五车,英姿洒窗"
	def f_hobby():
		print("吃喝嫖赌抽,坑蒙拐骗偷,抽烟喝酒烫头")
	
class Mother():
	property = "倾国倾城,貌美如花,沉鱼落雁,闭月羞花,婀娜多姿,前凸后翘"
	def m_hobby(self):
		print(self.property)
		print("蹦野迪,社会摇,打麻将,网红勾引小鲜肉")

"""
(1)super本身是一个类 super()是一个对象 用于调用父类的绑定方法
(2)super() 只应用在绑定方法中,默认自动传递self对象 (前提:super所在作用域存在self)
(3)super用途: 解决复杂的多继承调用顺序	
"""
class Son(Father,Mother):
	property = "打游戏,吃小零食"
	
	def m_hobby(self):
		print("son中m_hobby方法")
	
	
	# 用类调用成员
	def skill1(self):
		Father.f_hobby()
		print(Mother.property)
		
	# 用对象调用成员
	"""self按照顺序找: 对象本身 => 类 => 父类 对应的成员 """
	def skill2(self):
		print(self.property)
		self.m_hobby()
		
	# 用super调用成员
	"""super()只调用父类的相关成员,顺带传递对象参数"""
	def skill3(self):
		print(super())
		print(super().property)
		super().m_hobby()
		

obj2 = Son()
# obj2.skill1()

obj2.property = "喜欢看lol,dnf,wow,跑跑卡丁车,ddo,霸王大陆,澄海3c"
# obj2.skill2()

obj2.skill3()







	
		
		
		