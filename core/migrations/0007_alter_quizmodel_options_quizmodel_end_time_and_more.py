# Generated by Django 4.2.4 on 2023-08-16 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_quizmodel_alter_answermodel_question_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quizmodel',
            options={'verbose_name': 'Quiz'},
        ),
        migrations.AddField(
            model_name='quizmodel',
            name='end_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='quizmodel',
            name='start_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
