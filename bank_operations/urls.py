from django.urls import path
from .views import BankAccountCreateView, TransactionCreateView

urlpatterns = [
    path('create_account/', BankAccountCreateView.as_view(), name='create-account'),
    path('transaction/', TransactionCreateView.as_view(), name='transaction'),
]
