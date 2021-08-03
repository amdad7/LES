# Generated by Django 3.1.1 on 2021-08-03 17:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20210803_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentvideodata',
            name='last_watched',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 3, 17, 27, 37, 522086, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='videos',
            name='is_added',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 3, 17, 27, 37, 521682, tzinfo=utc)),
        ),
    ]