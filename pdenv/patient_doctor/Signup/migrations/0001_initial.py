# Generated by Django 4.2.14 on 2024-07-30 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Signup",
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
                ("first_name", models.CharField(default="rrr", max_length=20)),
                ("last_name", models.CharField(default="sam", max_length=20)),
                ("username", models.CharField(default="user", max_length=30)),
                ("password", models.CharField(max_length=30)),
                ("confirm_password", models.CharField(max_length=30)),
                ("role", models.CharField(default="patient", max_length=30)),
                ("email", models.EmailField(max_length=30)),
                ("address", models.TextField(default="Sai palace", max_length=100)),
                ("pincode", models.IntegerField(default=411016)),
                ("state", models.CharField(default="Maharashtra", max_length=30)),
                ("city", models.CharField(default="Mumbai", max_length=30)),
                ("pic", models.FileField(max_length=30, upload_to="")),
            ],
            options={"db_table": "signup",},
        ),
    ]
