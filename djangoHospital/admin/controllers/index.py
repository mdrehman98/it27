import json

from django.http import HttpResponse
from django.shortcuts import render

from common.models import Admin


def index(request):
    username = request.session.get('admin_username', '')
    return render(request, 'admin/index/index.html', {'username': username})


def welcome(request):
    username = request.session.get('admin_username', '')
    return render(request, 'admin/index/welcome.html', {
        'username': username,
    })


def password(request):
    if request.method == 'POST':
        state = 0
        msg = 'Change failed'
        id = request.POST.get('id')
        sinfo = Admin.objects.get(id=id)
        oldpassword = request.POST.get('oldpassword')
        if sinfo.password != oldpassword:
            msg += ',The original password is wrong！'
        else:
            password = request.POST.get('password')
            repassword = request.POST.get('repassword')
            if password != repassword:
                msg += ',Two inconsistent passwords！'
            else:
                update = Admin.objects.filter(id=id).update(password=password)
                if update:
                    state = 1
                    msg = 'Change successfully！'
                else:
                    msg += ',Database errors！'

        info = {"state": state, "msg": msg}
        return HttpResponse(json.dumps(info))

    else:
        admin_id = request.session.get("admin_id", "")
        try:
            sinfo = Admin.objects.get(id=admin_id)
        except Admin.DoesNotExist:
            sinfo = []
        # 获取管理员信息
        return render(request, 'admin/index/password.html', {'sinfo': sinfo})
