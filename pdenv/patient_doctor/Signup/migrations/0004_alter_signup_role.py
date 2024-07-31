# Generated by Django 4.2.14 on 2024-07-31 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Signup", "0003_alter_signup_pic"),
    ]

    operations = [
        migrations.AlterField(
            model_name="signup",
            name="role",
            field=models.CharField(
                choices=[("patient", "Patient"), ("doctor", "Doctor")],
                default="Patient",
                max_length=20,
            ),
        ),
    ]
