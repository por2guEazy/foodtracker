# Generated by Django 2.0.6 on 2018-07-26 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_remove_userprofile_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='height',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='weight',
            field=models.PositiveIntegerField(),
        ),
    ]
