from django.urls import path
from . import views

app_name = 'legal'

urlpatterns = [
    path('terms/', views.terms_and_conditions, name='terms'),
    path('privacy/', views.privacy_policy, name='privacy'),
]
