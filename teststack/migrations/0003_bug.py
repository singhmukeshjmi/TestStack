# Generated by Django 3.2.12 on 2023-03-29 11:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teststack', '0002_project_project_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bug',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('steps_to_reproduce', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('bug_category', models.CharField(choices=[('Critical', 'Critical'), ('Blocker', 'Blocker'), ('Non Critical', 'Non Critical'), ('Undecided', 'Undecided')], default='Undecided', max_length=50)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='teststack.project')),
                ('testcase', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='teststack.testcase')),
            ],
        ),
    ]
