from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from givito.account.views import UserMeChangePassword, UserMeView, UserRegisterView

urlpatterns = [
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('user/register/', UserRegisterView.as_view(), name="user_register"),
    path('user/me/', UserMeView.as_view(), name="user_me"),
    path('user/me/change_password/', UserMeChangePassword.as_view(), name="user_me"),
]
