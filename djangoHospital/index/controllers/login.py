from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from common.models import User
import json
import time


def index(request):
    return render(request, 'index/login/index.html')


def login(request):
    '''登录方法'''
    if request.method == 'POST':
        state = 0
        msg = 'login error'
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == "" or password == "":
            msg = 'Username or password cannot be empty'
        else:
            rows = User.objects.filter(username=username).first()
            try:
                user = User.objects.get(username=username)
                if user.password == password:
                    if rows.status == 0:
                        msg = 'Account unavailable'
                    else:
                        request.session['user_name'] = request.POST.get('username')
                        request.session['user_password'] = request.POST.get('password')
                        state = 1
                        msg = 'login success'
                else:
                    msg = 'password error'
            except User.DoesNotExist:
                msg = 'username does not exist'
        info = {"state": state, "msg": msg}
        return HttpResponse(json.dumps(info))


def logout(request):
    try:
        del request.session['user_name']
        del request.session['user_password']
    except KeyError:
        pass
    return redirect(reverse('login_index'))
