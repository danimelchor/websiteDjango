# Generated by Django 3.1.3 on 2021-01-13 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectfilter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_link',
            field=models.CharField(default='/', max_length=300),
            preserve_default=False,
        ),
    ]