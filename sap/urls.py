"""
URL configuration for sap project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from Doctores.views import Nuevo_Doctor, Editar_Doctor, Eliminar_Doctor, Ver_Doctor, Registro_Doctor, DoctorViewSet, \
    ExperienciaViewSet, TurnoTrabajoViewSet, Lugar_TrabajoViewSet
#from quickstart import views
from webapp.views import mostrar_Doctores

router = routers.DefaultRouter()
router.register(r'doctor', DoctorViewSet)
router.register(r'experiencia', ExperienciaViewSet)
router.register(r'turnotrabajo', TurnoTrabajoViewSet)
router.register(r'lugartrabajo', Lugar_TrabajoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mostrar_Doctores, name= 'inicio'),
    path('Nuevo_Doctor/', Nuevo_Doctor),
    path('Editar_Doctor/<int:idDoctor>', Editar_Doctor),
    path('Ver_Doctor/<int:idDoctor>', Ver_Doctor),
    path('Eliminar_Doctor/<int:idDoctor>', Eliminar_Doctor),
    path('Registro_Doctor/', Registro_Doctor),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
