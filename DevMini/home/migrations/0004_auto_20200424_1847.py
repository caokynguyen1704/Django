# Generated by Django 3.0.5 on 2020-04-24 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200424_1828'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='Birthday',
        ),
        migrations.AddField(
            model_name='myuser',
            name='Namsinh',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='myuser',
            name='Noio',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='myuser',
            name='Uid',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='Chucvu',
            field=models.CharField(default='Không có', max_length=500),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='Linhvuc',
            field=models.CharField(default='Không có', max_length=500),
        ),
    ]
