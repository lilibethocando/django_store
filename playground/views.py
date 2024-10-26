from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product, Customer, Collection, OrderItem


def say_hello(request):
    queryset = OrderItem.objects.values("product_id").distinct()

    return render(request, "hello.html", {"products": queryset})
