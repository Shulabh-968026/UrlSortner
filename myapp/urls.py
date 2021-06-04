
from django.urls import path
from . import views

app_name="myapp"

urlpatterns = [
    path("",views.home,name="home"),
    path("url/",views.index,name="index"),
    path("<str:key>/",views.sort_url,name="sort_url"),
]