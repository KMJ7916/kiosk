from django.db import models

# Create your models here.

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name #매직 매서드(데이터를 바로 알 수 있음)

class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    name  =models.CharField(max_length=100)
    price = models.IntegerField()
    description=models.TextField()
    image = models.ImageField(upload_to='menu_images/', null=True, blank=True)
    def __str__(self):
        return self.name

class Order(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now=True)
    item_count = models.IntegerField()
    order_price = models.IntegerField()

    def __str__(self):
        return f"Order {self.id} - {self.item.name} (x{self.item_count})"  # 문자열 반환

class Cart(models.Model):
    item = models.ForeignKey(Item,on_delete=models.DO_NOTHING )
    amount =models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.name