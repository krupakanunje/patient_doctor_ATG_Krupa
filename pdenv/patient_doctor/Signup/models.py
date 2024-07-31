from django.db import models

# Create your models here.
class Signup(models.Model):
    
    ROLES_CHOICES = [
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
        
    ]
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    confirm_password=models.CharField(max_length=30)
    role = models.CharField(max_length=20, choices=ROLES_CHOICES, default='Patient')

    #role=models.CharField(max_length=30,default="patient")
    email=models.EmailField(max_length=30)
    address=models.TextField(max_length=100)
    pincode= models.IntegerField(default=411016)
    state=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    pic= models.ImageField(upload_to="upload/",default="")

    
    class Meta:  
        db_table = "signup"  
