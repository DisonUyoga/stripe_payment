# Generated by Django 5.0.6 on 2024-06-19 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stripe_app', '0006_alter_payment_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='user',
            field=models.CharField(max_length=255),
        ),
    ]
