# ### 用户类

class Person():
	def __init__(self,name,userid,phone,card):
		self.name = name
		self.userid = userid
		self.phone = phone
		# card属性中存放的是 卡对象 ;
		self.card = card