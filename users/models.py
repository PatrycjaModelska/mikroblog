from django.db import models
from django.contrib.auth.models import AbstractUser


# class Users(AbstractUser):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=50)
#     email = models.CharField(max_length=50, null=False)
#     password = models.CharField(max_length=30, null=False)
#     USERNAME_FIELD = "username"

#     class Meta:
#         verbose_name = "User"
#         verbose_name_plural = "Users"

#     def __str__(self):
#         return self.username
