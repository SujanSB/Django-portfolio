# Generated by Django 2.2.12 on 2021-03-30 02:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20210330_0224'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogharu',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]