# Generated by Django 4.0.1 on 2022-05-17 10:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0003_advice_en_text_advice_en_title_advice_ru_text_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='going_to_loss_day',
        ),
        migrations.AddField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
