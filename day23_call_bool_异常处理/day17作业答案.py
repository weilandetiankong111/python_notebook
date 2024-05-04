# 1、匹配整数或者小数（包括正数和负数）
[+-]?\d+(\.\d+)?

# 2、匹配年月日日期 格式 2018-12-31
([12]\d{3})-(0?[1-9]|1[0-2])-(0?[1-9]|[12]\d|3[01])      # 0?[1-9]|1\d|2\d|3[01]   => 0?[1-9]|[12]\d|3[01] 

# 3、匹配qq号 5-12 首字符没有0 
[1-9]\d{4,11}

# 4、11位的电话号码
1[356789]\d{9}
 
# 5、长度为8-10位的用户密码 : 包含数字字母下划线
\w{8,10}
if "数字" in strvar and "字母" in strvar and "_" in strvar:
	return ok
else :
	return "格式不对"

# 6、匹配验证码：4位数字字母组成的
[0-9a-zA-Z]{4}

# 7、匹配邮箱地址 邮箱规则 123463922@qq.com  123@abc.com.cn
# @之前必须有内容且只能是字母,数字,下划线(_),减号(-),点(.)
[\w\-\.]+
# @符号后面是字母,数字,减号(-),保留121@qq.com.cn 的可能
@[a-zA-Z\d\-]+(\.[a-zA-Z\d\-]+)?
# 最后一个点(.)之后必须有内容,字母,数字且长度为大于等于2个字节,小于等于6个字节
\.[a-zA-Z\d]{2,6}

#综合:
[\w\-\.]+@[a-zA-Z\d\-]+(\.[a-zA-Z\d\-]+)?\.[a-zA-Z\d]{2,6}



# 8、从类似
# <a>wahaha</a>
# <b>banana</b>
# <h1>qqxing</h1>
# <h1>q</h1>
# 这样的字符串中，
# 1）匹配出 wahaha，banana，qqxing 内容。
<.*?>(.*?)<.*?>
# 2）匹配出 a,b,h1这样的内容
<(.*?)>.*?<.*?>

# 9、'1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'
# 从上面算式中匹配出最内层小括号的表达式
import re
strvar = '1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'
obj = re.search(r"\([^\(\)]+\)",strvar)
print(obj.group())

# 10正则小程序:
"""
	给你字符串 '1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))' 计算最后结果.  
"""










