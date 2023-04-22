from django.db import models

class User(models.Model):
    uid = models.CharField(max_length=4, verbose_name='UID',
        unique=True)
    pwd = models.CharField(max_length=16)
    def __str__(self):
        return self.uid

class Memorandum(models.Model):
    title = models.CharField(max_length=64, verbose_name='标题',
        blank=True, null=True)
    content = models.TextField(verbose_name='内容', blank=True, null=True)
    status = models.BooleanField(verbose_name='状态', default=False)
    timeStamp = models.DateTimeField(verbose_name='时间戳')
    def __str__(self):
        return self.title

# class Schedule(models.Model):

class Notebook(models.Model):
    head = models.CharField(max_length=64, verbose_name='标题')
    body = models.TextField(verbose_name='正文', blank=True, null=True)
    timeStamp = models.DateTimeField(verbose_name='创建时间')
    def __str__(self):
        return self.head

class Codebook(models.Model):
    tag = models.CharField(max_length=32, verbose_name='标签')
    unm = models.CharField(max_length=32, verbose_name='账号')
    pwd = models.CharField(max_length=32, verbose_name='密码')
    tsp = models.DateField(verbose_name='时间戳')
    def __str__(self):
        return self.tag

# class Axis()