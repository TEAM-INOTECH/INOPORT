# Generated by Django 4.2 on 2023-04-05 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_rename_contact_details_contact_detail'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contact_Detail',
            new_name='Contact_Details',
        ),
    ]
