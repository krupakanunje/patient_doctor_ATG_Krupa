# Generated by Django 4.2.14 on 2024-07-31 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Signup", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="signup",
            name="pic",
            field=models.ImageField(default="", upload_to="upload/images"),
        ),
    ]
