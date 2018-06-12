# Generated by Django 2.0.5 on 2018-06-11 12:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('xasdb1', '0002_auto_20180607_1701'),
    ]

    operations = [
        migrations.CreateModel(
            name='XASArray',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('array', models.TextField()),
                ('unit', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='xasfile',
            name='edge',
            field=models.CharField(default='', max_length=3),
        ),
        migrations.AddField(
            model_name='xasfile',
            name='element',
            field=models.CharField(default='', max_length=3),
        ),
        migrations.AddField(
            model_name='xasfile',
            name='review_status',
            field=models.SmallIntegerField(choices=[(0, 'Pending'), (1, 'Approved'), (2, 'Rejected')], default=0),
        ),
        migrations.AddField(
            model_name='xasfile',
            name='uploader',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='xasarray',
            name='file',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xasdb1.XASFile'),
        ),
    ]