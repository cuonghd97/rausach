# Generated by Django 2.1.7 on 2019-03-27 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0005_remove_hinhanhsp_duong_dan'),
    ]

    operations = [
        migrations.AddField(
            model_name='sanpham',
            name='avt',
            field=models.FileField(default=0, upload_to='product/avatar/'),
            preserve_default=False,
        ),
    ]