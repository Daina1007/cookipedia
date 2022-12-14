# Generated by Django 4.1.1 on 2022-10-10 05:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("food", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("ingredient", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="like",
            name="like_user",
            field=models.OneToOneField(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="food",
            name="ingredient",
            field=models.ManyToManyField(
                related_name="food_ingredient", to="ingredient.ingredient"
            ),
        ),
        migrations.AddField(
            model_name="comment",
            name="comment_user",
            field=models.OneToOneField(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
