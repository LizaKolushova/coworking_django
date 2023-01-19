from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('auth', views.auth, name='auth'),
    path('registration', views.registration, name='registration'),
    path('place', views.places, name='place'),
    path('place/<int:place_id>/', views.rate, name='rate'),
    path('about', views.about, name='about'),
]