# Generated by Django 4.2 on 2023-04-05 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_employee_delete_driver'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Employee',
            new_name='Contact_Details',
        ),
    ]
