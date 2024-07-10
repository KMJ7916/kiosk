from django.urls import path
from . import views

app_name="cafe"
urlpatterns = [
    path('', views.rich_cafe),
    path('menu/',views.menu_list,name='menu_list'),
    path('menu_detail/<int:pk>',views.menu_detail,name='menu_detail'),
    path('order/',views.order_menu,name="order_menu"),
    path('result/',views.order_result,name="order_result"),
    path('modify_cart/',views.modify_cart,name='modify_cart'),
]