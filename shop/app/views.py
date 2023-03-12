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
    return render(request, 'app/index.html', data)


