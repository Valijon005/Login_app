# Generated by Django 3.2.1 on 2021-06-16 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboardapp', '0004_course_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='finish',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='price',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='start',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='student_qty',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
