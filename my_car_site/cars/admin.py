from django.contrib import admin
from cars.models import Car
# Register your models here.

class CarAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Time Information', {'fields': ['year']}),
        ('Car Information', {'fields': ['brand']})
    ]

admin.site.register(Car, CarAdmin)
