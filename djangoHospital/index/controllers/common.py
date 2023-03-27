from common.models import User
import time


def setting(request):
    username = request.session.get('user_name', '')
    user = ''
    if username != '':
        user = User.objects.get(username=username)
        user.addtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(user.addtime)))
    content = {"userinfo": user}
    return content
