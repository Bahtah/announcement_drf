# Generated by Django 4.2.4 on 2023-08-31 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='создано'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='main_image',
            field=models.ImageField(upload_to='images/announcement/', verbose_name='фото'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='title',
            field=models.CharField(max_length=155, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='обновлено'),
        ),
    ]
