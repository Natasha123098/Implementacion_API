from rest_framework import serializers
from Doctores.models import Doctor, Experiencia, TurnoTrabajo, Lugar_Trabajo


class DoctorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Doctor
        fields = ['nombre', 'apellido','sexo', 'email', 'especialidad']

class ExperienciaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Experiencia
        fields = ['edad', 'años_experiencia']

class TurnoTrabajoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TurnoTrabajo
        fields = ['turno']

class Lugar_TrabajoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lugar_Trabajo
        fields = ['lugar']