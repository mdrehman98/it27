# Generated by Django 4.1.5 on 2023-02-05 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0009_alter_project_conclusion_alter_project_fsno_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="joins",
            field=models.CharField(default="", max_length=255, verbose_name="参与人"),
        ),
    ]