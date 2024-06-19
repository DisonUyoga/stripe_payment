# Generated by Django 5.0.6 on 2024-06-19 06:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stripe_app', '0011_alter_payment_customer_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stripe_app.customer'),
        ),
    ]