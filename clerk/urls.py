from . import views
from django.urls import path
app_name='clerk'
urlpatterns = [
    # path('',views.main,name='main'),
    # path('register/',views.registerClerk,name='registerClerk'),
    path('login/',views.loginClerk,name='loginClerk'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('dash_to_userreg/',views.dash_to_userreg,name='dash_to_userreg'),
    path('register_user/',views.register_user,name='register_user'),
    path ('dash_to_ourfund/',views.dash_to_ourfund,name='dash_to_ourfund'),
    path ('ourfundtosuccess/',views.ourfundtosuccess,name='ourfundtosuccess'),
    path ('succestohome/',views.succestohome,name='succestohome'),
    path ('dashtoloi/',views.dashtoloi,name='dashtoloi'),
    path ('loitosucc/',views.loitosucc,name='loitosucc'),
    # path('details',views.investment_details,name='details'),


    
]