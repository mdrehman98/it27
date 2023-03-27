import json
import time

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

from common.models import Appointment, User, Doctor, Reports


def index(request):
    # 获取ajax参数
    ajax = request.GET.get('ajax')
    # 根据参数是否存在判断是展示页面还是返回数据
    if ajax is not None:
        # 搜索需要的参数
        keywords = request.GET.get('keywords')
        status = request.GET.get('status')
        # 获取第几页，默认是1开始
        page = request.GET.get('page') if request.GET.get('page') is not None else 1
        page = int(page)
        # 每页默认取10条数据
        limit = request.GET.get('limit') if request.GET.get('limit') is not None else 10
        limit = int(limit)
        start = (int(page) - 1) * int(limit)
        end = int(page) * int(limit)

        doctor_id = request.session.get("doctor_id", "")

        rows = Appointment.objects.filter(doctor_id=doctor_id)
        count = Appointment.objects.filter(doctor_id=doctor_id)

        # 判断关键字是否为空
        if keywords is not None and keywords != '':
            rows = rows.filter(app_date=keywords)
            count = count.filter(app_date=keywords)

        if status != '0' and status is not None:
            print(status)
            rows = rows.filter(status=int(status))
            count = count.filter(status=int(status))

        rows = rows[start:end].values()
        count = count.count()
        rows = list(rows)
        # 循环整个学生数据，将addtime格式化成日期
        for i, value in enumerate(rows):
            rows[i]['addtime'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(rows[i]['addtime'])))

            user = User.objects.filter(id=rows[i]['user_id']).first()
            if user is not None:
                rows[i]['user'] = user.realname

            doctor = Doctor.objects.filter(id=rows[i]['doctor_id']).first()
            if doctor is not None:
                rows[i]['doctor'] = doctor.realname

        data = {"code": 0, "msg": "", "count": count, "data": rows}
        # 返回json数据给前端
        return HttpResponse(json.dumps(data))
    else:
        # 渲染teacher/student/index.html模板
        return render(request, 'admin/appointment/index.html')


def update(request):
    if request.method == 'POST':
        state = 0
        msg = 'error'
        id = request.POST.get('id')
        user_id = request.POST.get('user_id')
        doctor_id = request.POST.get('doctor_id')
        symptoms = request.POST.get('symptoms')
        results = request.POST.get('results')
        treatment = request.POST.get('treatment')
        desc = request.POST.get('desc')
        status = 1
        addtime = time.time()
        updatetime = time.time()

        Appointment.objects.filter(id=id).update(status=2)
        rest = Reports.objects.create(
            user_id=user_id,
            doctor_id=doctor_id,
            appointment_id=id,
            symptoms=symptoms,
            results=results,
            treatment=treatment,
            status=status,
            addtime=addtime,
            updatetime=updatetime,
            desc=desc
        )
        if rest:
            state = 1
            msg = 'Successfully'

        info = {"state": state, "msg": msg}
        return HttpResponse(json.dumps(info))


def edit(request):
    id = request.GET.get('id')
    info = Appointment.objects.get(id=id)
    return render(request, 'admin/appointment/edit.html', {'info': info})
