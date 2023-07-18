#from django.contrib.auth.models import Doctor
from django.shortcuts import render
from rest_framework import viewsets, permissions

from Doctores.models import Doctor
from quickstart.serializers import DoctorSerializer


# Create your views here.
class DoctorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Doctor.objects.all().order_by()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]
