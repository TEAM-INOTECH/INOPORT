# Generated by Django 4.2 on 2023-04-05 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_rename_employee_contact_details'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contact_Details',
            new_name='Contact_Detail',
        ),
    ]