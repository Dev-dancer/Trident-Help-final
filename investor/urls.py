from . import views
from django.urls import path
app_name='investor'
urlpatterns = [
    path('',views.main,name='main'),
    path('investment',views.investment,name='investment'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('details',views.investment_details,name='details'),
    path('success',views.success,name='success')
]