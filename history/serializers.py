from rest_framework import serializers
from .models import LoginLogoutHistory, TransactionHistory

class LoginLogoutHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginLogoutHistory
        fields = '__all__'

class TransactionHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionHistory
        fields = '__all__'
