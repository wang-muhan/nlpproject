from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):#这个AbstractUser挺好用的，下面是附加的一些属性
    student_id = models.CharField(max_length=10) #学号
    chat_limitation = models.IntegerField(default=999999999)
    def __str__(self):
        return self.username