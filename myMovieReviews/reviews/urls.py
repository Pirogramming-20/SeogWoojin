from django.urls import path, include
from .views import *
app_name = 'reviews'

urlpatterns = [
    path('', review_list),
    path('create',review_create),
    path('detail/<int:pk>', review_detail),
    path('edit/<int:pk>', review_update),
    path('delete/<int:pk>', review_delete),
]
