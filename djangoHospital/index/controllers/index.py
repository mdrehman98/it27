from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from common.models import User, Doctor, Appointment
from index.controllers import common
from django.db import transaction
from django.db.models import Count, Q
import json
import time
import datetime


def index(request):
    keywords = request.GET.get('keywords', '')
    doctorlist = Doctor.objects
    if keywords != '':
        doctorlist = doctorlist.filter(Q(username__contains=keywords) | Q(realname__contains=keywords))

    doctorlist = doctorlist.order_by('-id').values()
    for i, value in enumerate(doctorlist):
        doctorlist[i]['addtime'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(doctorlist[i]['addtime'])))
    return render(request, 'index/index/index.html', {'doctorlist': doctorlist})


def detail(request):
    id = request.GET.get('id', '')
    info = Doctor.objects.get(id=id)
    return render(request, 'index/index/appointment.html', {'info': info})


def save(request):
    if request.method == 'POST':
        state = 0
        msg = 'add error'
        app_date = request.POST.get('app_date')
        start_time = request.POST.get('start_time')
        comments = request.POST.get('comments')
        doctor_id = request.POST.get('doctor_id')
        addtime = time.time()
        updatetime = time.time()

        userinfo = common.setting(request)  # 查询当前登录的用户信息
        user = User.objects.get(id=userinfo['userinfo'].id)

        info = Appointment.objects.filter(doctor_id=doctor_id, app_date=app_date, start_time=start_time).count()
        if info > 0:
            info = {"state": state, "msg": "The current time is not available"}
            return HttpResponse(json.dumps(info))

        rest = Appointment.objects.create(
            app_date=app_date,
            start_time=start_time,
            comments=comments,
            doctor_id=doctor_id,
            user_id=user.id,
            status=1,
            addtime=addtime,
            updatetime=updatetime
        )
        if rest:
            state = 1
            msg = 'Successfully appointment'

        info = {"state": state, "msg": msg}
        return HttpResponse(json.dumps(info))
