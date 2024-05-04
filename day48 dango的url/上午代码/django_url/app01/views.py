from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
	return HttpResponse('首页')

def index(request):

	return HttpResponse('ok')

def index2(request):

	return HttpResponse('index2')



def books(request, m, y):
	print(y, m)  # 2019  匹配出来的都是字符串

	return HttpResponse('%s-%s所有书籍都在这儿,你随意看' % (y, m))


def books2(request,  month, year):
	print(year, month)  # 2019  匹配出来的都是字符串

	return HttpResponse('%s--%s所有书籍都在这儿,你随意看' % (year,month ))










