from django.urls import path
from . import views

urlpatterns = [
    path('',views.get_user,name="get-user"),
    path('post-user-data',views.post_user,name="post-user-data")
]
