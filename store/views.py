from django.shortcuts import render, HttpResponse
from .models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
def product_list(request):
    queryset = Product.objects.all()
    return Response("products.html", {"products": list(queryset)})