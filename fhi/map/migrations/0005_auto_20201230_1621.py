# Generated by Django 3.1 on 2020-12-30 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0004_auto_20201221_0845'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planttype',
            name='image',
        ),
        migrations.AddField(
            model_name='planttype',
            name='lat_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='planttype',
            name='short_descroption',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='planttype',
            name='wiki',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='planttype',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
