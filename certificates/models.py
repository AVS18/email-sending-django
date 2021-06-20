from django.db import models

# Create your models here.
class Email(models.Model):
    par_name = models.CharField(max_length=100)
    par_email = models.EmailField()
    par_cerf = models.FileField(upload_to='cerf/')
    par_event = models.CharField(max_length=100,blank=True)