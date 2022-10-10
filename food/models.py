from email.policy import default
from django.db import models
from core.models import TimeStampedModel

# Create your models here.


class FoodCategory(models.Model):
    FOOD_CATEGORY_CHOICES = [
        ("한식", "한식"),
        ("양식", "양식"),
        ("일식", "일식"),
        ("분식", "분식"),
        ("베이킹", "베이킹"),
    ]
    # 카테고리 종류 채우기

    food_category = models.CharField(
        blank=True, choices=FOOD_CATEGORY_CHOICES, max_length=40, default='')

    MACHINE_CATEGORY_CHOICES = [
        ("필요없음", "필요없음"),
        ("전자레인지", "전자레인지"),
        ("오븐", "오븐"),
        ("에어프라이기", "에어프라이기"),
        ("인덕션", "인덕션"),
        ("기타", "기타"),
    ]
    # 카테고리 종류 채우기
    machine_category = models.CharField(
        blank=True, choices=MACHINE_CATEGORY_CHOICES, max_length=40, default='')


class Recipe(models.Model):
    # ingredient = models.ManyToManyField() - food 에서 이미 재료 선택 완료 굳이 필요?
    recipe = models.TextField()
    # 레시피 순서에 맞게 입력할 수 있도록 하면 좋지않을깡
    food = models.OneToOneField(
        "Food", related_name="recipe", on_delete=models.CASCADE)


class Food(models.Model):
    LEVEL_CHOICES = [("*", "*"), ("**", "**"), ("***", "***"),
                     ("****", "****"), ("*****", "*****"), ]
    COOK_HOUR = [("0", "0"), ("1", "1"), ("2", "2"), ("3", "3"),
                 ("4", "4"), ("5", "5"), ("6", "6"), ("7", "7"), ]
    COOK_MINUTE = [("10", "10"), ("20", "20"), ("30", "30"),
                   ("40", "40"), ("50", "50"), ]

    food_name = models.CharField(
        max_length=50, default="", null=True, blank=True)
    level = models.CharField(
        blank=False, choices=LEVEL_CHOICES, max_length=40, default='')
    cooktime_hour = models.CharField(
        blank=False, choices=COOK_HOUR, max_length=40, default='')
    cooktime_minute = models.CharField(
        blank=False, choices=COOK_MINUTE, max_length=40, default='')
    ingredient = models.ManyToManyField(
        "ingredient.Ingredient", related_name="food_ingredient")

    like_count = models.PositiveIntegerField(default='', null=True, blank=True)
    # 좋아요 기능 구현하고 싶당

    def __str__(self) -> str:
        return f"{self.food_name} with {self.like_count} ❤️"


class Comment(TimeStampedModel):
    comment_user = models.OneToOneField(
        "user.User", on_delete=models.CASCADE, default='')
    comment = models.TextField()
    comment_food = models.ForeignKey(
        "Food", on_delete=models.CASCADE, default='')


class Like(models.Model):
    like_user = models.OneToOneField(
        "user.User", on_delete=models.CASCADE, default='')
    like = models.ManyToManyField(
        'Food', blank=True, related_name='like_users')
