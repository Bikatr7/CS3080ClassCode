from django.contrib import admin
from django.urls import path
from token_auth_app.views import loginView, redirect_to_admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", redirect_to_admin),
    path("api/login/", loginView),
]