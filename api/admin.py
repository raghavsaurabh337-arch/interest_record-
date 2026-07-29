from django.contrib import admin
from .models import Home


# Register your models here.
@admin.register(Home)
class homeAdmin(admin.ModelAdmin):
     list_display=['id','name','amount','interest_rate','date']

