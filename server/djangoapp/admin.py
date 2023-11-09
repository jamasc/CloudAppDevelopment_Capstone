from django.contrib import admin
from .models import CarModel, CarMake


# Register your models here.

# CarModelInline class
class ModelInline(admin.StackedInline):
    model = CarModel 
# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    fields = ['name', 'dealer_id','car_type','year']
# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    fields = ['name', 'description']
    inlines = [ModelInline]
# Register models here
admin.site.register(CarModel, CarModelAdmin)
admin.site.register(CarMake, CarMakeAdmin)
