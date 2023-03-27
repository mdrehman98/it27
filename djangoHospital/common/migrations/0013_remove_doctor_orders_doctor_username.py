# Generated by Django 4.1.7 on 2023-03-21 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0012_appointment_doctor_reports_user_delete_achievements_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="doctor", name="orders",),
        migrations.AddField(
            model_name="doctor",
            name="username",
            field=models.CharField(default="", max_length=100, verbose_name="用户名"),
        ),
    ]
