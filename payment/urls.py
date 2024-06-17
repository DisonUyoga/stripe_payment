
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path("api/users/token/", obtain_auth_token),
    path("api/",include("djoser.urls")),
    path("api/v1/", include("stripe_app.urls")),
    path('admin/', admin.site.urls),
]
