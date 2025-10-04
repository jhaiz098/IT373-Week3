from django.urls import path
from library.views import home

urlpatterns = [
    path('', home, name="home")
]