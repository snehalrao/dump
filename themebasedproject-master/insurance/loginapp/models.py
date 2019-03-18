from django.db import models

# Create your models here.

class  User_insurance(models.Model):
    usr_id = models.CharField(max_length = 100, unique = True)
    usr_pass = models.CharField(max_length = 100, unique = True)

    def __str__(self):
        return self.usr_id
class Image(models.Model):
    name= models.CharField(max_length=500)
    videofile= models.FileField(upload_to='images/', null=True, verbose_name="")

    def __str__(self):
        return self.name + ": " + str(self.imagefile)
