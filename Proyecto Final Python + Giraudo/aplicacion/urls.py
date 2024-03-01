from django.urls import path, include
from .views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [    
    path('', home, name="1home"),
   
#------------------------------------------------------------------------------------------------------#
#                                              CONSULTORIOS                                            #
#------------------------------------------------------------------------------------------------------#
    path('consultorios/' , ConsultorioList.as_view() , name="consultorios"),
    path('consultorio_create/' , ConsultorioCreate.as_view() , name="consultorio_create"),
    path('consultorio_update/<int:pk>/' , ConsultorioUpdate.as_view() , name="consultorio_update"),
    path('consultorio_delete/<int:pk>/' , ConsultorioDelete.as_view() , name="consultorio_delete"),
#------------------------------------------------------------------------------------------------------#
#                                             ESPECIALIDADES                                           #
#------------------------------------------------------------------------------------------------------#
    path('especialidades/' , EspecialidadList.as_view() , name="especialidades"),
    path('especialidad_create/' , EspecialidadCreate.as_view() , name="especialidad_create"),
    path('especialidad_update/<int:pk>/' , EspecialidadUpdate.as_view() , name="especialidad_update"),
    path('especialidad_delete/<int:pk>/' , EspecialidadDelete.as_view() , name="especialidad_delete"),
#------------------------------------------------------------------------------------------------------#
#                                              PACIENTES                                               #
#------------------------------------------------------------------------------------------------------#
    path('pacientes/' , PacienteList.as_view() , name="pacientes"),
    path('paciente_create/' , PacienteCreate.as_view() , name="paciente_create"),
    path('paciente_update/<int:pk>/' , PacienteUpdate.as_view() , name="paciente_update"),
    path('paciente_delete/<int:pk>/' , PacienteDelete.as_view() , name="paciente_delete"),
#------------------------------------------------------------------------------------------------------#
#                                            PROFESIONALES                                             #
#------------------------------------------------------------------------------------------------------#
    path('profesionales/' , ProfesionalList.as_view() , name="profesionales"),
    path('profesional_create/' , ProfesionalCreate.as_view() , name="profesional_create"),
    path('profesional_update/<int:pk>/' , ProfesionalUpdate.as_view() , name="profesional_update"),
    path('profesional_delete/<int:pk>/' , ProfesionalDelete.as_view() , name="profesional_delete"),
#------------------------------------------------------------------------------------------------------#
#                                              BUSCAR                                                  #
#------------------------------------------------------------------------------------------------------#
    path('buscar/' , buscar , name="buscar"), 
    path('buscarConsultorio/' , buscarConsultorio , name="buscarConsultorio"),  
    path('buscarProfesional/' , buscarProfesional , name="buscarProfesional"),
    path('buscarEspecialidad/' , buscarEspecialidad , name="buscarEspecialidad"),
    path('buscarPaciente/' , buscarPaciente , name="buscarPaciente"),
#------------------------------------------------------------------------------------------------------#
#                                     LOGIN - LOGOUT - REGISTRACION                                    #
#------------------------------------------------------------------------------------------------------#
path('login/' , login_request , name="login"),
path('registro/' , register , name="registro"),
path('logout/' , logout_request , name="logout"),
#------------------------------------------------------------------------------------------------------#
#                                       EDITAR PERFIL DE USUARIO                                       #
#------------------------------------------------------------------------------------------------------#
path('editar_perfil/', editarPerfil, name="editar_perfil"),
path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),
#----------------------------------------------------------------------------------------------#
#                                          ACERCA DE MI                                        #
#----------------------------------------------------------------------------------------------#
path('acerca_de_mi/', acercademi, name="acerca_de_mi"),


]