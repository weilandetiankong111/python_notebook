'''
card 卡类
卡号    密码      余额    锁定状态
cardid  password   money   islock
'''
class Card():
	def __init__(self,cardid,password,money):
		self.cardid = cardid
		self.password = password
		self.money = money
		self.islock = False
		






