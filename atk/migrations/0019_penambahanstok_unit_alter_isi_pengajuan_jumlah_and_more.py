# Generated by Django 4.2 on 2023-05-22 10:44

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('atk', '0018_rename_pengambahanstok_penambahanstok'),
    ]

    operations = [
        migrations.AddField(
            model_name='penambahanstok',
            name='unit',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='atk.unit'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='isi_pengajuan',
            name='jumlah',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='isi_pengajuan',
            name='rekomendasi',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='penambahanstok',
            name='jumlah',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='penggunaanstok',
            name='jumlah',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='penggunaanstok',
            name='penerima',
            field=models.CharField(choices=[('M', 'Mahasiswa'), ('D', 'Dosen'), ('S', 'Staff'), ('L', 'Lainnya')], default='M', max_length=20),
        ),
        migrations.AlterField(
            model_name='penggunaanstok',
            name='tanggal',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 5, 22, 10, 44, 15, 203763, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='stokatk',
            name='jumlah',
            field=models.IntegerField(),
        ),
    ]
