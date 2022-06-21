from django.urls import path
from . import views
urlpatterns = [
    path('', views.landing,name="home"),
    path('login/', views.login_view,name="login_view"),
    path('register/', views.register_view,name="register_view"),
    path('adminpage/', views.admin,name="adminpage"),
    path('teacher/', views.teacher,name="teacher"),
    path('student/', views.student,name="student"),
]
