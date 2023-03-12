from django.db import models
from djmoney.money import Money
from mptt.models import MPTTModel, TreeForeignKey
from djmoney.models.fields import MoneyField
from tinymce.models import HTMLField


# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=100, null=False)
    password = models.CharField(max_length=255, null=False)
    phone = models.PositiveBigIntegerField(null=True)

    def __str__(self):
        return self.name


class Address(models.Model):
    user_id = models.ForeignKey(Customer, null=False, on_delete=models.CASCADE, verbose_name="Customer Name")
    building = models.CharField(max_length=255, null=False)
    address1 = models.CharField(max_length=255, null=True, verbose_name="Address Line 1")
    address2 = models.CharField(max_length=255, null=True, verbose_name="Address Line 2")
    city = models.CharField(max_length=50, null=False)
    pin_code = models.PositiveIntegerField(null=False)
    country = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.user_id.name + "'s address"


class Category(MPTTModel):
    parent = TreeForeignKey("self", null=True, blank=True, on_delete=models.CASCADE, related_name='children')
    name = models.CharField(max_length=127, null=False, unique=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=500, null=False)
    description = HTMLField(max_length=511, null=True, blank=True)
    price = models.PositiveIntegerField(null=False)
    merchant_name = models.CharField(max_length=50, null=False)
    company = models.CharField(max_length=50, null=False)
    discount = models.PositiveIntegerField(null=True, blank=True)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name


class Gallery(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    photo_url = models.URLField(blank=True, null=True, default="https://images.unsplash.com/photo-1598620617137-2ab990aadd37?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1740&q=80")

    def __str__(self):
        return self.product_id.name


class Variation(models.Model):
    category_id = models.ForeignKey(Category, null=True, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.category_id.name + "'s " + self.name


class Option(models.Model):
    variation_id = models.ForeignKey(Variation, null=True, blank=True, on_delete=models.CASCADE)
    value = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.value


class Transaction(models.Model):
    method_options = (('credit_card', 'Credit Card'), ('debit_card', 'Debit Card'), ('wallet', 'Wallets'),
               ('netbanking', 'Net Banking'), ('upi', 'UPI'), ('pod', 'Pay on Delivery'))
    date = models.DateTimeField(auto_now_add=True)
    amount = MoneyField(max_digits=10, decimal_places=2, default_currency='INR')
    method = models.CharField(max_length=63, null=False, choices=method_options, default='pod')

    def __str__(self):
        return "Trnx-ID: " + str(self.id)


class Order(models.Model):
    customer_id = models.ForeignKey(Customer, null=False, on_delete=models.CASCADE)
    order_status_options = (('pending', 'Pending'), ('order_placed', 'Order Placed'), ('dispatched', 'Dispatched'),
                    ('shipped', 'Shipped'), ('delivered', 'Delivered'),)
    payment_id = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    order_status = models.CharField(max_length=62, null=False, choices=order_status_options, default='order_placed')

    def __str__(self):
        return self.customer_id.name


class OrderItem(models.Model):
    order_id = models.ForeignKey(Order, null=False, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.order_id.customer.id.name


class Cart(models.Model):
    card = 5

