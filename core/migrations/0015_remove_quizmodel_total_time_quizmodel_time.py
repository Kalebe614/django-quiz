# Generated by Django 4.2.4 on 2023-09-02 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_alter_quizmodel_total_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quizmodel',
            name='total_time',
        ),
        migrations.AddField(
            model_name='quizmodel',
            name='time',
            field=models.CharField(blank=True, default='', max_length=6, verbose_name='Time'),
        ),
    ]
