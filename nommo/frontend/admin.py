from django.contrib import admin

from .models import Country, Category, Investment


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    # pass
@admin.register(Investment)
class InvestmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'category')
    pass
