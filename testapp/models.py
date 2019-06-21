from django.db import models


# Create your models here.

class Teacher(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=20, verbose_name='教师姓名')
    sex = models.CharField(max_length=1, choices=(('0', '未知'), ('1', '男'), ('2', '女')), default='0',
                           verbose_name='教师性别')
    phone = models.CharField(max_length=11, blank=True, null=True, verbose_name='手机号')

    age = models.CharField(max_length=10, blank=False, null=False, verbose_name='年龄', default='未知')

    class Meta:
        ordering = ["id"]


class Courses(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=60, verbose_name='课程名称')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    class Meta:
        ordering = ["id"]
