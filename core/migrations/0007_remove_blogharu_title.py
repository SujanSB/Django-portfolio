# Generated by Django 2.2.12 on 2021-03-02 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_blogharu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogharu',
            name='title',
        ),
    ]