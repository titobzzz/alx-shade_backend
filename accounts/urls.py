from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


from . import views


urlpatterns=[
    path('',views.UserViewSet.as_view({"post":"create"}),name="registration"),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/',views.UserViewSet.as_view({"get":"list"}),name="list_user"),
    path('user/<str:pk>/',views.UserViewSet.as_view({"get":"retrieve"}),name="retriveuser")
]