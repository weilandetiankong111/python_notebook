from package.view import View
from package.operation import Operation


class Main():

	def run():
		if View.login():
			obj = Operation()
			while True:	
				choice = input('请输入需要办理的业务:')
				if choice == '1':
					# 开户
					print('★★★★★★欢迎使用开户功能★★★★★★')
					obj.register()
				elif choice == '2':
					# 查询
					print('★★★★★★欢迎使用查询功能★★★★★★')
					obj.query()
				elif choice == '3':
					# 存钱
					print('★★★★★★欢迎使用存钱功能★★★★★★')
					obj.save_money()
				elif choice == '4':
					# 取钱
					print('★★★★★★欢迎使用取钱功能★★★★★★')
					obj.get_money()
				elif choice == '5':
					print('★★★★★★欢迎使用转账功能★★★★★★')
					obj.trans_money()
					# 改密
				elif choice == '6':
					print('★★★★★★欢迎使用改密功能★★★★★★')
					obj.change_pwd()
					# 锁卡
				elif choice == '7':
					print('★★★★★★欢迎使用锁卡功能★★★★★★')
					obj.lock()
					# 解卡
				elif choice == '8':
					print('★★★★★★欢迎使用解卡功能★★★★★★')
					obj.unlock()
				elif choice == '9':
					print('★★★★★★欢迎使用补卡功能★★★★★★')
					obj.new_card()
				elif choice == '0':
					print('★★★★★★欢迎使用销卡功能★★★★★★')
					obj.del_user()
				elif choice == '*':
					obj.save()
					print('★★★★★★★欢迎下次光临★★★★★★')
					print('★★★★★★请收好您的卡片★★★★★★★')
					break
			

if __name__ == '__main__':
	Main.run()
