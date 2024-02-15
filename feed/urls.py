from django.urls import path
 
from . import views
 
urlpatterns=[
    path("dashboard/",views.feed,name="profile"),
    path("input/",views.input,name="input")

           ]