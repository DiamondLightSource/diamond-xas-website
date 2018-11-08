# Generated by Django 2.0.5 on 2018-07-10 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xasdb1', '0017_xasuploadauxdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='xasuploadauxdata',
            name='aux_description',
            field=models.CharField(blank=True, default='', max_length=256, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='xasuploadauxdata',
            name='aux_file',
            field=models.FileField(blank=True, upload_to='uploads/%Y/%m/%d/'),
        ),
    ]