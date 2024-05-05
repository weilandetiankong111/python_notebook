

from django import template

register = template.Library()  #注册器,变量名称必须叫register

@register.filter   #过滤器
def xx(v1):  #第一参数是使用过滤器时,管道符前面的数据 <h1>{{ name|xx }}</h1>

	return v1 + 'xx'

@register.filter   #过滤器,至多有两个参数
def xx2(v1, v2):  #第一参数是使用过滤器时,管道符前面的数据 ,第二个参数是冒号后面的值,<h1>{{ name|xx:'oo' }}</h1>

	return v1 + 'xx2' + v2



@register.simple_tag
def tag1(v1, v2 ,v3):  #参数个数没有限制


	return v1 + v2 + v3


@register.inclusion_tag('zujian2.html')
def dongtai(v1):  #参数没有个数限制
	data = v1  #[11,22,33,44,55,66]
	return {'data': data}




