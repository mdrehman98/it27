from django.test import TestCase

# Create your tests here.
from common.models import User, Doctor


def test_sign(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if username == "" or password == "":
        msg = 'Username or password cannot be empty'
    else:
        try:
            user = User.objects.get(username=username)
            if user.password == password:
                request.session['user_name'] = request.POST.get('username')
                request.session['user_password'] = request.POST.get('password')
                state = 1
                msg = 'login success'
            else:
                msg = 'password error'
        except User.DoesNotExist:
            msg = 'username does not exist'


def test_detail(request):
    id = request.GET.get('id', '')
    info = Doctor.objects.get(id=id)
    print(info)
