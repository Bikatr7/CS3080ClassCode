from django.contrib import admin
from django.urls import path
from token_auth_app.views import loginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/login/", loginView),
]