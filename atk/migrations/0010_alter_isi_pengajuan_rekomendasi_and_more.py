# Generated by Django 4.2 on 2023-05-14 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('atk', '0009_alter_jadwal_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='isi_pengajuan',
            name='rekomendasi',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jadwal',
            name='keterangan',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='pengajuan',
            name='jadwal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='atk.jadwal'),
        ),
        migrations.AlterField(
            model_name='pengumpulanpengajuan',
            name='jadwal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='atk.jadwal'),
        ),
    ]
