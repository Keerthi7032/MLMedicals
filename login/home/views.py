from django.shortcuts import render,render_to_response
from django.contrib.auth import logout as auth_logout
from django.core.files.storage import FileSystemStorage
import json
import requests


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

def image_upload(request):
	headers = {"Authorization": "Bearer ya29.GlsIBm_RHgwGwQV-pMuvlKFLNDXbSLZylaEV04tzNTfBPKIktw8ZSn29c8oN_7drBsnpaejC5fandjNQd3jTiUbXm-c4tuaKp8IWJCPK-paiIf6-Ng4kpdFEhv91"}
	para = {
	    "name": "roche.png",
	    "parents": ["14ricvjvrL9rvZop_IanWQfS6Go3jvbKr"]
	}
	files = {
	    'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
	    'file': open("home/static/images/upload.png", "rb")
	}
	r = requests.post(
	    "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
	    headers=headers,
	    files=files
	)
	print(r.text)