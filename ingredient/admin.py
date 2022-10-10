from django.contrib import admin
from . import models

@admin.register(models.Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass

