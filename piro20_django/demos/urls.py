from django.urls import path, include
from .views import *

app_name="demos"

urlpatterns = [
    path('index', index, name='index'),
    path('cal', car, name='index'),
    path('calculator', calculator, name='index'),
]

