from django.urls import path
from .views import add_student, dashboard, home, login_view, register

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('add-student/', add_student, name='add_student'),
]
