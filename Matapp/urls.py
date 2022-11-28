from django.urls import path
from Matapp import views

urlpatterns = [
    path('transpose', views.main),
]