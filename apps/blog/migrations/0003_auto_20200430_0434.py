# Generated by Django 3.0.5 on 2020-04-30 04:34

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200430_0057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='header',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]