# Generated by Django 5.0.6 on 2024-06-02 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='is_default',
            field=models.BooleanField(default=False),
        ),
    ]
