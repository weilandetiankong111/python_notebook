# ### 操作类 operation
import os
import pickle
import random
from .card import Card
from .person import Person


class Operation():

	def __init__(self):
		# 加载user.txt文件数据
		self.load_user()
		# 加载userid.txt文件数据
		self.load_userid()
		
		
	# 加载user.txt文件数据
	def load_user(self):
		if os.path.exists("user.txt"):
			with open("user.txt",mode="rb") as fp:
				self.user_dict = pickle.load(fp)
		else:
			# 设置空字典
			self.user_dict = {}
			
		print(self.user_dict)
			
	# 加载userid.txt文件数据
	def load_userid(self):
		if os.path.exists("userid.txt"):
			with open("userid.txt",mode="rb") as fp:
				self.user_id_dict = pickle.load(fp)
		else:
			# 设置空字典
			self.user_id_dict = {}
			
		print(self.user_id_dict)			
			
	# 保存退出
	def save(self):	
		# 存储user_dict 字典
		with open("user.txt",mode="wb") as fp:
			pickle.dump(self.user_dict,fp)
	
		# 存储user_id_dict 字典
		with open("userid.txt",mode="wb") as fp:
			pickle.dump(self.user_id_dict,fp)
			
	# 注册用户	
	def register(self):
		# 获取用户名
		name = input("请输入您的姓名:")
		# 获取身份证号
		userid = input("请输入您的身份证号:")
		# 获取手机号
		phone = input("请输入您的手机号:")
		# 获取密码
		password = self.get_pwd("请输入您的密码:","请确认您的密码:")
		# 获取卡号
		cardid = self.get_cardid()
		# 卡内默认余额 10元
		money = 10
		# 创建一张卡
		card = Card(cardid,password,money)
		# 创建一个用户
		user = Person(name,userid,phone,card)
		# 存储数据到 user_dict    卡号:用户对象
		self.user_dict[cardid] = user
		# 存储数据到 user_id_dict 身份证号:卡号
		self.user_id_dict[userid] = cardid
		print("恭喜{}开卡成功,您的卡号为:{},卡内余额{}元".format(name,cardid,money))
		

	# 获取密码
	def get_pwd(self,name1,name2):
		while True:
			pwd1 = input(name1)
			pwd2 = input(name2)
			if pwd1 == pwd2:
				return pwd1
			else:
				print("两次密码不一致,请重新输入")
				
	# 获取卡号
	def get_cardid(self):
		while True:
			cardid = str(random.randrange(100000,1000000))
			if cardid not in self.user_dict:
				return cardid
			
			
	def query(self):
		# 1.获取这张卡的相关信息
		card = self.get_card_info()
		if not card:
			print("抱歉,您的这张卡不存在")
		else:
			if card.islock:
				print("抱歉,您的卡已经被锁了")
			else:
				if self.check_pwd(card):
					# 显示卡内余额
					print("您的卡内余额是{}元".format(card.money))
				
	
	# 用的信息
	def get_card_info(self):
		cardid = input("请输入您的卡号:")
		if cardid not in self.user_dict:
			return False
		else:
			# 通过卡号 -> 用户对象
			user = self.user_dict[cardid]
			return user.card
			
			
	def check_pwd(self,card):
		
		times = 1
		while times <= 3:
			pwd = input("请输入您的密码")
			if pwd == card.password:
				return True
			else:
				#剩余次数 = 总次数 - 使用次数
				print("密码错误~ , 您还剩下{}次机会".format(3 - times))
				if times == 3:
					card.islock = True
					print("抱歉,密码输错三次,卡被锁定,请联系管理员.")
			
			
			times+=1
			
			
			

		









		
			