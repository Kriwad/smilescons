from django.db import models

# Create your models here.

class CustomerInfo(models.Model):

    name = models.CharField(max_length= 60 , verbose_name= "Full Name")
    email = models.EmailField(verbose_name= "Email")
    phone = models.IntegerField(verbose_name="Phone Number")
    message = models.TextField(verbose_name="Message")
    created_at = models.DateTimeField(auto_now_add = True , verbose_name = "Date Created")

    def __str__(self):
        return f"{self.name} - {self.email}"
    
    class Meta:
        verbose_name = "User Information"
        verbose_name_plural = "User Information Records"
        ordering = ['-created_at']
