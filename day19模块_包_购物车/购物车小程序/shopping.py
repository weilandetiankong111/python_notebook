# ### 购物车小程序
"""
	# 1.充值
	# 2.加载中...
	# 3.获取数据
	# 4.展现商品
	# 5.购买商品
"""
import time
import json
# 充值的价格
money = 0
# 购物车字典
car = {}

"""
2 <=> 商品的详情 捆绑
购物车的数据形式:
{
	2:{'name': '鼠标', 'price': 10},
	3:{'name': '游艇', 'price': 20},
}
"""

# 充值
def recharge():
	global money
	while True:
		num = input("请充值吧,大哥")
		if num.isdecimal():
			money = int(num)
			print("恭喜你~ 充值成功{}元人民币".format(money))
			break			
		else:
			print("充值失败,非数字.")

# 进度条
def myprocess(percent):
	if percent > 1:
		percent = 1

	strvar = int(percent * 50) * "#"
	print("\r[%-50s] %d%%" % (strvar , percent * 100) , end="")

# 执行进度条
def exe_process():
	recv_size = 0
	total_size = 1000
	while recv_size < total_size:
		time.sleep(0.01)
		recv_size += 10	
		percent = recv_size/total_size 
		myprocess(percent)

# 加载中
def loading():
	print("加载商品中 ... ")
	exe_process()
	print()

# 读取数据
def read_data(filename):
	lst = []
	with open(filename , mode="r+" ,encoding="utf-8") as fp:
		for i in fp:
			dic = json.loads(i)
			# print(dic, type(dic))
			lst.append(dic)
	return lst

def show_goods(data):
	"""
	[
		{'name': '电脑', 'price': 1999}, 
		{'name': '鼠标', 'price': 10}, 
		{'name': '游艇', 'price': 20}, 
		{'name': '美女', 'price': 998}, 
		{'name': '风油精', 'price': 30}
	]
	"""
	strvar = "商品名称".center(18)
	print("序号"+strvar+"价格")
	for k,v in enumerate(data,start=1):
		# print(k,v)
		v["num"] = k
		print(  "{v[num]:<10}{v[name]:<12}{v[price]}".format(v=v)   )

def error():
	strvar = """
**************************************************
*           您输入的选项不存在 , 请重新输入          *
**************************************************	
	"""
	print(strvar)
	time.sleep(1)

def add_car(num,data):
	# print(num)
	# print(data)
	"""
	car = {
		2:{'name': '鼠标', 'price': 10},
		3:{'name': '游艇', 'price': 20},
	}
	"""
	# 如果第一次购买商品,键一定不再字典中
	if num not in car:
		car[num] = {
		"name":data[num-1]["name"],
		"price":data[num-1]["price"],
		"account":1		
		}		
	else:
		car[num]["account"] += 1
	# print(car) # {1: {'name': '电脑', 'price': 1999, 'account': 1}}
	
def show_car(num):
	print("*" * 50)
	print("您选择的商品具体信息:")
	print("*-商品名称:{}".format(car[num]["name"]))
	print("*-商品单价:{}".format(car[num]["price"]))
	print("*-商品数量:{}".format(car[num]["account"]))
	print("已成功添加到购物车~ 请继续shopping ~")
	print("*" * 50)

def balance():
	total = 0
	print("[-------------------您购物车的具体商品如下:-------------------]")
	for k,v in car.items():
		v["num"] = k
		v["mysum"] = v["price"] * v["account"] 
		total += v["mysum"]
		print("序号: {v[num]} 商品名称:{v[name]} 商品单价:{v[price]} 商品数量:{v[account]} 此商品总价:{v[mysum]}".format(v=v))
	return total
	# print(i) # (2, {'name': '鼠标', 'price': 10, 'account': 1})
	# print("序号: 2 商品名称:鼠标 商品单价:10 商品数量:1 此商品总价:10")
	

def success(total,money):
	print("正在结算数据中 ... ")
	exe_process()
	print("请稍后...")
	print("[一共：{}元]".format(total))
	# 剩余金额 = 充值金额-花费金额
	print("[您已经成功购买以上所有商品 , 余额还剩{}元，感谢您下次光临~]".format(money-total))
	time.sleep(1)
	
	
def del_goods(total,money):
	print("余额不足，还差{}元，请忍痛割爱，删除某些商品".format(total-money))
	num = input("[-------------------请输入要删除的商品序号:-------------------]")
	if num.isdecimal():
		num = int(num)
		if num in car:
			# 删除商品数量
			car[num]["account"] -= 1
			# 检测商品数量是不是0,如果是把该条商品信息从购物车中扣掉;
			if not car[num]["account"]:
				car.pop(num)
		else:
			error()
	else:
		error()
	
def myexit():
	print("[============== 欢迎下次光临: ==============]")
	time.sleep(1)
	
def main():
	# 1.充值
	recharge()	
	# 2.加载中...
	loading()
	# 3.获取数据
	data = read_data("shopping_data.json")
	# 4.展现商品
	show_goods(data)
	# 5.购买商品
	sign = True
	while sign:
		num= input("请输入您要购买的商品:")
		# 1.添加商品到购物车
		if num.isdecimal():
			num = int(num)
			if 1 <= num <= len(data):
				# 把要买的商品添加到购物车
				add_car(num,data)
				# 展现一下购买的商品详情
				show_car(num)
			else:
				error()
		# 2.结算商品
		elif num.upper() == "N":
			while True:
				# 结算出总价格
				total = balance()
				print(total)
				if total > money:
					# 删除商品
					del_goods(total,money)
				else:
					# 正常结算
					success(total,money)
					sign = False
					break
			
		# 3.退出购物
		elif num.upper() == "Q":
			myexit()
			sign = False
		else:
			error()		
	


main()






