# Generated by Django 2.0.7 on 2018-08-08 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0013_auto_20180808_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, default='food/static/placeholder-profile-pic.png', upload_to='food/static/media'),
        ),
    ]
