# Generated by Django 5.0.6 on 2024-08-11 12:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_alter_productimage_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='main_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parent_category', to='inventory.category'),
        ),
    ]
