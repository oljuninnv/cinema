from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Rate)

admin.site.register(Genre)

@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('name_price','price')
    list_filter = ('name_price','price')

@admin.register(Hall)
class HallAdmin(admin.ModelAdmin):
    list_display = ('name_hall','capacity')
    list_filter = ('name_hall','capacity')

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ("date","name_film","rate",'genre')
    list_filter = ('name_film',"date",'genre',"rate")
    
@admin.register(Seans)
class SeansAdmin(admin.ModelAdmin):
    list_display = ('film','time_begin','price_seans','status')
    list_filter = ('film','hall','date','time_begin','price_seans','status')
    
@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('seans','price')
    list_filter = ('seans','price')