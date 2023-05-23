# Generated by Django 4.2 on 2023-05-22 05:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('atk', '0016_alter_penggunaanstok_atk'),
    ]

    operations = [
        migrations.CreateModel(
            name='PengambahanStok',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jumlah', models.BigIntegerField()),
                ('tanggal', models.DateField()),
                ('keterangan', models.CharField(blank=True, max_length=200, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('atk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='atk.barang_atk')),
            ],
            options={
                'ordering': ['-updated', '-created'],
            },
        ),
    ]
