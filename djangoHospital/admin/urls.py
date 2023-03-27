from django.urls import path
from admin.controllers import index, admin, doctor, user, appointment, reports
from common.controllers import upload

urlpatterns = [
    path('upload/index.html', upload.image),
    # 首页路由
    path('index/index.html', index.index),
    path('index/welcome.html', index.welcome),
    path('index/password.html', index.password),

    # 管理员管理路由
    path('admin/index.html', admin.index),
    # 管理员添加路由
    path('admin/add.html', admin.add),
    path('admin/save.html', admin.save),
    # 管理员编辑路由
    path('admin/edit.html', admin.edit),
    path('admin/update.html', admin.update),
    # 管理员重置密码路由
    path('admin/password.html', admin.password),
    # 管理员删除路由
    path('admin/delete.html', admin.delete),

    path('doctor/index.html', doctor.index),
    path('doctor/add.html', doctor.add),
    path('doctor/save.html', doctor.save),
    path('doctor/edit.html', doctor.edit),
    path('doctor/update.html', doctor.update),
    path('doctor/delete.html', doctor.delete),
    path('doctor/password.html', doctor.password),

    path('user/index.html', user.index),
    path('user/edit.html', user.edit),
    path('user/update.html', user.update),
    path('user/delete.html', user.delete),
    path('user/password.html', user.password),

    path('appointment/index.html', appointment.index),
    path('appointment/edit.html', appointment.edit),
    path('appointment/update.html', appointment.update),

    path('reports/index.html', reports.index),
    path('reports/edit.html', reports.edit),

]
