from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
# Create your models here.
class User(AbstractUser):
    is_admin=models.BooleanField('Is admin',default=False)
    is_teacher=models.BooleanField('Is teacher',default=False)
    is_student=models.BooleanField('Is student',default=False)
User = get_user_model()
