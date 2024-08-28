from django.urls import path
from .views import UserCreateView, UserListView, UserLoginView, UserLogoutView, UserDashboardView

urlpatterns = [
    path('signup/', UserCreateView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('dashboard/', UserDashboardView.as_view(), name='user-dashboard'),
]
