# Generated by Django 4.2 on 2023-04-05 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_remove_payment_invoice_remove_order_order_status_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='delivery_requirements',
            new_name='information',
        ),
    ]