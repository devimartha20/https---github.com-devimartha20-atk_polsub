# Generated by Django 4.2 on 2023-05-28 05:58

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('atk', '0027_pengajuan_tanggal_konfirmasi_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='total_pengajuan',
            name='harga',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='atk.harga'),
        ),
        migrations.AddField(
            model_name='total_pengajuan',
            name='total_dana',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='penggunaanstok',
            name='tanggal',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 5, 28, 5, 57, 44, 646673, tzinfo=datetime.timezone.utc)),
        ),
    ]