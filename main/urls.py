
from django.contrib import admin
from django.urls import path,include
# from user import views as user_views
from django.conf.urls.static import static
from django.conf import settings
from . import views
app_name='main'
urlpatterns = [
    path('',views.main_page,name="main_page"),
    path('toabtpage',views.toabtpage,name="toabtpage"),
]
