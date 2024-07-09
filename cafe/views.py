from django.shortcuts import render
from .models import Category, Item, Order

# Create your views here.

def menu_list(request):
    menu_items = Item.objects.all()
    return render(request,'cafe/menu_list.html',{'menu_list': menu_items})

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