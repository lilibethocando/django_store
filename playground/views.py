from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product, Customer, Collection, Order, OrderItem


def say_hello(request):
    queryset = Order.objects.all().select_related("customer").prefetch_related("orderitem_set__product").order_by("-placed_at")[:5]

    return render(request, "hello.html", {"orders": queryset})
