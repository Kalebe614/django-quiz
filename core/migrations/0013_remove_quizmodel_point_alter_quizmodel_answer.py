# Generated by Django 4.2.3 on 2023-08-31 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_rename_end_time_quizmodel_total_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quizmodel',
            name='point',
        ),
        migrations.AlterField(
            model_name='quizmodel',
            name='answer',
            field=models.CharField(max_length=255, verbose_name='Answer User'),
        ),
    ]
