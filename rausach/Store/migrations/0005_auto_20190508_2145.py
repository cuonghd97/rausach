# Generated by Django 2.1.7 on 2019-05-08 14:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0004_hoadon_is_change'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hoadon',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 5, 8, 14, 45, 24, 646592, tzinfo=utc)),
        ),
    ]
