# Generated by Django 2.0.6 on 2018-07-25 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='height',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='weight',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
