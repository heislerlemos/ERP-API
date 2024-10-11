from django.urls import path
from . import views

urlpatterns = [
    path('erps/', views.erps, name="erps")
]
