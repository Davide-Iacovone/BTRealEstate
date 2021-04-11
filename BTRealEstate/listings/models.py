from django.db import models
from datetime import datetime
from realtors.models import Realtor

class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete = models.DO_NOTHING)
    title = models.CharField(max_length = 200)
    addres = models.CharField(max_length = 200)
    city = models.CharField(max_length = 200)
    state = models.CharField(max_length = 200)
    zipcode = models.CharField(max_length = 200)
    desciption = models.TextField(blank = True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits = 2, decimal_places = 1)
    garage = models.IntegerField(default = 0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits = 5, decimal_places = 1)
    photo_main = models.ImageField(upload_to = 'Photos/')
    is_published = models.BooleanField(default = True)
    list_date = models.DateTimeField(default = datetime.now, blank = True)
    def __str__(self):
        return self.title
