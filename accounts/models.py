from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    """拡張ユ－ザーモデル"""

    class Meta:
        verbosa_name_plural='CustomeUser'