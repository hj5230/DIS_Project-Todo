# Generated by Django 4.0.5 on 2022-08-21 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0005_memorandum'),
    ]

    operations = [
        migrations.AddField(
            model_name='memorandum',
            name='status',
            field=models.BooleanField(blank=True, null=True, verbose_name='状态'),
        ),
    ]
