from django.urls import path
from . import views

app_name = "holter"

urlpatterns = [
    path('', views.ProfileView.as_view(), name="profile_list"),
    
]
