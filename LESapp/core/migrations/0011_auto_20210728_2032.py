# Generated by Django 3.1.1 on 2021-07-28 15:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20210728_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentvideodata',
            name='last_watched',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 28, 15, 2, 34, 214617, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='studentvideodata',
            name='timelist',
            field=models.TextField(max_length=500000),
        ),
        migrations.AlterField(
            model_name='videos',
            name='is_added',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 28, 15, 2, 34, 214161, tzinfo=utc)),
        ),
    ]
