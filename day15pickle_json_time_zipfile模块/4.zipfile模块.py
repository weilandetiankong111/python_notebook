# ### zipfile 压缩模块
import zipfile

# (1) 压缩文件
""" zipfile.ZIP_DEFLATED 压缩减少空间 """
# 创建压缩包
zf = zipfile.ZipFile("ceshi111.zip","w",  zipfile.ZIP_DEFLATED)
# 写入文件
'''write(路径,别名)'''
zf.write("/bin/bash","bash")
zf.write("/bin/bunzip2","bunzip2")
zf.write("/bin/cat","tmp/cat")
# 关闭文件
zf.close()

# (2) 解压文件
zf = zipfile.ZipFile("ceshi111.zip","r")
# 解压单个文件
"""extract(文件,路径)"""
# zf.extract("bash","ceshi111")
# 解压所有文件
zf.extractall("ceshi222")
zf.close()


# (3) 追加文件
zf = zipfile.ZipFile("ceshi111.zip","a", zipfile.ZIP_DEFLATED)
zf.write("/bin/chmod","chmod")
zf.close()

# 用with来简化操作
with zipfile.ZipFile("ceshi111.zip","a", zipfile.ZIP_DEFLATED) as zf:
	zf.write("/bin/chmod","chmod123456")

# (4) 查看文件
with zipfile.ZipFile("ceshi111.zip","r") as zf:
	lst = zf.namelist()	
	print(lst)