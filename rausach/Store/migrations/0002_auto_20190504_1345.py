# Generated by Django 2.1.7 on 2019-05-04 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrangThaiHangHoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ma', models.CharField(max_length=200)),
                ('mo_ta', models.TextField()),
            ],
            options={
                'db_table': 'trang_thai_hang_hoass',
            },
        ),
        migrations.AddField(
            model_name='chitiethoadon',
            name='trang_thai',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Store.TrangThaiHangHoa'),
        ),
    ]