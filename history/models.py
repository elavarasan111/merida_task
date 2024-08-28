from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginLogoutHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    login_time = models.DateTimeField()
    logout_time = models.DateTimeField(null=True, blank=True)
    # Other fields can be added here

    def __str__(self):
        return f"{self.user.username} - {self.login_time}"

class TransactionHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=50)  # e.g., 'deposit', 'withdrawal'
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField()
    # Other fields can be added here

    def __str__(self):
        return f"{self.user.username} - {self.transaction_type} - {self.amount}"
