# Generated by Django 4.2 on 2023-05-23 08:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atk', '0021_rename_pengajuan_abc_cek_pengajuanabccek_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pengajuanabccek',
            name='harga',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pengajuanabccek',
            name='total_harga',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='penggunaanstok',
            name='tanggal',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 5, 23, 8, 9, 39, 45341, tzinfo=datetime.timezone.utc)),
        ),
    ]