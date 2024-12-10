from django.db import models
from django.contrib.auth.models import User

import time

# Create your models here.

# Relatiivinen filename kuville 
#'images/[user_id]/[unix timestamp].[file extension]'
def content_file_name(instance, filename):
    name, ext = filename.split('.')
    file_path = 'images/{user_id}/{timestamp}.{ext}'.format(
        user_id=instance.owner.id,timestamp= str(int(time.time())), ext=ext) 
    return file_path

class Item(models.Model):
    """
    Kirpputorilla myytävä tavara.
    """
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_added = models.DateField(auto_now_add=True)
    visible = models.BooleanField(default=True)
    owner=models.ForeignKey(User, on_delete=models.CASCADE)

    # Kuva
    image = models.ImageField(upload_to=content_file_name, null=True, blank=True)

    def __str__(self):
        return f"{self.name} : {self.price}€"
    
class Comment(models.Model):
    """
    Ihmisten myytäviin tavaroihin liittyvät ostajien kommentit, ym.
    """
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    visible = models.BooleanField(default=True)
    owner=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class Reply(Comment):
    """
    Kommentteihin vastaaminen.
    """

    original_comment = models.ForeignKey(Comment, related_name='rel', on_delete=models.CASCADE)


