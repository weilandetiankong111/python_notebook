# ### 视图类
import time
# 登录 打印欢迎界面 打印操作界面
class View():
	
	def login():
		name = input("请输入管理员的账户:")
		pwd = input("请输入管理员密码:")
		if name == "admin" and pwd == "111":
			# 打印欢迎界面
			View.welcome_view()
		
			# 延迟一秒
			time.sleep(1)
			
			# 打印操作界面
			View.operation_view()
			
			return True
		else:
			print("抱歉,您的用户密码有错误")
			
	@staticmethod
	def welcome_view():
		print("*******************************************")
		print("*                                         *")
		print("*                                         *")
		print("*         Welcome To OldBoy Bank          *")
		print("*                                         *")
		print("*                                         *")
		print("*******************************************")
				
	@staticmethod
	def operation_view():
		print("*******************************************")
		print("*           开户(1)    查询(2)             *")
		print("*           存钱(3)    取钱(4)             *")
		print("*           转账(5)    改密(6)             *")
		print("*           锁卡(7)    解卡(8)             *")
		print("*           补卡(9)    退出(0)             *")
		print("*******************************************")


		
if __name__ == "__main__":
	View.login()
	
	
	
	