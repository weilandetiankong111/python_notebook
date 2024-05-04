# ### 信号量 Semaphore 本质上就是锁,只不过是多个进程上多把锁,可以控制上锁的数量
"""Semaphore = lock + 数量 """
from multiprocessing import Semaphore , Process
import time , random
"""
	# 同一时间允许多个进程上5把锁
	sem = Semaphore(5)
	#上锁
	sem.acquire()
	print("执行操作 ... ")
	#解锁
	sem.release()
"""

def singsong_ktv(person,sem):
	# 上锁
	sem.acquire()
	
	print("{}进入了唱吧ktv , 正在唱歌 ~".format(person))
	# 唱一段时间
	time.sleep( random.randrange(4,8) ) # 4 5 6 7
	
	print("{}离开了唱吧ktv , 唱完了 ... ".format(person))
	
	# 解锁
	sem.release()

if __name__ == "__main__":
	sem = Semaphore(5)
	lst = ["赵凤勇" , "沈思雨", "赵万里" , "张宇" , "假率先" , "孙杰龙" , "陈璐" , "王雨涵" , "杨元涛" , "刘一凤"   ]
	for i  in lst:
		p = Process(target=singsong_ktv , args = (i , sem)		)
		p.start()


"""
# 总结: Semaphore 可以设置上锁的数量 , 同一时间上多把锁
创建进程时,是异步并发,执行任务时,是同步程序;
"""







# 赵万里进入了唱吧ktv , 正在唱歌 ~
# 赵凤勇进入了唱吧ktv , 正在唱歌 ~
# 张宇进入了唱吧ktv , 正在唱歌 ~
# 沈思雨进入了唱吧ktv , 正在唱歌 ~
# 孙杰龙进入了唱吧ktv , 正在唱歌 ~











