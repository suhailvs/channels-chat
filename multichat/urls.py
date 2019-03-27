from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
# from django.contrib.auth import login
from chat.views import index


urlpatterns = [
    path('', index),
    # path('accounts/login/', login),
    path('accounts/login/', LoginView.as_view(), name="login"),
    path('accounts/logout/', LogoutView.as_view()),
    path('admin/', admin.site.urls),
]
