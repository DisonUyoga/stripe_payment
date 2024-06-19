# Generated by Django 5.0.6 on 2024-06-19 06:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stripe_app', '0009_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stripe_app.customer'),
        ),
    ]