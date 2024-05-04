import socket
import json


sk = socket.socket()
sk.connect( ("127.0.0.1",9001) )
# 处理收发数据的逻辑
def auth(opt):
	usr = input("username : >>> ").strip()
	pwd = input("password : >>> ").strip()
	dic = {"user":usr,"passwd":pwd,"operate":opt}
	str_dic = json.dumps(dic)
	
	# 发送数据
	sk.send(str_dic.encode())
	
	# 接受数据
	info = sk.recv(1024).decode()
	dic = json.loads(info)
	return dic
	
# res = auth("register")
# res = auth("login")
# print(res)


def login():
	res = auth("login")
	return res	

def register():
	res = auth("register")
	return res 
	
def myexit():
	opt_dic = {"operate":"myexit"}
	sk.send( json.dumps(opt_dic).encode() )
	exit("欢迎下次再来~ .... ")
# myexit()

# 1注册 2登录 3退出
operat_lst1 = [ ("注册",register),("登录",login),("退出",myexit)]
"""
(1, ('注册', <function register at 0x7ff1427faa60>))
(2, ('登录', <function login at 0x7ff1427fa9d8>))
(3, ('退出', <function myexit at 0x7ff1427faae8>))
"""

def main(operat_lst):
	for i,tup in enumerate(operat_lst,start=1):
		#展示界面
		print(i,tup[0])
	# 提供操作
	num = int(input("请输入要执行的选项>>>").strip())
	# print(num)
	# operat_lst[num-1][1] => register/login/myexit
	res = operat_lst[num-1][1]()
	return res

while True:
	# 开启第一套操作界面
	res = main(operat_lst1)
	print(res)



sk.close()

