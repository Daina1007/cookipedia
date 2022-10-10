from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Address(models.Model):
    pass
    # 광역시, 구, 동까지 표현하면 좋을듯? 커뮤니티 생성시 필요하다고 생각


class User(AbstractUser):
    nickname = models.CharField(max_length=40, unique=True, default='')
    avatar = models.ImageField(
        blank=True, null=True, upload_to="avatar/%Y/%m/%d/")
    phone_number = models.CharField(max_length=11, unique=True, default='')
    address = models.ForeignKey("Address", on_delete=models.CASCADE)
    # 주소를 선택할 수 있으면 좋을 듯 함.


class UserIngredient(models.Model):
    has_ingredient = models.ForeignKey("User", on_delete=models.CASCADE)
    bought_ingredient_date = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True)
