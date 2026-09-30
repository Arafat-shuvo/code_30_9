from django.urls import path
from app.views import *


urlpatterns = [
   
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('home/', home, name='home'),
    
]
