from django.urls import path

from .views import HeroView, SingleHeroView

urlpatterns = [
    path('heroes/', HeroView.as_view(), name='hero_list'),
    path('heroes/<int:pk>/', SingleHeroView.as_view(), name='single_hero'),
]