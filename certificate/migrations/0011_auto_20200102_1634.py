# Generated by Django 3.0.1 on 2020-01-02 15:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('certificate', '0010_auto_20200102_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
