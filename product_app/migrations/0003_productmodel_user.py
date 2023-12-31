# Generated by Django 4.2.7 on 2023-12-03 14:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product_app', '0002_productmodel_image_productmodel_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='products', to=settings.AUTH_USER_MODEL),
        ),
    ]
