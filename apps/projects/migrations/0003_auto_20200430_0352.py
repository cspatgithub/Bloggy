# Generated by Django 3.0.5 on 2020-04-30 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_project_visit_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='techology',
        ),
        migrations.AddField(
            model_name='project',
            name='technology',
            field=models.CharField(default='', max_length=300),
        ),
    ]
