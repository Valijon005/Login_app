# Generated by Django 3.1.7 on 2021-06-23 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboardapp', '0008_remove_mentor_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentor',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='mentors/'),
        ),
    ]