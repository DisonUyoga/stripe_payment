# Generated by Django 5.0.6 on 2024-06-18 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stripe_app', '0003_product_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='user',
        ),
        migrations.AddField(
            model_name='product',
            name='user_id',
            field=models.CharField(default='', max_length=255),
        ),
    ]