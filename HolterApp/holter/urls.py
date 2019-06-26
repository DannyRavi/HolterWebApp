from django.urls import path
from . import views

app_name = "holter"

urlpatterns = [
    path('', views.ProfileView.as_view(), name="profile_list"),
    path('<int:pk>/', views.ProfileDetail.as_view(), name="profile_retrive"),
    path('0813595858/', views.ProfileDetail.as_view(), name="profile_retrive"),
]
