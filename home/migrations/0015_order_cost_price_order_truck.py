# Generated by Django 4.2 on 2023-04-06 05:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_delete_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cost_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='order',
            name='truck',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.truck'),
        ),
    ]