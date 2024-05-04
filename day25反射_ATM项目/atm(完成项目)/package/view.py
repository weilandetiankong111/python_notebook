import time
class View():
	def login():
		name = input('请输入管理员的账户:')
		pwd = input('请输入管理员密码')
		if name == 'admin' and pwd == '111':
			View.welcome_view()
			time.sleep(1)
			View.operation_view()
			return True
		else:
			print('抱歉,您的用户密码错误!')
			
	# @staticmethod	
	def welcome_view():
		strvar = '''*******************************************
*                                         *
*                                         *
*         Welcome To OldBoy Bank          *
*                                         *
*                                         *
*******************************************
		'''
		print(strvar)
		
	# @staticmethod
	def operation_view():
		strvar = '''*******************************************
*           开户(1)    查询(2)             *
*           存钱(3)    取钱(4)             *
*           转账(5)    改密(6)             *
*           锁卡(7)    解卡(8)             *
*           补卡(9)    销卡(0)             *
*                 退出(*)                 *
*******************************************
		'''
		print(strvar)
		
if __name__ == '__main__':
	View.login()










