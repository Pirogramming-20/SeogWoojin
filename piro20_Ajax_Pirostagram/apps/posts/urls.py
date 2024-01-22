from django.urls import path,include
from .views import *

app_name='posts'

urlpatterns = [
    path('', main, name="main"),
    path('create/', create, name="create"),
    path('write_comment/', write_comment, name="comment"),
    path('change_like/', change_like, name="like"),
    path('delete_comment/', delete_comment, name="delete_comment"),
]