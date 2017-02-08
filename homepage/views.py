from django.shortcuts import render, redirect, 	reverse
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages

from karyawan.models import Akun, Karyawan

# Create your views here.

def login_view(request):
	if request.POST:
		user = authenticate(username=request.POST['username'], password=request.POST['password'])
		if user is not None:
			if user.is_active:
				try:
					akkun = Akun.objects.get(akkun=user.id)
					login(request, user)
					
					request.session['karyawan_id'] = akkun.karyawan.id
					request.session['jenis_akun'] = akkun.jenis_akun
					request.session['username'] = request.POST['username']
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