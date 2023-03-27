from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from common.models import User
import json
import time


def index(request):
    return render(request, 'index/register/index.html')


def register(request):
    '''注册方法'''
    if request.method == 'POST':
        state = 0
        msg = 'register error'
        username = request.POST.get('username')
        telephone = request.POST.get('telephone')
        email = request.POST.get('email')
        realname = request.POST.get('realname')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        status = 1
        address = request.POST.get('address')
        addtime = time.time()
        updatetime = time.time()
        try:
            userexist = User.objects.get(username=username)
            msg = 'The username has already been used'
        except User.DoesNotExist:
            rest = User.objects.create(
                username=username,
                telephone=telephone,
                status=status,
                password=password,
                gender=gender,
                address=address,
                addtime=addtime,
                email=email,
                realname=realname,
                updatetime=updatetime
            )
            if rest:
                state = 1
                msg = 'register success'

        info = {"state": state, "msg": msg}
        return HttpResponse(json.dumps(info))
