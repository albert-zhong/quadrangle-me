# Generated by Django 3.0.1 on 2019-12-30 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('colleges', '0002_auto_20191230_0031'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollegeEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.URLField(max_length=31)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emails', to='colleges.College')),
            ],
        ),
    ]