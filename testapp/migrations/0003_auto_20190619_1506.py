# Generated by Django 2.2.1 on 2019-06-19 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_courses'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='courses',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'ordering': ['id']},
        ),
    ]
