# ###  客户端
import socket
sk = socket.socket()
sk.connect( ("127.0.0.1",9001)  )


# 处理收发数据逻辑
while True:
	sk.send(b'give me five')
	res = sk.recv(1024)
	print(res.decode())

sk.close()






