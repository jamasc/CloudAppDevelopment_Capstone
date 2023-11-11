from django.db import models
from django.utils.timezone import now


# Create your models here.

class CarMake(models.Model):
    name = models.CharField(null=False, max_length=30, default='car make')
    description = models.CharField(max_length=1000)

    def __str__(self):
        return "Name: " + self.name + "," + \
               "Description: " + self.description

class CarModel(models.Model):
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(null=False, max_length=30, default='car model')
    dealer_id = models.IntegerField()
    SEDAN = 'sedan'
    SUV = 'suv'
    WAGON = 'wagon'
    VAN = 'van'
    TYPE_CHOICES = [
        (SEDAN, 'sedan'),
        (SUV, 'suv'),
        (WAGON, 'wagon'),
        (VAN, 'van')
    ]
    car_type = models.CharField(
        null=False,
        max_length=20,
        choices=TYPE_CHOICES,
    )
    year = models.DateField()

    def __str__(self):
        return "Name: " + self.name + "," + \
               "Description: " + self.car_type

class CarDealer:
    def __init__(self, id, city, state, st, address, zip, lat, longt, short_name, full_name):
        self.id = id
        self.city = city
        self.state = state
        self.st = st
        self.address = address
        self.zip = zip
        self.lat = lat
        self.longt = longt
        self.short_name = short_name
        self.full_name = full_name

    def __str__(self):
        return "Dealer name: " + self.full_name

# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview:
    def __init__(self, dealership, name, purchase, review, purchase_date, car_make, car_model, car_year, sentiment, id):
        self.dealership = dealership
        self.name = name
        self.purchase = purchase
        self.review = review
        self.purchase_date = purchase_date,
        self.car_make = car_make
        self.car_model = car_model
        self.car_year = car_year
        self.sentiment = sentiment
        self.id = id
