from django.urls import path
from .views import *

urlpatterns = [
    path('', savepromf, name="savepromf"),
]


