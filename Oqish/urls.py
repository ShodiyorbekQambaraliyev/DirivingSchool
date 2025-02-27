from django.urls import path
from .views import *

urlpatterns = [
    path('', hom_page)
]