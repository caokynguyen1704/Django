# Generated by Django 3.0.5 on 2020-04-28 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_delete_thongbao'),
    ]

    operations = [
        migrations.AddField(
            model_name='code',
            name='Loai',
            field=models.CharField(default='[Chưa có]', max_length=200),
        ),
    ]
