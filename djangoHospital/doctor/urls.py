from django.urls import path
from doctor.controllers import index, appointment, reports

urlpatterns = [
    # 首页路由
    path('index/index.html', index.index),
    path('index/welcome.html', index.welcome),
    path('index/password.html', index.password),

    path('appointment/index.html', appointment.index),
    path('appointment/edit.html', appointment.edit),
    path('appointment/update.html', appointment.update),

    path('reports/index.html', reports.index),
    path('reports/edit.html', reports.edit),

]
