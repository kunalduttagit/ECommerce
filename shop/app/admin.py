from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin


# Register your models here.

from .models import *

admin.site.register(
    Category,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
        # ...more fields if you feel like it...
    ),
    list_display_links=(
        'indented_title',
    ),
)

admin.site.register(Customer)
admin.site.register(Address)
admin.site.register(Product)
admin.site.register(Variation)
admin.site.register(Option)
admin.site.register(Transaction)
admin.site.register(Order)
admin.site.register(OrderItem)