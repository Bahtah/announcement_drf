# Generated by Django 4.2.4 on 2023-09-05 16:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('announcement', '0008_announcement_price_announcement_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='announcement', to=settings.AUTH_USER_MODEL),
        ),
    ]
