# Generated by Django 3.0.1 on 2020-01-01 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colleges', '0006_auto_20191231_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college',
            name='banner',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='college',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
