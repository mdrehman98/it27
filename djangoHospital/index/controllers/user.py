from django.shortcuts import render
from django.http import HttpResponse
from common.models import User, Appointment, Doctor, Reports
from index.controllers import common
from index.controllers import upload
from django.conf import settings
import json
import time


def center(request):
    userinfo = common.setting(request)  # 查询当前登录的用户信息
    user = User.objects.get(id=userinfo['userinfo'].id)

    appointments = Appointment.objects.filter(user_id=user.id).values()
    for i, value in enumerate(appointments):
        appointments[i]['addtime'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(appointments[i]['addtime'])))

        doctor = Doctor.objects.filter(id=appointments[i]['doctor_id']).first()
        if doctor is not None:
            appointments[i]['doctor'] = doctor.realname

    return render(request, 'index/user/center.html', {'user': user, 'appointments': appointments})


def report(request):
    userinfo = common.setting(request)  # 查询当前登录的用户信息
    user = User.objects.get(id=userinfo['userinfo'].id)

    reportslists = Reports.objects.filter(user_id=user.id).values()
    for i, value in enumerate(reportslists):
        reportslists[i]['addtime'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(reportslists[i]['addtime'])))

        doctor = Doctor.objects.filter(id=reportslists[i]['doctor_id']).first()
        if doctor is not None:
            reportslists[i]['doctor'] = doctor.realname

    return render(request, 'index/user/report.html', {'user': user, 'reportslists': reportslists})


def set(request):
    userinfo = common.setting(request)
    user = User.objects.get(id=userinfo['userinfo'].id)
    return render(request, 'index/user/set.html', {'user': user})


def userinfo(request):
    if request.method == 'POST':
        state = 0
        msg = 'update error'
        id = request.POST.get('id')
        username = request.POST.get('username')
        user = User.objects.filter(username=username).get()
        if user is not None:
            if int(user.id) != int(id):
                msg = 'username already exists'
                info = {"state": state, "msg": msg}
                return HttpResponse(json.dumps(info))

        telephone = request.POST.get('telephone')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        email = request.POST.get('email')
        realname = request.POST.get('realname')
        updatetime = time.time()
        update = User.objects.filter(id=id).update(
            username=username,
            telephone=telephone,
            gender=gender,
            address=address,
            email = email,
            realname=realname,
            updatetime=updatetime
        )
        if update:
            state = 1
            msg = 'update success'
        info = {"state": state, "msg": msg}
        return HttpResponse(json.dumps(info))


def password(request):
    if request.method == 'POST':
        state = 0
        msg = 'update error'
        id = request.POST.get('id')
        nowpass = request.POST.get('nowpass')
        newpass = request.POST.get('newpass')
        repass = request.POST.get('repass')
        if newpass != repass:
            msg = 'The two passwords are inconsistent'
            info = {"state": state, "msg": msg}
            return HttpResponse(json.dumps(info))
        user = User.objects.get(id=id)
        if user.password != nowpass:
            msg = 'he original password is incorrect'
            info = {"state": state, "msg": msg}
            return HttpResponse(json.dumps(info))

        updatetime = time.time()
        update = User.objects.filter(id=id).update(password=newpass, updatetime=updatetime)
        if update:
            state = 1
            msg = 'update success'
        info = {"state": state, "msg": msg}
        return HttpResponse(json.dumps(info))

def avatar(request):
    if request.method == 'POST':
        state = 0
        msg = 'update error'
        id = request.POST.get('id')
        avatar = request.POST.get('avatar')
        useravatar = User.objects.get(id=id).avatar
        # print(useravatar)
        if useravatar == avatar:
            state = 1
            msg = 'update success'
            info = {"state": state, "msg": msg}
            return HttpResponse(json.dumps(info))

        updatetime = time.time()
        update = User.objects.filter(id=id).update(avatar=avatar, updatetime=updatetime)
        if update:
            uploads = upload.move_image(request, avatar, 'avatar')
            uploadobj = json.loads(uploads)
            if uploadobj['state'] == 0:
                info = {"state": state, "msg": msg}
                return HttpResponse(json.dumps(info))
            # 删除原来图片
            if useravatar == '':
                print('oooooooo')
            else:
                upload.del_image(request, settings.MEDIA_ROOT + 'avatar/' + useravatar)
            state = 1
            msg = 'update success'
        info = {"state": state, "msg": msg}
        return HttpResponse(json.dumps(info))


def detailReport(request):
    id = request.GET.get('id')
    info = Reports.objects.get(id=id)
    doctor = Doctor.objects.filter(id=info.doctor_id).first()
    if doctor is not None:
        info.doctor = doctor.username

    return render(request, 'index/user/detail.html', {'info': info})
