from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Customer)
admin.site.register(Address)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Variation)
admin.site.register(Option)
admin.site.register(Transaction)
admin.site.register(Order)
admin.site.register(OrderItem)
