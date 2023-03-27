import json
import time

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

from common.models import Doctor


def index(request):
    # 获取ajax参数
    ajax = request.GET.get('ajax')
    # 根据参数是否存在判断是展示页面还是返回数据
    if ajax is not None:
        # 搜索需要的参数
        keywords = request.GET.get('keywords')
        # 获取第几页，默认是1开始
        page = request.GET.get('page') if request.GET.get('page') is not None else 1
        page = int(page)
        # 每页默认取10条数据
        limit = request.GET.get('limit') if request.GET.get('limit') is not None else 10
        limit = int(limit)
        start = (int(page) - 1) * int(limit)
        end = int(page) * int(limit)
        # 判断关键字是否为空
        if keywords is None:
            rows = Doctor.objects.filter()[start:end].values()
            count = Doctor.objects.filter().count()
        else:
            rows = Doctor.objects.filter(
                Q(username__contains=keywords) | Q(realname__contains=keywords))[
                   start:end].values()
            count = Doctor.objects.filter(
                Q(username__contains=keywords) | Q(realname__contains=keywords)).count()
        rows = list(rows)
        for i, value in enumerate(rows):
            rows[i]['addtime'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(rows[i]['addtime'])))
        print(count)
        data = {"code": 0, "msg": "", "count": count, "data": rows}
        # 返回json数据给前端
        return HttpResponse(json.dumps(data))
    else:
        return render(request, 'admin/doctor/index.html')


def add(request):
    return render(request, 'admin/doctor/add.html')


def save(request):
    if request.method == 'POST':
        state = 0
        msg = 'add error'
        username = request.POST.get('username')
        realname = request.POST.get('realname')
        avatar = request.POST.get('avatar')
        telephone = request.POST.get('telephone')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        status = request.POST.get('status')
        email = request.POST.get('email')
        addtime = time.time()
        updatetime = time.time()
        try:
            Doctor.objects.get(username=username)
            msg += ',username already exists！'
        except Doctor.DoesNotExist:
            rest = Doctor.objects.create(
                username=username,
                realname=realname,
                avatar=avatar,
                telephone=telephone,
                address=address,
                password='123456',
                gender=gender,
                status=status,
                addtime=addtime,
                updatetime=updatetime,
                email=email
            )
            if rest:
                state = 1
                msg = 'Successfully added, initial password is 123456'

        info = {"state": state, "msg": msg}
        return HttpResponse(json.dumps(info))


def edit(request):
    id = request.GET.get('id')
    info = Doctor.objects.get(id=id)
    return render(request, 'admin/doctor/edit.html', {'info': info})


def update(request):
    if request.method == 'POST':
        state = 0
        msg = 'update error'
        id = request.POST.get('id')
        username = request.POST.get('username')
        realname = request.POST.get('realname')
        avatar = request.POST.get('avatar')
        telephone = request.POST.get('telephone')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        status = request.POST.get('status')
        email = request.POST.get('email')
        updatetime = time.time()

        update = Doctor.objects.filter(id=id).update(
            username=username,
            realname=realname,
            avatar=avatar,
            telephone=telephone,
            address=address,
            gender=gender,
            status=status,
            updatetime=updatetime,
            email=email
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
        updatetime = time.time()
        update = Doctor.objects.filter(id=id).update(
            password='123456',
            updatetime=updatetime
        )
        if update:
            state = 1
            msg = 'Update succeeded, initial password is 123456'

        info = {"state": state, "msg": msg}
        return HttpResponse(json.dumps(info))


def delete(request):
    if request.method == 'POST':
        state = 0
        msg = 'delete error'
        id = request.POST.get('id')

        delete = Doctor.objects.filter(id=id).delete()
        if delete:
            state = 1
            msg = 'delete success'
        info = {"state": state, "msg": msg}
        return HttpResponse(json.dumps(info))
