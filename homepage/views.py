from django.shortcuts import render, redirect, 	reverse
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages

from django.contrib.auth.backends import ModelBackend
from django.http import HttpResponseForbidden, HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.models import User, Group

from karyawan.models import Akun, Karyawan
		
def login_view(request):
	if request.method == 'POST':
		user = authenticate(username=request.POST['username'], password=request.POST['password'])
		if user is not None:
			if user.is_active:
				try:
					akun = Akun.objects.get(akun=user.id)
					login(request, user)

					request.session['karyawan_id'] = akun.karyawan.id
					request.session['jenis_akun'] = akun.jenis_akun
					request.session['username'] = request.POST['username']
					return redirect('blog:post_list')
				except:
					return redirect('blog:post_list')
			else:
				messages.add_message(request, messages.INFO, 'User belum terverifikasi')
		else:
			messages.add_message(request, messages.INFO, 'Username atau password Anda salah')
			
	return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('/login/')

def login_redirect(request):
    return redirect('/login/')	