# Generated by Django 4.0.5 on 2022-08-21 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0006_memorandum_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memorandum',
            name='timeStamp',
            field=models.DateTimeField(verbose_name='时间戳'),
        ),
    ]
