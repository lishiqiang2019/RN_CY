# Generated by Django 2.2.5 on 2019-10-05 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dine', '0004_auto_20191005_0817'),
    ]

    operations = [
        migrations.AddField(
            model_name='food_info',
            name='food_imag',
            field=models.ImageField(default=1, upload_to='img'),
            preserve_default=False,
        ),
    ]
