# Generated by Django 3.0.1 on 2020-01-01 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colleges', '0005_auto_20191231_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='is_anonymous',
            field=models.BooleanField(default=False),
        ),
    ]
