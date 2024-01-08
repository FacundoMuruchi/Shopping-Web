from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    desc = RichTextField(max_length=1000)
    img = models.ImageField(upload_to='posts')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}, ${self.price}'