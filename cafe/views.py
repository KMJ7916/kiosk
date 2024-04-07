from django.shortcuts import render
from .models import Category, Item, Order

# Create your views here.

def rich_cafe(request):
    categorys=Category.objects.all()
    context= {
        "lions":categorys
    }
    return render(request,"cafe/rich_cafe.html",context)

def order_menu(request):
    return render(request,"cafe/order_menu.html")

def order_result(request):
    return render(request,"cafe/order_result.html" )