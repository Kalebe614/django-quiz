# Generated by Django 4.2.4 on 2023-08-16 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_quizmodel_correct_answer_delete_resultquiztmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizmodel',
            name='is_correct',
            field=models.BooleanField(default=False),
        ),
    ]