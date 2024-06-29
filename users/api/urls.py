from django.urls import path
from users.api.views import *

urlpatterns = [
    path('users/', CustomUserListAPIView.as_view(), name='custom_user_list'),
    path('users/create/', CustomUserCreateAPIView.as_view(), name='custom_user_create'),
    path('users/<int:pk>', CustomUserRetrieveAPIView.as_view(), name='custom_user_retrieve'),
    path('normal-users/', NormalUserListAPIView.as_view(), name='normal_user_list'),
    path('normal-users/<int:pk>', NormalUserDetailAPIView.as_view(), name='normal_user_detail')
]

