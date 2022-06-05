from django.shortcuts import render
from rest_framework import viewsets

from .models import Pledge
from .serializers import PledgeSerializers


class PledgeViewSet(viewsets.ModelViewSet):
    queryset = Pledge.objects.all()
    serializer_class = PledgeSerializers
