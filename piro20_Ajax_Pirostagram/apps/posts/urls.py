from django.urls import path,include
from .views import *

app_name='posts'

urlpatterns = [
    path('', main, name="main"),
    path('create/', create, name="create"),
    path('write_comment/', write_comment, name="comment"),
    # path('detail/<int:pk>', detail, name="detail"),
    # path('update/<int:pk>', update, name="update"),
    # path('delete/<int:pk>', delete, name="delete"),
    # path('change_interest/', change_interest, name='change_interest'),
    # path('change_heart/', change_heart, name='change_heart'),
]