# Generated by Django 3.2.12 on 2023-03-29 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teststack', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_status',
            field=models.CharField(choices=[('Not started', 'Not started'), ('Under investigation / testcase creation', 'Under investigation / testcase creation'), ('Under testing', 'Under testing'), ('Tested', 'Tested'), ('Sent for fixation', 'Sent for fixation'), ('Ready for Launch with some known bugs', 'Ready for Launch with some known bugs'), ('Ready for Launch', 'Ready for Launch')], default='Not started', max_length=50),
        ),
    ]
