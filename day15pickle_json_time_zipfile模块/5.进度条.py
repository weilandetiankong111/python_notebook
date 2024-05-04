# ### 进度条
import time
"""
[###################################] 100%
[##############                     ] 40%
[#############################      ] 80%
"""
# (1) 定义进度条样式
"""
print("[%-50s]" % ("#"))
print("[%-50s]" % ("######################"))
print("[%-50s]" % ("##############################################"))
"""

# (2) 让进度条动起来
"""
strvar = ""
for i  in range(50):
	time.sleep(0.1)
	strvar += "#"
	print("\r[%-50s]" % (strvar) , end="")
"""

# (3) 加上百分比
# 显示进度条
def myprocess(percent):
	if percent > 1:
		percent = 1
	
	# 打印对应的#号数量 * "#" => 字符串#号效果
	strvar = int(percent * 50) * "#"
	# 进行打印 %% => % 
	print("\r[%-50s] %d%%" % (strvar , percent * 100) , end="")

# 接受数据
recv_size = 0
total_size = 1000
while recv_size < total_size:
	time.sleep(0.01)
	recv_size += 10
	
	percent = recv_size/total_size # 0.5 
	myprocess(percent)
	

		
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

