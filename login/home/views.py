from django.shortcuts import render,render_to_response
from django.contrib.auth import logout as auth_logout
from django.core.files.storage import FileSystemStorage


def login(request):
	return render(request, 'login.html')

def base(request):
	print("yes")
	name = request.user.get_full_name
	context_dic = {'user':name}
	return render_to_response('base.html',context_dic)

def index(request):
	
	return render_to_response('index.html',{})

def logout(request):
    auth_logout(request)
    return render(request, 'login.html')

def add(request):
	return render(request,'add_new.html')