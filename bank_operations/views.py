from rest_framework import generics
from .models import BankAccount, Transaction
from .serializers import BankAccountSerializer, TransactionSerializer
from rest_framework.permissions import IsAuthenticated

class BankAccountCreateView(generics.CreateAPIView):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer
    permission_classes = [IsAuthenticated]

class TransactionCreateView(generics.CreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]
