# Generated by Django 3.1.7 on 2021-06-21 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboardapp', '0007_auto_20210618_1441'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mentor',
            name='photo',
        ),
    ]
