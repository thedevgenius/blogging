# Generated by Django 4.1.4 on 2023-09-20 11:43

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_project_password_project_url_project_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]
