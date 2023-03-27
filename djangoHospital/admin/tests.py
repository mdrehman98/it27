import time

from django.db.models import Q
from django.test import TestCase

# Create your tests here.
from common.models import Admin


def test_index(request):
    ajax = request.GET.get('ajax')
    if ajax is not None:
        keywords = request.GET.get('keywords')
        page = request.GET.get('page') if request.GET.get('page') is not None else 1
        page = int(page)
        limit = request.GET.get('limit') if request.GET.get('limit') is not None else 10
        limit = int(limit)
        start = (int(page) - 1) * int(limit)
        end = int(page) * int(limit)
        if keywords is None:
            rows = Admin.objects.filter()[start:end].values()
            count = Admin.objects.filter().count()
        else:
            rows = Admin.objects.filter(
                Q(username__contains=keywords) | Q(realname__contains=keywords))[
                   start:end].values()
            count = Admin.objects.filter(
                Q(username__contains=keywords) | Q(realname__contains=keywords)).count()
        rows = list(rows)
        for i, value in enumerate(rows):
            rows[i]['addtime'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(rows[i]['addtime'])))
        print(count)


def test_password(request):
        id = request.POST.get('id')
        updatetime = time.time()
        update = Admin.objects.filter(id=id).update(
            password='123456',
            updatetime=updatetime
        )
        print(update)

