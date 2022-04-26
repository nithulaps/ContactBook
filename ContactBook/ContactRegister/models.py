from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class contactregister(models.Model):
    name=models.CharField(max_length=20,blank=True)
    contact_num = PhoneNumberField(blank=True)

    def __str__(self):
        return self.name
    
    



