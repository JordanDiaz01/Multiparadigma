# Generated by Django 4.2 on 2023-04-17 01:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contratos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patrocinadores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('idcontrato', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contratos.contratos')),
            ],
        ),
    ]
