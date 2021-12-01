# Generated by Django 3.2.9 on 2021-12-01 14:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('spotmes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spotme',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spot_mes', to=settings.AUTH_USER_MODEL),
        ),
    ]
