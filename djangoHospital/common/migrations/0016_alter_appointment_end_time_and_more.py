# Generated by Django 4.1.7 on 2023-03-22 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0015_appointment_comments"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appointment",
            name="end_time",
            field=models.CharField(default="", max_length=255, verbose_name="预约时间"),
        ),
        migrations.AlterField(
            model_name="appointment",
            name="start_time",
            field=models.CharField(default="", max_length=255, verbose_name="预约时间"),
        ),
    ]
