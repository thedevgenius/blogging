# Generated by Django 4.1.4 on 2023-09-29 13:00

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(default=''),
        ),
    ]
