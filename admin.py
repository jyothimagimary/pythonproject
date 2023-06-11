from django.contrib import admin
from . models import Portfolio

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ("name","image","address","contact","email","objective","Skills")

# Register your models here.
admin.site.register(Portfolio, PortfolioAdmin)