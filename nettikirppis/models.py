from django.db import models

# Create your models here.

class Item(models.Model):
    """
    Kirpputorilla myytävä tavara.
    """
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_added = models.DateField(auto_now_add=True)
    visible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} : {self.price}"
    
class Comment(models.Model):
    """
    Ihmisten myytäviin tavaroihin liittyvät ostajien kommentit, kyselyt, pyynnöt, tarkennukset, tarjoukset, ym.
    """
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    visible = models.BooleanField(default=True)

    def __str__(self):
        return self.text
