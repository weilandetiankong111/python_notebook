# ### 客户端
import socket
import time 

sk = socket.socket()
sk.connect( ("127.0.0.1",9001)  )

time.sleep(2)
# 收发数据的逻辑
# 第一步,先接受接下来要发送的数据的总大小
res = sk.recv(8)
num = int(res.decode())  # 180

# 第二部,在接受真实的数据
res1 = sk.recv(num)
print(res1.decode() , "<==1===>")
res2 = sk.recv(1024)
print(res2.decode() , "<==2===>")

sk.close()
