# Generated by Django 3.0.5 on 2020-04-28 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_code_loai'),
    ]

    operations = [
        migrations.AddField(
            model_name='code',
            name='HuongUng',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='code',
            name='Unlike',
            field=models.IntegerField(default=1),
        ),
    ]
