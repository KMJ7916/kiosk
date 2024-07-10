from django.db import models
from django.contrib.auth.models import User
from cafe.models import Item
# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    item = models.ForeignKey(Item,on_delete=models.DO_NOTHING )
    amount =models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.name