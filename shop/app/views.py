from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import *
from djmoney.money import Money


def home(request):
    laptop = Category.objects.get(name="Laptop")
    filters = Variation.objects.get(category_id=laptop.id)
    values = Option.objects.filter(variation_id = filters.id)
    data = {"laptop": laptop, "filters": filters, "values": values}
    electronic = Category.objects.get(name='Electronic').get_descendants(include_self=False)
    fashion = Category.objects.get(name='Fashion').get_descendants(include_self=False)
    beauty = Category.objects.get(name="Beauty").get_descendants(include_self=False)
    grocery = Category.objects.get(name="Grocery").get_descendants(include_self=False)
    home = Category.objects.get(name="Home & Living").get_descendants(include_self=False)
    labels = ['Electronics', 'Fashion', 'Beauty', 'Grocery', 'Home & Living']
    context = [electronic, fashion, beauty, grocery, home]
    dic = dict(zip(context, labels))
    #tree = obj.get_descendants().filter(level__lte=obj.level + 2)
    return render(request, 'app/index.html', {'dic': dic})

