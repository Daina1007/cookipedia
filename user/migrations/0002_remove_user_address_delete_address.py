# Generated by Django 4.1.1 on 2022-10-10 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="address",
        ),
        migrations.DeleteModel(
            name="Address",
        ),
    ]