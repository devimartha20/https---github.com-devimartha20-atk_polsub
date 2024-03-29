# Generated by Django 4.2 on 2023-06-22 21:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atk', '0037_isi_pengajuan_rekomendasi_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pengajuanabccek',
            name='dana',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pengajuanabccek',
            name='persentase_dana',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pengajuanabccek',
            name='persentase_item',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pengajuanabccek',
            name='persentase_kumulatif_dana',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pengajuanabccek',
            name='persentase_kumulatif_item',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pengajuanabccek',
            name='prioritas',
            field=models.CharField(blank=True, choices=[('A', 'Tinggi'), ('B', 'Sedang'), ('C', 'Rendah')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='penggunaanstok',
            name='tanggal',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 6, 22, 21, 0, 18, 293466, tzinfo=datetime.timezone.utc)),
        ),
    ]
