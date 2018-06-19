# Generated by Django 2.0.5 on 2018-06-15 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('xasdb1', '0007_auto_20180615_1602'),
    ]

    operations = [
        migrations.CreateModel(
            name='XASMode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode', models.SmallIntegerField(choices=[(-1, 'Unknown'), (0, 'Transmission'), (1, 'Fluorescence')], default=-1)),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xasdb1.XASFile')),
            ],
        ),
    ]
