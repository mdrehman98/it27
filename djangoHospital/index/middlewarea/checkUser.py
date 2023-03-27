from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponseRedirect
from common.models import User
import re


# 前台url判断中间件
class checkUser(MiddlewareMixin):

    def process_request(self, request):
        index_url = request.path
        # print(index_url)
        if index_url.startswith('/index') or index_url.startswith('/'):
            pattern = '/admin/'
            iscms = re.search(pattern, request.path)

            pattern1 = '/common/'
            iscomm = re.search(pattern1, request.path)

            pattern2 ='/doctor'
            iscommm = re.search(pattern2,request.path)

            # print(iscms)
            if iscms is None and iscomm is None and iscommm is None:
                urls_list = [
                    '/index/login/index.html',
                    '/index/login/login.html',
                    '/index/login/logout.html',
                    '/index/register/index.html',
                    '/index/register/register.html'
                ]
                print(request.path)
                if (request.path not in urls_list):
                    username = request.session.get("user_name", "")
                    password = request.session.get("user_password", "")
                    if username == "" or username is None or password == "" or password is None:
                        return HttpResponseRedirect('/index/login/index.html')
                    else:
                        try:
                            rows = User.objects.get(username=username)
                            if rows.password == password:
                                if rows.status == '0':
                                    status = 0
                                    msg = 'The user is disabled, please contact the administrator'
                                    del request.session["user_name"]
                                    del request.session["user_password"]
                                else:
                                    status = 1
                                    msg = 'Allow login'
                            else:
                                status = 0
                                msg = 'Incorrect password'
                                del request.session["user_name"]
                                del request.session["user_password"]
                        except User.DoesNotExist:
                            status = 0
                            msg = 'username does not exist'
                        if status == 0:
                            return HttpResponseRedirect('/index/login/index.html')

    def process_response(self, request, response):
        # print("当前url为：" + request.path)
        return response
