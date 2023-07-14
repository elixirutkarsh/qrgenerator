from django.urls import path
from . import views

urlpatterns = [
    path('genera/', views.generate_qr, name='generate_qr'),
]
