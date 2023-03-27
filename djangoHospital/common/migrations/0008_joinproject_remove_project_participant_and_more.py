# Generated by Django 4.1.5 on 2023-02-02 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0007_project_endtime"),
    ]

    operations = [
        migrations.CreateModel(
            name="JoinProject",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("project_id", models.IntegerField(default=0, verbose_name="项目ID")),
                ("teacher_id", models.IntegerField(default=0, verbose_name="教师ID")),
                (
                    "score",
                    models.FloatField(default=0.0, max_length=30, verbose_name="得分"),
                ),
                ("status", models.SmallIntegerField(default=1, verbose_name="状态")),
                (
                    "addtime",
                    models.FloatField(default=0.0, max_length=30, verbose_name="加入时间"),
                ),
                (
                    "updatetime",
                    models.FloatField(default=0.0, max_length=30, verbose_name="更新时间"),
                ),
            ],
            options={"verbose_name": "参与项目表", "verbose_name_plural": "参与项目表",},
        ),
        migrations.RemoveField(model_name="project", name="participant",),
        migrations.RemoveField(model_name="project", name="participant_score",),
        migrations.RemoveField(model_name="project", name="principal",),
        migrations.AddField(
            model_name="project",
            name="teacher_id",
            field=models.IntegerField(default=0, verbose_name="负责人"),
        ),
        migrations.AddField(
            model_name="project",
            name="total_score",
            field=models.CharField(default="", max_length=255, verbose_name="总得分"),
        ),
    ]
