from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
import datetime
# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=200, blank=True)
    profile_pic = models.ImageField(blank=True, null=True, upload_to='profile_pic/')
    date_crated = models.DateTimeField(default=datetime.datetime.now(), blank=True)


    def save(self, *args, **kwargs):
        self.name = self.user.username
        super(Customer, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
        

def Customer_Profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='customer')
        instance.groups.add(group)
        Customer.objects.create(user=instance, name=instance.username)

post_save.connect(Customer_Profile, sender=User)

class Tag(models.Model):
    name = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name



class Product(models.Model):
    CATEGORY = (
        ('indoor','indoor'),
        ('outdoor','outdoor'),
    )

    name = models.CharField(max_length=200, blank=True)
    category = models.CharField(max_length=200, blank=True, choices=CATEGORY)
    price = models.FloatField(validators=[MinValueValidator(0)], blank=True)
    description = models.TextField(max_length=400, blank=True)
    date_crated = models.DateTimeField(default=datetime.datetime.now(), blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    def __str__(self):
        return self.name



class Order(models.Model):
    STATUS = (
        ('Pending','Pending'),
        ('Out for delivery','Out for delivery'),
        ('Delivered','Delivered'),
    )

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(default=datetime.datetime.now(), blank=True)
    status = models.CharField(max_length=200, blank=True, choices=STATUS)
    
    def __str__(self):
        return self.product.name + ' order'