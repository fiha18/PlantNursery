# Generated by Django 3.1.5 on 2021-01-07 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nursery_API', '0002_auto_20210107_0116'),
    ]

    operations = [
        migrations.AddField(
            model_name='nursery',
            name='password',
            field=models.CharField(default='password123', max_length=20),
        ),
        migrations.AddField(
            model_name='users',
            name='password',
            field=models.CharField(default='password123', max_length=20),
        ),
    ]
