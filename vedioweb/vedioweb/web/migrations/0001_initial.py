# Generated by Django 3.0.8 on 2020-07-07 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='vedio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='视频名称')),
                ('content', models.FileField(upload_to='', verbose_name='视频')),
            ],
        ),
    ]
