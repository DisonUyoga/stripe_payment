# Generated by Django 5.0.6 on 2024-06-19 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stripe_app', '0008_payment_customer_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=255)),
                ('customer_id', models.CharField(max_length=255)),
            ],
        ),
    ]
