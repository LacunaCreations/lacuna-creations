# Generated by Django 4.1.5 on 2023-09-25 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_dashboard', '0006_project_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='end_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]