# Generated by Django 4.2 on 2023-06-22 03:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atk', '0036_barang_atk_status_alter_guna_kegunaan_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='isi_pengajuan',
            name='rekomendasi',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='penggunaanstok',
            name='tanggal',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 6, 22, 3, 10, 30, 824718, tzinfo=datetime.timezone.utc)),
        ),
    ]
