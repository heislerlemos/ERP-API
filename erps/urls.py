from django.urls import path
from . import views

urlpatterns = [
    path('', views.erps, name="erps")
]
