# Generated by Django 3.1.1 on 2021-08-03 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_student_rollno'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='name',
            field=models.CharField(default='nidu', max_length=100),
        ),
    ]