from django.urls import path
from . import views

app_name="kiosk"
urlpatterns = [
    path('', views.rich_cafe),
    path('menu/',views.menu_list,name='menu_list'),
    path('order/',views.order_menu,name="order_menu"),
    path('result/',views.order_result,name="order_result"),
]