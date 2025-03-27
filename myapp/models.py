from django.db import models

from django.core.validators import RegexValidator, MinLengthValidator
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
# Create your models here.

# model for CustomerInfo
class CustomerInfo(models.Model):

    phone_validator = RegexValidator(
        regex= r'^\+?1?\d{9,15}$', 
        message= "Phone number must be between 9-15 digits long."
    )

    name = models.CharField(max_length= 60 , verbose_name= "Full Name")
    email = models.EmailField(verbose_name= "Email")
    phone = models.CharField(max_length=16 , validators=[phone_validator] , verbose_name= "Phone Nummber")
    message = models.TextField(verbose_name="Message")
    created_at = models.DateTimeField(auto_now_add = True , verbose_name = "Date Created")

    def __str__(self):
        return f"{self.name} - {self.email}"
    
    class Meta:
        verbose_name = "User Information"
        verbose_name_plural = "User Information Records"
        ordering = ['-created_at']


# model for Admins posts like photos and messages
class UserMessages(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE  , related_name="user")
    message = models.TextField(blank = True , null = True)
    images = models.ImageField(upload_to="images")

    def clean(self):
        if not self.message and not self.images:
            raise ValidationError("Either message or image is required")

    def save(self, *args , **kwargs):
        self.full_clean()
        return super().save(*args , **kwargs)

