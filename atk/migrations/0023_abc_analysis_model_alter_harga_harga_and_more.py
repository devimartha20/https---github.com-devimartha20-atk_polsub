# Generated by Django 4.2 on 2023-05-24 03:34

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('atk', '0022_alter_pengajuanabccek_harga_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='abc_analysis_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tahun', models.IntegerField()),
                ('harga', models.IntegerField(blank=True, null=True)),
                ('dana', models.IntegerField(blank=True, null=True)),
                ('presentase_dana', models.FloatField(blank=True, null=True)),
                ('presentase_kumulatif_dana', models.FloatField(blank=True, null=True)),
                ('presentase_item', models.FloatField(blank=True, null=True)),
                ('presentase_kumulatif_item', models.FloatField(blank=True, null=True)),
                ('prioritas', models.CharField(blank=True, choices=[('A', 'Tinggi'), ('B', 'Sedang'), ('C', 'Rendah')], max_length=20, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('atk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='atk.barang_atk')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atk.unit')),
            ],
            options={
                'ordering': ['-updated', '-created'],
            },
        ),
        migrations.AlterField(
            model_name='harga',
            name='harga',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='penggunaanstok',
            name='tanggal',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 5, 24, 3, 34, 23, 646273, tzinfo=datetime.timezone.utc)),
        ),
        migrations.DeleteModel(
            name='abc_analysis',
        ),
        migrations.AddConstraint(
            model_name='abc_analysis_model',
            constraint=models.UniqueConstraint(fields=('atk', 'unit', 'tahun'), name='unique_atk_unit_tahun_abc'),
        ),
    ]
