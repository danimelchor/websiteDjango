# Generated by Django 3.1.3 on 2020-11-11 03:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('project_img', models.CharField(max_length=100)),
                ('project_tags', models.CharField(max_length=300)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
