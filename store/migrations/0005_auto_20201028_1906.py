# Generated by Django 3.1.1 on 2020-10-28 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_order_orderitem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='email',
            new_name='emailAddress',
        ),
    ]
