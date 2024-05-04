from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def login(request):
	print(request)  #<WSGIRequest: GET '/login/?a=1&b=2'> WSGIRequest类的实例化对象
	print(request.method)
	print(request.POST)
	print(request.GET)  # request.GET.get('a')  == 1
	print(request.path)  #当前请求路径
	print(request.get_full_path())  #当前请求路径包含查询参数
	print(request.META)  #所有请求头的信息 {''HTTP_USER_AGENT':'asdfasdfasdf',....}
	# 	request.META 字典类型数据,所有的请求头的键都加上了一个HTTP_键名称
	# return HttpResponse('ok')
	if request.method == 'GET':
		return render(request, 'login.html')

	else:
		uname = request.POST.get('username')
		if uname == 'shiyuan':

			# return redirect('/home/')  #redirect的参数为一个路径
			return render(request, 'home.html')  #redirect的参数为一个路径


def home(request):
	book = '金瓶梅'
	return render(request,'home.html' , {'book': book})



def index(request):
	re = HttpResponse('xxx')
	# re = render('xxx')
	# ret = redirect('/home/')
	re['name'] = 'gaodaao'  # 添加响应头键值对
	re.status_code = 404  # 修改状态码
	return re



from django.views import View
class BookView(View):
	# get post
	# 通过反射获取到请求方法对应的类中的方法来执行
	def get(self,request):
		return HttpResponse('ok')



	'''
	    def dispatch(self, request, *args, **kwargs):
	        # Try to dispatch to the right method; if a method doesn't exist,
	        # defer to the error handler. Also defer to the error handler if the
	        # request method isn't on the approved list.
	        if request.method.lower() in self.http_method_names: #get
	            # ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
	            handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
	        else:
	            handler = self.http_method_not_allowed
	        return handler(request, *args, **kwargs)  # HttpResponse('ok')
	
	'''


def func(f):
	def inner(*args,**kwargs):
		print('aaaaa')
		ret = f(*args,**kwargs)
		print('bbbbb')
		return ret
	return inner


@func  # FBV装饰器用法和普通函数一样
def index(request):
	return HttpResponse('index')

from django.utils.decorators import method_decorator

# 方式 3
# @method_decorator(func,name='post')
# @method_decorator(func,name='get')
class ArticalView(View):

	# def get(self,request, year):
	# 	print(year)
	# 	return HttpResponse('articals')
	# 重写dispatch方法来进行拓展
	# @method_decorator(func)  # 方式2
	# def dispatch(self, request, *args, **kwargs):
	#
	# 	print('111111')
	# 	ret = super(ArticalView, self).dispatch(request, *args, **kwargs)
	#
	# 	print('222222')
	# 	return ret

	# @method_decorator(func)  # CBV方法加装饰器的方式1
	def get(self,request, year):
		print(year)
		return render(request, 'articals.html')

	# @method_decorator(func)
	def post(self,request, year):
		print(request.POST)
		return HttpResponse('ok')



