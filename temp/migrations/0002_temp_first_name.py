# Generated by Django 4.2.13 on 2024-07-06 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='temp',
            name='first_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
