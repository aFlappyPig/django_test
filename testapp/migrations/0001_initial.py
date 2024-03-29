# Generated by Django 2.1.7 on 2019-04-01 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='教师姓名')),
                ('sex', models.CharField(choices=[('0', '未知'), ('1', '男'), ('2', '女')], default='0', max_length=1, verbose_name='教师性别')),
                ('phone', models.CharField(blank=True, max_length=11, null=True, verbose_name='手机号')),
            ],
        ),
    ]
