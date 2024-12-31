from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField



# Create your models here.

class Musician(models.Model):
    f_name=models.CharField(max_length=50)  #labels="First Name" will be added later on forms
    l_name=models.CharField(max_length=50)
    email=models.EmailField(default="example@example.com")
    phone_number = models.CharField(max_length=12)
    instrument_type=models.CharField(max_length=20,null=True)
  
    
    def __str__(self) -> str:
        return f"Musician Name: {self.f_name}"
