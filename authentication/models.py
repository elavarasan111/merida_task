from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    bank = models.CharField(max_length=50)  # 'SBI', 'ICICI BANK', 'KTK BANK'
    is_employee = models.BooleanField(default=False)  # To differentiate bank employees from regular users

    def __str__(self):
        return self.username
