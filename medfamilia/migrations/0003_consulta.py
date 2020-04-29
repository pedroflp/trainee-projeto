# Generated by Django 3.0.5 on 2020-04-28 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medfamilia', '0002_auto_20200428_1919'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(max_length=100)),
                ('data', models.CharField(max_length=10)),
                ('turno', models.CharField(choices=[('manha', 'Manhã'), ('tarde', 'Tarde')], default='manha', max_length=10)),
                ('info_adicionais', models.TextField(null=True)),
                ('especialidade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='medfamilia.Especialidade')),
            ],
        ),
    ]