# Generated by Django 3.0.5 on 2020-04-29 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_myuser_thongbao'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThongBao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Thongbao', models.TextField(default='Không có thông báo')),
            ],
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='Thongbao',
        ),
    ]
