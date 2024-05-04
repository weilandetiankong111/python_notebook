# ### 操作类 operation
import re,time
import os,pickle
import random
from .card import Card
from .person import Person

class Operation():
	def __init__(self):
		# 加载user.txt文件数据
		self.load_user()
		self.load_userid()
		
	# user.txt=>{卡号:用户对象}{"555666": 用户对象}=>user_dict
	
	# 加载user.txt文件数据
	def load_user(self):
			if os.path.exists('user.txt'):
				with open('user.txt',mode='rb') as fp:
					self.user_dict =  pickle.load(fp)
			else:
				self.user_dict = {}
			print(self.user_dict)

	# userid.txt=>{身份证:卡号}=>{"111": "555666" , "222":"777888"} 
	# =>user_id_dict
	
	# 加载userid.txt文件数据
	def load_userid(self):
		if os.path.exists('userid.txt'):
			with open('userid.txt',mode='rb') as fp:	
				self.user_id_dict = pickle.load(fp)
		else:
			self.user_id_dict = {}
		print(self.user_id_dict)
	
	# 保存退出
	def save(self):	
		with open('user.txt',mode='wb') as fp:
			pickle.dump(self.user_dict,fp)
		with open('userid.txt',mode='wb') as fp:
			pickle.dump(self.user_id_dict,fp)
	
	# 1.注册
	def register(self):
		# 输入姓名
		name = self.get_name()
		while True:
			userid = self.get_userid()
			if userid in self.user_id_dict:
				print('这张身份证已经注册过银行卡~~~~')
			else:
				phone = self.get_phone()
				password = self.get_pwd('请输入您的密码:','请确认您的密码:')
				cardid = self.get_cardid()
				money = 10
				# 创建一张卡对象
				card = Card(cardid,password,money)
				# 创建一个用户
				user = Person(name,userid,phone,card)
				# 存储数据到 user_dict    卡号:用户对象
				self.user_dict[cardid] = user
				# 存储数据到 user_dict    卡号:用户对象
				self.user_id_dict[userid] = cardid
				print('恭喜{}开卡成功,您的卡号为:{},卡内余额{}元'.format(name,cardid,money))
				break
			
	# 获取姓名:
	def get_name(self):
		while True:
			name = input('请输入您的姓名:')
			obj = re.search(r'^[\u4E00-\u9FA5A-Za-z\s]+(·[\u4E00-\u9FA5A-Za-z]+)*$', name)
			if obj is None:
				print('姓名格式不正确,需要更改:')
			else:
				return obj.group()
	
	# 获取身份证号:
	def get_userid(self):
		while True:
			userid = input('请输入您的身份证号:')
			obj = re.search(r'(?<!\d)(?:(?:([1-9]\d{5}(?:18|19|(?:[23]\d))\d{2}(?:(?:0[1-9])|(?:10|11|12))(?:(?:[0-2][1-9])|10|20|30|31)\d{3}[0-9Xx])(?!\d))|([1-9]\d{5}\d{2}(?:(?:0[1-9])|(?:10|11|12))(?:(?:[0-2][1-9])|10|20|30|31)\d{3}))(?!\d)',userid)
			if obj is None:
				print('身份证格式不正确,需要更改:')
			else:
				return obj.group()
				
	# 获取手机号
	def get_phone(self):
		while True:
			phone = input('请输入您的手机号:')
			obj = re.search(r'^(((13[0-9]{1})|(15[0-9]{1})|(18[0-9]{1}))+\d{8})$',phone)
			if obj is None:
				print('电话号码格式不正确,需要更改:')
			else:
				return obj.group()
	
	# 获取密码
	def get_pwd(self,name1,name2):
		while True:
			pwd1=  input(name1)
			obj = re.search(r"^(\w{6})$",pwd1)
			if obj is None:
				print('密码格式不正确:')
				print('密码长度6位不能空,由字母数字下划线组成,且不能全为数字')
			else:
				pwd1 = obj.group()
				if pwd1.isdecimal():
					print('密码不能为6位纯数字:')
				else:	
					pwd2 = input(name2)
					if pwd1 == pwd2:
						return pwd1
					else:
						print('两次密码不一致,请重新输入')
	
	# 获取卡号
	def get_cardid(self):
		while True:
			cardid = str(random.randrange(100000,1000000))
			if cardid not in self.user_dict:
				return cardid
	
	# 2.查询			
	def query(self):
		# 1.获取这张卡的相关信息
		card = self.get_card_info()
		if not card:
			print('抱歉,您的这张卡不存在')
		else:
			if card.islock:
				print('抱歉,您的卡已经被锁了')
			else:
				if self.check_pwd(card):
					print('您的卡内余额是{}元'.format(card.money))	

	# 卡的信息
	def get_card_info(self):
		cardid = input('请输入您的卡号:')
		if cardid not in self.user_dict:	
			return False
		else:
			# 通过卡号 -> 用户对象
			user = self.user_dict[cardid]
			return user.card
			
	def check_pwd(self,card):
		times = 1
		while times <= 3:
			pwd = input('请输入您的密码:')
			if pwd == card.password:
				return True
			else:
				print('密码错误~您还剩{}次机会'.format(3-times))
				if times == 3:
					card.islock = True
					print('抱歉,密码输错三次,卡被锁定,请联系管理员.')
			times += 1
	
	# 3.存钱
	def save_money(self):
		card  = self.get_card_info()
		if not card:
			print('抱歉,您的这张卡不存在')
		else:
			if card.islock:
				print('此卡已经被冻结了,请联系管理员~~~')
			else:
				user = self.user_dict[card.cardid]
				key_sure = input('确认存款请按1,任意键返回上一层:')
				if key_sure == '1':
					while True:
						str_money = input('请将您的现金放在卡槽内:')
						obj = re.search(r'^(\d)+(00)$', str_money)
						if obj is None:
							print('咱们只能存100元的毛爷爷~~')
						else:	
							money = int(str_money)
							card.money += money
							time.sleep(1)
							print('★'*30)
							print('★★★★★成功存入了{}元人民币★★★★★'.format(money))
							print('★★★★★您的卡内余额为{}元人民币★★'.format(card.money))
							print('★'*30)
							break
	# 4.取钱
	def get_money(self):
		card  = self.get_card_info()
		if not card:
			print('抱歉,您的这张卡不存在')
		else:
			if card.islock:
				print('此卡已经被冻结了,请联系管理员~~~')
			else:
				user = self.user_dict[card.cardid]
				key_sure = input('确认取款请按1,任意键返回上一层:')
				if key_sure == '1':
					print('★'*30)
					print('★★★★★您的卡内余额为{}元人命币★★'.format(card.money))
					print('★'*30)		
					str_money = input('请输入您的取的金额:')
					obj = re.search(r'^(\d)+(00)$', str_money)
					if obj is None:
						print('咱们能取100元的毛爷爷~~')
					else:
						money = int(str_money)
						if card.money >= money:
							card.money -= money
							time.sleep(1)
							print('★'*30)
							print('★★★★★成功取了{}元人民币★★★★★★★★'.format(money))
							print('★★★★★您的卡内余额为{}元★★★★★★'.format(card.money))
							print('★'*30)
						else:
							print('您卡内余额不足~~~')

	# 5.转账
	'''
	转账:把一个卡里的钱转到其他卡内 
	(卡是否存在,是否冻结,对方账户是否存在,转账的金额是否正确)
	'''
	def trans_money(self):
		# 返回user.card对象
		card = self.get_card_info()
		if not card:
			print('抱歉,您的这张卡不存在')
		else:
			if card.islock:
				print('此卡已经被冻结了,请联系管理员~~~')
			else:
				cardid = card.cardid
				user = self.user_dict[cardid]
				print("账户：%s 余额：%d" % (card.cardid,int(card.money)))
				other_cardid = input('请输入对方卡号:')
				# 判断是否是给自己转账
				if other_cardid == cardid:
					print('不能给自己转账~~~')

				else:
					if other_cardid in self.user_dict:
						other_user = self.user_dict[other_cardid]
						if other_user.card.islock:
							print('对方卡号已经被冻结了,请跟对方确认卡号信息~~~')
						else:	
							while True:
								trans_rmb = input('请输入转账金额:')
								if trans_rmb.isdecimal():
									trans_rmb = int(trans_rmb)
									if trans_rmb > card.money:
										print('您的卡内余额不足,重新输入')
									else:
										card.money -= trans_rmb
										other_user.card.money += trans_rmb
										print('您的卡内余额还有{}'.format(card.money))
										print('对方的卡内余额还有{}'.format(other_user.card.money))
										sign = False
										break
					else:
						print('对方卡号不存在,请重新输入对方卡号....')
							
				
	# 6.改密
	def change_pwd(self):
		# 通过卡号获取卡对象
		card = self.get_card_info()
		if not card:
			print('抱歉,您的这张卡不存在')
		else:
			if card.islock:
				print('此卡已经被冻结了,请联系管理员~~~')
			else:
				key_sure = input('用旧密码改密请按1,用身份证改密请按2,任意键返回上一层:')
				if key_sure == '1':
					old_pwd = card.password
					while True:
						pwd = input('请输入您的密码:')
						if card.password == pwd:
							newpasswd = self.get_pwd("请输入新密码：","请确认新密码:")
							if old_pwd == newpasswd:
								print('新旧密码不能相同~~~')
								break
							else:
								card.password = newpasswd
								print('修改密码成功~~~')
								break
						else:
							print('密码不正确...')
							break
				elif key_sure == '2':
					# 找到身份证
					userid = self.get_userid()
					
					# 判断是否有这个身份证在user_id_dict中
					if userid in self.user_id_dict:
						cardid = self.user_id_dict[userid]
						old_pwd = card.password
						
						# 判断通过身份证找到的卡号和用户直接输入的的卡号是否一致
						if cardid == card.cardid:
							while True:
								newpasswd = self.get_pwd("请输入新密码：","请确认新密码:")
								if old_pwd == newpasswd:
									print('新旧密码不能相同~~~')
								else:
									card.password = newpasswd
									print('修改密码成功~~~')
									break
						else:
							print('身份证信息和卡信息不匹配~~~')
					else:
						print('身份证信息错误~~~')

	# 7.锁卡
	def lock(self):
		card = self.get_card_info()
		if not card:
			print('抱歉,您的这张卡不存在')
		else:
			if card.islock:
				print('此卡已经被冻结了,请联系管理员~~~~')
			else:
				key_sure = input('用密码冻结请按1,用身份证冻结请按2,任意键返回上一层:')
				if key_sure == '1':
					pwd = input('请输入您的密码:')
					if card.password == pwd:
						card.islock = True
						print('冻结成功~~~')
					else:
						print('冻结失败~~~')
				elif key_sure == '2':
					userid = input('请输入身份证号码:')
					user = self.user_dict[card.cardid]
					if user.userid == userid:
						card.islock = True
						print('冻结成功~~~')
					else:
						print('冻结失败~~~')
	
	# 8.解卡
	def unlock(self):
		card = self.get_card_info()
		if not card:
			print('抱歉,您的这张卡不存在')
		else:
			userid = self.get_userid()
			user = self.user_dict[card.cardid]
			if user.card.islock:
				if user.userid == userid:
					card.islock = False
					print('解卡成功~~~')
				else:
					print('您填写的信息不对,解卡失败~~~~')
			else:
				print('此卡没有被锁,请核对您的信息~~~')

	
	# 9.补卡
	def new_card(self):
		dic1 = {}
		dic2 = {}
		userid = self.get_userid()
		if userid in self.user_id_dict:
			cardid = self.user_id_dict[userid]
			user = self.user_dict[cardid]
			if user.card.islock:
				print('这张卡已经被冻结,请联系管理员~~~~')
			else:	
				old_pwd = user.card.password
				new_pwd = self.get_pwd('请输入您的密码:','请确认您的密码:')
				if old_pwd == new_pwd:
					print('新旧密码不能相同~~~~')
				else:
					# 利用之前的钱,新卡号,新密码,创建新的卡号.
					new_cardid = self.get_cardid()
					new_card = Card(new_cardid,new_pwd,user.card.money)
					# 更新usr_id_dict   {身份证号:卡号}
					dic1[userid] = new_cardid
					self.user_id_dict.update(dic1)
					# print(self.user_id_dict,'<========1=========>') 
					# 把新卡给用户对象
					user.card = new_card
					# 更新user_dict   {卡号:用户对象}
					dic2[new_cardid] = user
					self.user_dict.update(dic2)
					self.user_dict.pop(cardid)
					print('补卡成功,新卡号为{}'.format(new_card.cardid))
					# print('补卡成功,新卡号为{}'.format(new_cardid))
					# print(self.user_dict,'<========2=========>')
	
	# 10.销卡
	def del_user(self):
		while True:
			userid = self.get_userid()
			if userid in self.user_id_dict:
				cardid = self.user_id_dict[userid]
				name = self.user_dict[cardid].name
				self.user_id_dict.pop(userid)
				self.user_dict.pop(cardid)
				print('尊敬的{}先生/女士,您的卡号为{}的银行卡已经完成销卡~~~'.format(name,cardid))
				break   
			else:
				print('身份证号不存在~~~')
			
	
	
