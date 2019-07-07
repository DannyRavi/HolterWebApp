from django.urls import path
from . import views

app_name = "doc"

urlpatterns = [
     path('docers/', views.DocView.as_view(), name="profile_list"),
    # path('<int:pk>/', views.DocDetail.as_view(), name="profile_retrive"),
    # path('0813595858/', views.DocDetail.as_view(), name="profile_retrive"),
]
