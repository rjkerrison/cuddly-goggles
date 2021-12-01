# Generated by Django 3.2.9 on 2021-12-01 15:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('spotmes', '0002_alter_spotme_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spotme',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
