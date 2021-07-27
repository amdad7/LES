# Generated by Django 3.1.5 on 2021-07-07 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=100)),
                ('link', models.CharField(max_length=400)),
                ('description', models.CharField(max_length=100)),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_added', models.DateTimeField(default=1625688749.3963723)),
            ],
            options={
                'ordering': ['is_added'],
            },
        ),
        migrations.CreateModel(
            name='StudentVideoData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_watched', models.TimeField(default=1625688749.3967657)),
                ('total_watched', models.IntegerField(default=0)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.student')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.videos')),
            ],
        ),
    ]