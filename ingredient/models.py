from django.db import models

# Create your models here.

class IngredientCategory(models.Model):
    INGREDIENT_CATEGORY_CHOICES = [
        ("과일", "과일"),
        ("채소", "채소"),
        ("정육, 계란", "정육, 계란"),
        ("수산", "수산"),
        ("우유, 유제품","우유, 유제품"),
        ("빵, 잼", "빵, 잼"),
        ("양념", "양념"),
        ("햄, 어묵, 통조림", "햄, 어묵, 통조림"),
    ]
    #카테고리 종류 채우기
    ingredient_category = models.CharField(blank = True, choices = INGREDIENT_CATEGORY_CHOICES, max_length = 40, default = '')

class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=40, default = '')
    expiry_date = models.DateField(auto_now = False, auto_now_add=False, null=False)
    #유통기한 의미
    price = models.IntegerField(verbose_name = "가격")