from django.db import models


# Create your models here.

class Admin(models.Model):
    """管理员数据库模型"""
    username = models.CharField(default='', max_length=50, verbose_name="管理员用户名")
    realname = models.CharField(default='', max_length=50, verbose_name="管理员姓名")
    password = models.CharField(default='', max_length=32, verbose_name="管理员密码")
    gender = models.SmallIntegerField(default=1, verbose_name="性别")  # 1表示男，2表示女
    status = models.SmallIntegerField(default=1, verbose_name="状态")
    addtime = models.FloatField(max_length=30, default=0.0, verbose_name="加入时间")
    updatetime = models.FloatField(max_length=30, default=0.0, verbose_name="更新时间")
    email = models.EmailField(default='', verbose_name="邮箱")

    class Meta:
        verbose_name = '管理员列表'
        verbose_name_plural = verbose_name

    def __str__(self):  # 在Python3中用 __str__ 代替 __unicode__
        return self.username


class Doctor(models.Model):
    """医生数据库模型"""
    username = models.CharField(default='', max_length=100, verbose_name="用户名")
    realname = models.CharField(default='', max_length=50, verbose_name="姓名")
    password = models.CharField(default='', max_length=32, verbose_name="密码")
    telephone = models.CharField(default='', max_length=50, verbose_name="电话")
    address = models.CharField(default='', max_length=255, verbose_name="地址")
    gender = models.SmallIntegerField(default=1, verbose_name="性别")  # 1表示男，2表示女
    avatar = models.CharField(default='', max_length=255, verbose_name="头像")
    status = models.SmallIntegerField(default=1, verbose_name="状态")
    addtime = models.FloatField(max_length=30, default=0.0, verbose_name="加入时间")
    updatetime = models.FloatField(max_length=30, default=0.0, verbose_name="更新时间")
    email = models.EmailField(default='', verbose_name="邮箱")

    class Meta:
        verbose_name = '医生表'
        verbose_name_plural = verbose_name

    def __str__(self):  # 在Python3中用 __str__ 代替 __unicode__
        return self.username


class Appointment(models.Model):
    """预约数据库模型"""
    doctor_id = models.IntegerField(default=0, verbose_name="所属医生")
    user_id = models.IntegerField(default=0, verbose_name="所属用户")
    status = models.IntegerField(default=1, verbose_name="状态")
    app_date = models.CharField(max_length=255, default='', verbose_name="预约日期")
    start_time = models.CharField(max_length=255, default='', verbose_name="预约时间")
    comments = models.CharField(default='', max_length=255, verbose_name="备注")
    addtime = models.FloatField(max_length=30, default=0.0, verbose_name="加入时间")
    updatetime = models.FloatField(max_length=30, default=0.0, verbose_name="更新时间")

    class Meta:
        verbose_name = '预约表'
        verbose_name_plural = verbose_name

    def __str__(self):  # 在Python3中用 __str__ 代替 __unicode__
        return self.status


class User(models.Model):
    """用户数据库模型"""
    username = models.CharField(default='', max_length=50, verbose_name="姓名")
    password = models.CharField(default='', max_length=32, verbose_name="密码")
    gender = models.SmallIntegerField(default=1, verbose_name="性别")  # 1表示男，2表示女
    age = models.IntegerField(default=0, verbose_name="年龄")
    avatar = models.CharField(default='', max_length=255, verbose_name="头像")
    address = models.CharField(default='', max_length=255, verbose_name="地址")
    status = models.SmallIntegerField(default=1, verbose_name="状态")
    addtime = models.FloatField(max_length=30, default=0.0, verbose_name="加入时间")
    updatetime = models.FloatField(max_length=30, default=0.0, verbose_name="更新时间")
    email = models.EmailField(default='', verbose_name="邮箱")
    telephone = models.CharField(default='', max_length=20, verbose_name="电话")
    # add realname in user field
    realname = models.CharField(default='', max_length=50, verbose_name="RealName")

    class Meta:
        verbose_name = '用户表'
        verbose_name_plural = verbose_name

    def __str__(self):  # 在Python3中用 __str__ 代替 __unicode__
        return self.username


class Reports(models.Model):
    """报告数据库模型"""
    doctor_id = models.IntegerField(default=0, verbose_name="所属医生")
    user_id = models.IntegerField(default=0, verbose_name="所属用户")
    appointment_id = models.IntegerField(default=0, verbose_name="所属预约")
    status = models.SmallIntegerField(default=1, verbose_name="状态")
    symptoms = models.CharField(max_length=255, default='', verbose_name="症状")
    results = models.CharField(max_length=255, default='', verbose_name="结果")
    treatment = models.CharField(max_length=255, default='', verbose_name="治疗方案")
    desc = models.CharField(max_length=255, default='', verbose_name="说明")
    addtime = models.FloatField(max_length=30, default=0.0, verbose_name="加入时间")
    updatetime = models.FloatField(max_length=30, default=0.0, verbose_name="更新时间")

    class Meta:
        verbose_name = '报告表'
        verbose_name_plural = verbose_name

    def __str__(self):  # 在Python3中用 __str__ 代替 __unicode__
        return self.status
