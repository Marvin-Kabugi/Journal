from django.urls import path

from . import views

urlpatterns = [
    path('users', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user-detail'),
    path('user/signup', views.RegisterUser.as_view(), name='register-user'),
    path('user/verify-email/', views.VerifyEmail.as_view(), name='verify-email')
]