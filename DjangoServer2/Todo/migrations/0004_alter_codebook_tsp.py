# Generated by Django 4.0.5 on 2022-08-20 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0003_codebook'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codebook',
            name='tsp',
            field=models.DateField(verbose_name='时间戳'),
        ),
    ]
