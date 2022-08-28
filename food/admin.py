from django.contrib import admin
from food import models
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )


class FoodAdmin(admin.ModelAdmin):
    list_display = ('title', 'cat',)
    list_filter = ('cat', )


admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Food, FoodAdmin)