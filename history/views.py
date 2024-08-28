from rest_framework import generics
from .models import LoginLogoutHistory, TransactionHistory
from .serializers import LoginLogoutHistorySerializer, TransactionHistorySerializer
from rest_framework.permissions import IsAuthenticated

class LoginLogoutHistoryListView(generics.ListAPIView):
    queryset = LoginLogoutHistory.objects.all()
    serializer_class = LoginLogoutHistorySerializer
    permission_classes = [IsAuthenticated]

class TransactionHistoryListView(generics.ListAPIView):
    queryset = TransactionHistory.objects.all()
    serializer_class = TransactionHistorySerializer
    permission_classes = [IsAuthenticated]
