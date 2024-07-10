from django.shortcuts import render
from .models import Category, Item, Order,Cart
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def menu_list(request):
    menu_items = Item.objects.all()
    return render(request,'cafe/menu_list.html',{'menu_list': menu_items})

def menu_detail(request,pk):
    menu = Item.objects.get(pk=pk)
    return render(request,'cafe/menu_detail.html',{'menu': menu})

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Sum
from .models import Item, Cart

@csrf_exempt
def modify_cart(request):
    if request.method == 'POST':
        item_id = request.POST.get('itemId')
        amount_change = request.POST.get('amountChange')

        if item_id is not None and amount_change is not None:
            try:
                item = Item.objects.get(pk=item_id)
                
                cart = request.session.get('cart', {})
                
                if item_id in cart:
                    cart[item_id]['amount'] += int(amount_change)
                else:
                    cart[item_id] = {
                        'name': item.name,
                        'price': str(item.price),  # Convert to string for JSON serialization
                        'amount': int(amount_change)
                    }
                
                if cart[item_id]['amount'] <= 0:
                    del cart[item_id]  # Remove item if the amount is 0 or less
                
                request.session['cart'] = cart

                total_quantity = sum(item['amount'] for item in cart.values())
                
                context = {
                    'newQuantity': cart[item_id]['amount'] if item_id in cart else 0,
                    'totalQuantity': total_quantity,
                    'message': '성공',
                    'success': True
                }
                return JsonResponse(context)
            except Item.DoesNotExist:
                return JsonResponse({'message': 'Item not found', 'success': False}, status=404)
        else:
            return JsonResponse({'message': 'Invalid data provided', 'success': False}, status=400)
    else:
        return JsonResponse({'message': 'Invalid request method', 'success': False}, status=405)


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