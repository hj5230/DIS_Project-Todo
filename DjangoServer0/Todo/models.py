from django.db import models

class User(models.Model):
    uid = models.CharField(max_length=4, verbose_name='UID',
        unique=True)
    pwd = models.CharField(max_length=16)
    def __str__(self):
        return self.uid

class Memorandum(models.Model):
    title = models.CharField(max_length=64, verbose_name='Title',
        blank=True, null=True)
    content = models.TextField(verbose_name='Content', blank=True, null=True)
    status = models.BooleanField(verbose_name='Status', default=False)
    timeStamp = models.DateTimeField(verbose_name='TimeStamp')
    def __str__(self):
        return self.title

# class Schedule(models.Model):

class Notebook(models.Model):
    head = models.CharField(max_length=64, verbose_name='Title')
    body = models.TextField(verbose_name='Text', blank=True, null=True)
    timeStamp = models.DateTimeField(verbose_name='TimeStamp')
    def __str__(self):
        return self.head

class Codebook(models.Model):
    tag = models.CharField(max_length=32, verbose_name='Tag')
    unm = models.CharField(max_length=32, verbose_name='Account')
    pwd = models.CharField(max_length=32, verbose_name='Password')
    tsp = models.DateField(verbose_name='TimeStamp')
    def __str__(self):
        return self.tag
