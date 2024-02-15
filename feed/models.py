from django.db import models
from register.models import CustomUser

class Post_image(models.Model):
    author=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    photo=models.ImageField(upload_to="photos/")
    notes=models.CharField(max_length=200)
    time=models.TimeField()
    date=models.DateField()
    def __str__(self):
        return self.author.name

