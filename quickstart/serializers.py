#from django.contrib.auth.models import Doctor
from rest_framework import serializers
from Doctores.models import Doctor


class DoctorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Doctor
        fields = ['url', 'nombre', 'apellido', 'email', 'especialidad']