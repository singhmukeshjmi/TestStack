# Generated by Django 4.1.7 on 2023-04-11 13:55

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('teststack', '0005_alter_bug_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testcase',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
    ]
