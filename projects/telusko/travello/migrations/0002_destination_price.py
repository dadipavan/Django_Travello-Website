# Generated by Django 2.2.6 on 2019-10-14 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='price',
            field=models.ImageField(default=0, upload_to=''),
            preserve_default=False,
        ),
    ]