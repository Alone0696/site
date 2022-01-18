from django.urls import path
from .views import *
urlpatterns = [
    #path('',login,name = 'login'),
    path('registration',Register.as_view(),name = 'reg'),
    path('',main_page,name = 'main_page'),
    path('logining',Login.as_view(),name = 'login'),
    path('logout',logout_user,name = 'logout'),
]