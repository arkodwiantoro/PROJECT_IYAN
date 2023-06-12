from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Armada(models.Model):
    name = models.CharField(max_length=200, null=True)
    harga = models.FloatField()
    image = models.ImageField()
    created = models.DateTimeField(auto_now_add=True, null=True)

    @property
    def imageURL(self):
        try :
            url = self.image.url
        except:
            url = ''
        return url
    

    def __str__(self):
        return self.name


class Testi(models.Model):
    image = models.ImageField()
    created = models.DateTimeField(auto_now_add=True, null=True)

    @property
    def imageURL(self):
        try :
            url = self.image.url
        except:
            url = ''
        return url

class Order(models.Model):
    STATUS = (
        ('Pending', "Pending"),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered')
    )

    armada = models.ForeignKey(Armada, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    tgl_mulai = models.DateField()
    durasi = models.IntegerField()
    status = models.CharField(max_length=200, null=True, blank=True, choices=STATUS, default=STATUS[0])
    created = models.DateTimeField(auto_now_add=True, null=True)


    @property
    def total_price(self):
        return self.durasi * self.armada.harga
