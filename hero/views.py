from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Hero
from .serializers import HeroSerializer


class HeroView(ListCreateAPIView):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer


class SingleHeroView(RetrieveUpdateDestroyAPIView):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer