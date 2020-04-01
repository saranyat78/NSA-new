from rest_framework import viewsets
from .models import Tech, Tech1
from .serializer import TechSerializer, TechSerializer1
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import status


class TechViewSet(viewsets.ModelViewSet):
    queryset = Tech.objects.all()
    serializer_class = TechSerializer


class TechViewSet1(viewsets.ModelViewSet):
    queryset = Tech1.objects.all()
    serializer_class = TechSerializer1
