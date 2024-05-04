import re

str_money = input('请输入您要取的金额:')
obj = re.search(r'^(\d)+(00)$', str_money)
print(obj)





