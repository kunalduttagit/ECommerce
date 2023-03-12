# Generated by Django 4.1.7 on 2023-03-11 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_transaction_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('pending', 'Pending'), ('order_placed', 'Order Placed'), ('dispatched', 'Dispatched'), ('shipped', 'Shipped'), ('delivered', 'Delivered')], default='order_placed', max_length=62),
        ),
        migrations.AddField(
            model_name='transaction',
            name='method',
            field=models.CharField(choices=[('credit_card', 'Credit Card'), ('debit_card', 'Debit Card'), ('wallet', 'Wallets'), ('netbanking', 'Net Banking'), ('upi', 'UPI'), ('pod', 'Pay on Delivery')], default='pod', max_length=63),
        ),
    ]
