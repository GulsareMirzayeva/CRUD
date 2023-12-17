from django.db import models

# Create your models here.

class Test(models.Model):
    ad = models.CharField(max_length=50)
    soyad = models.CharField(max_length=100)
    
    def __str__(self):
        return self.ad