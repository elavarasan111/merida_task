from django.urls import path
from .views import LoginLogoutHistoryListView, TransactionHistoryListView

urlpatterns = [
    path('login_history/', LoginLogoutHistoryListView.as_view(), name='login-history'),
    path('transaction_history/', TransactionHistoryListView.as_view(), name='transaction-history'),
]
