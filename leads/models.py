from django.db import models
from django.contrib.auth.models import User,AbstractUser
class User(AbstractUser):
    pass


class Agents(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username 


class Leads(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey(Agents, on_delete=models.CASCADE)
