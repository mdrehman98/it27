import json

from django.http import HttpResponse
from django.shortcuts import render

from common.models import Doctor


def index(request):
    username = request.session.get('doctor_username', '')
    return render(request, 'doctor/index/index.html', {'username': username})


def welcome(request):
    username = request.session.get('doctor_username', '')
    return render(request, 'doctor/index/welcome.html', {
        'username': username,
    })


def password(request):
    if request.method == 'POST':
        state = 0
        msg = 'Change failed'
        id = request.POST.get('id')
        sinfo = Doctor.objects.get(id=id)
        oldpassword = request.POST.get('oldpassword')
        if sinfo.password != oldpassword:
            msg += ',The original password is wrong！'
        else:
            password = request.POST.get('password')
            repassword = request.POST.get('repassword')
            if password != repassword:
                msg += ',Two inconsistent passwords！'
            else:
                update = Doctor.objects.filter(id=id).update(password=password)
                if update:
                    state = 1
                    msg = 'Change successfully！'
                else:
                    msg += ',Database errors！'

        info = {"state": state, "msg": msg}
        return HttpResponse(json.dumps(info))

    else:
        doctor_id = request.session.get("doctor_id", "")
        try:
            sinfo = Doctor.objects.get(id=doctor_id)
        except Doctor.DoesNotExist:
            sinfo = []
        # 获取管理员信息
        return render(request, 'doctor/index/password.html', {'sinfo': sinfo})
