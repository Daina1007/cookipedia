# Generated by Django 4.1.1 on 2022-10-10 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Ingredient",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ingredient_name", models.CharField(default="", max_length=40)),
                ("expiry_date", models.DateField()),
                ("price", models.IntegerField(verbose_name="가격")),
            ],
        ),
        migrations.CreateModel(
            name="IngredientCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "ingredient_category",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("과일", "과일"),
                            ("채소", "채소"),
                            ("정육, 계란", "정육, 계란"),
                            ("수산", "수산"),
                            ("우유, 유제품", "우유, 유제품"),
                            ("빵, 잼", "빵, 잼"),
                            ("양념", "양념"),
                            ("햄, 어묵, 통조림", "햄, 어묵, 통조림"),
                        ],
                        default="",
                        max_length=40,
                    ),
                ),
            ],
        ),
    ]
