from django.db import models

class Realtor(models.Model):
    name = models.CharField(max_length = 200)
    photo = models.ImageField(upload_to = 'Photos/')
    description = models.TextField(blank =  True)
    phone = models.CharField(max_length = 20)
    is_mvp = models.BooleanField(default = False)
    def __str__(self):
        return self.name
    
