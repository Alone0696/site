from django.db import models
from django.contrib.auth.models import User

class Mainapp(models.Model):
    text = models.TextField(blank=True)
    name = models.OneToOneField(User,on_delete = models.CASCADE,primary_key=True)

    def __str__(self):
        return self.text