# Generated by Django 3.0.1 on 2019-12-31 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('certificate', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='certificate',
            old_name='user',
            new_name='profile',
        ),
    ]
