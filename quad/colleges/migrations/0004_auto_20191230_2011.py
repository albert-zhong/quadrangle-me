# Generated by Django 3.0.1 on 2019-12-31 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colleges', '0003_collegeemail'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='comments_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='thread',
            name='hits',
            field=models.IntegerField(default=0),
        ),
    ]
