from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import *
from .forms import *

from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

#----------------------------------------------------------------------------------------------

def home(request):
    return render(request, "aplicacion/1home.html")

login_required
def consultorios(request):
    contexto = {'consultorios': Consultorio.objects.all()}
    return render(request, "aplicacion/consultorios.html", contexto)

login_required
def especialidades(request):
    contexto = {'especialidades': Especialidad.objects.all()}
    return render(request, "aplicacion/especialidades.html", contexto)

login_required
def profesionales(request):
    contexto = {'profesionales': Profesional.objects.all()}
    return render(request, "aplicacion/profesionales.html", contexto)

login_required
def pacientes(request):
    contexto = {'pacientes': Paciente.objects.all()}
    return render(request, "aplicacion/pacientes.html", contexto)

#----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------
login_required
def consultorioForm(request):
    if request.method == "POST":
        miForm = ConsultorioForm(request.POST)
        if miForm.is_valid():
            consultorio_nombre = miForm.cleaned_data.get("nombre")
            consultorio_direccion = miForm.cleaned_data.get("direccion")
            consultorio_telefono = miForm.cleaned_data.get("telefono")
            consultorio_email = miForm.cleaned_data.get("email")
            consultorio = Consultorio(nombre=consultorio_nombre , direccion=consultorio_direccion , telefono=consultorio_telefono , email=consultorio_email)
            consultorio.save()
            return redirect(reverse_lazy('consultorios'))
    else:
        miForm = ConsultorioForm()
    
    return render(request, "aplicacion/consultorioForm.html" , {"form": miForm })
#----------------------------------------------------------------------------------------------
login_required
def especialidadForm(request):
    if request.method == "POST":
        miForm = EspecialidadForm(request.POST)
        if miForm.is_valid():
            especialidad_nombre = miForm.cleaned_data.get("nombre")
            especialidad_consultorio = miForm.cleaned_data.get("consultorio")
            especialidad_telefono = miForm.cleaned_data.get("telefono")            
            especialidad = Especialidad(nombre=especialidad_nombre , consultorio=especialidad_consultorio , telefono=especialidad_telefono)
            especialidad.save()
            return redirect(reverse_lazy('especialidades'))
    else:
        miForm = EspecialidadForm()
    
    return render(request, "aplicacion/especialidadForm.html" , {"form": miForm })

#----------------------------------------------------------------------------------------------
login_required
def pacienteForm(request):
    if request.method == "POST":
        miForm = PacienteForm(request.POST)
        if miForm.is_valid():
            paciente_nombre = miForm.cleaned_data.get("nombre")
            paciente_apellido = miForm.cleaned_data.get("apellido")
            paciente_dni = miForm.cleaned_data.get("dni")
            paciente_telefono = miForm.cleaned_data.get("telefono")
            paciente_obrasocial = miForm.cleaned_data.get("obrasocial")            
            paciente = Paciente(nombre=paciente_nombre, apellido=paciente_apellido , dni=paciente_dni , telefono=paciente_telefono, obrasocial=paciente_obrasocial)
            paciente.save()
            return redirect(reverse_lazy('pacientes'))
    else:
        miForm = PacienteForm()
    
    return render(request, "aplicacion/pacienteForm.html" , {"form": miForm })

#----------------------------------------------------------------------------------------------
login_required
def profesionalForm(request):
    if request.method == "POST":
        miForm = ProfesionalForm(request.POST)
        if miForm.is_valid():
            profesional_nombre = miForm.cleaned_data.get("nombre")
            profesional_apellido = miForm.cleaned_data.get("apellido")
            profesional_profesion = miForm.cleaned_data.get("profesion")            
            profesional = Profesional(apellido=profesional_apellido , nombre=profesional_nombre , profesion=profesional_profesion)
            profesional.save()
            return redirect(reverse_lazy('profesionales'))
    else:
        miForm = ProfesionalForm()
    
    return render(request, "aplicacion/profesionalForm.html" , {"form": miForm })

#----------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------#
#                                       CONSULTORIOS                                           #
#----------------------------------------------------------------------------------------------#
class ConsultorioList(LoginRequiredMixin, ListView):
    model = Consultorio
#----------------------------------------------------------------------------------------------#
class ConsultorioCreate(LoginRequiredMixin, CreateView):
    model = Consultorio
    fields = ['nombre', 'direccion', 'telefono', 'email']
    success_url = reverse_lazy('consultorios')
#----------------------------------------------------------------------------------------------#
class ConsultorioUpdate(LoginRequiredMixin, UpdateView):
    model = Consultorio
    fields = ['nombre', 'direccion', 'telefono', 'email']
    success_url = reverse_lazy('consultorios')
#----------------------------------------------------------------------------------------------
class ConsultorioDelete(LoginRequiredMixin, DeleteView):
    model = Consultorio
    success_url = reverse_lazy('consultorios')
#----------------------------------------------------------------------------------------------#
#                                       ESPECIALIDADES                                         #
#----------------------------------------------------------------------------------------------#
class EspecialidadList(LoginRequiredMixin, ListView):
    model = Especialidad
#----------------------------------------------------------------------------------------------#
class EspecialidadCreate(LoginRequiredMixin, CreateView):
    model = Especialidad
    fields = ['nombre', 'consultorio', 'telefono']
    success_url = reverse_lazy('especialidades')
#----------------------------------------------------------------------------------------------#
class EspecialidadUpdate(LoginRequiredMixin, UpdateView):
    model = Especialidad
    fields = ['nombre', 'consultorio', 'telefono']
    success_url = reverse_lazy('especialidades')
#----------------------------------------------------------------------------------------------
class EspecialidadDelete(LoginRequiredMixin, DeleteView):
    model = Especialidad
    success_url = reverse_lazy('especialidades')
#----------------------------------------------------------------------------------------------#
#                                       PACIENTES                                              #
#----------------------------------------------------------------------------------------------#
class PacienteList(LoginRequiredMixin, ListView):
    model = Paciente
#----------------------------------------------------------------------------------------------
class PacienteCreate(LoginRequiredMixin, CreateView):
    model = Paciente
    fields = ['nombre', 'apellido', 'dni', 'telefono', 'obrasocial']
    success_url = reverse_lazy('pacientes')
#----------------------------------------------------------------------------------------------#
class PacienteUpdate(LoginRequiredMixin, UpdateView):
    model = Paciente
    fields = ['nombre', 'apellido', 'dni', 'telefono', 'obrasocial']
    success_url = reverse_lazy('pacientes')  
#----------------------------------------------------------------------------------------------
class PacienteDelete(LoginRequiredMixin, DeleteView):
    model = Paciente
    success_url = reverse_lazy('pacientes')  
#----------------------------------------------------------------------------------------------#
#                                       PROFESIONALES                                          #
#----------------------------------------------------------------------------------------------#
class ProfesionalList(LoginRequiredMixin, ListView):
    model = Profesional
#----------------------------------------------------------------------------------------------
class ProfesionalCreate(LoginRequiredMixin, CreateView):
    model = Profesional
    fields = ['nombre', 'apellido', 'profesion']
    success_url = reverse_lazy('profesionales')
#----------------------------------------------------------------------------------------------#
class ProfesionalUpdate(LoginRequiredMixin, UpdateView):
    model = Profesional
    fields = ['nombre', 'apellido', 'profesion']
    success_url = reverse_lazy('profesionales')
#----------------------------------------------------------------------------------------------
class ProfesionalDelete(LoginRequiredMixin, DeleteView):
    model = Profesional
    success_url = reverse_lazy('profesionales')
#----------------------------------------------------------------------------------------------#
#                                       BUSCAR                                                 #
#----------------------------------------------------------------------------------------------#
login_required
def buscar(request):
    return render(request, "aplicacion/buscar.html")

login_required
def buscarConsultorio(request):
    if request.GET["buscar"]: 
        patron = request.GET["buscar"]
        consultorios = Consultorio.objects.filter(nombre__icontains=patron) 
        contexto = {"consultorios": consultorios }
        return render(request, "aplicacion/consultorios.html" , contexto)
    return HttpResponse("No se ingresaron patrones de busqueda.")
#----------------------------------------------------------------------------------------------
login_required
def buscarEspecialidad(request):
    if request.GET["buscar"]: 
        patron = request.GET["buscar"]
        especialidades = Especialidad.objects.filter(nombre__icontains=patron) 
        contexto = {"especialidades": especialidades }
        return render(request, "aplicacion/especialidades.html" , contexto)
    return HttpResponse("No se ingresaron patrones de busqueda.")
#----------------------------------------------------------------------------------------------
login_required
def buscarPaciente(request):
    if request.GET["buscar"]: 
        patron = request.GET["buscar"]
        pacientes = Paciente.objects.filter(nombre__icontains=patron) 
        contexto = {"pacientes": pacientes }
        return render(request, "aplicacion/pacientes.html" , contexto)
    return HttpResponse("No se ingresaron patrones de busqueda.")
#----------------------------------------------------------------------------------------------
login_required
def buscarProfesional(request):
    if request.GET["buscar"]: 
        patron = request.GET["buscar"]
        profesionales = Profesional.objects.filter(nombre__icontains=patron) 
        contexto = {"profesionales": profesionales }
        return render(request, "aplicacion/profesionales.html" , contexto)
    return HttpResponse("No se ingresaron patrones de busqueda.")
#----------------------------------------------------------------------------------------------#
#                                        LOGIN                                                 #
#----------------------------------------------------------------------------------------------#
def login_request(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            password = miForm.cleaned_data.get("password")
            user = authenticate(username=usuario , password=password)
            if user is not None:
                login(request, user)
                
                
                try:
                    avatar = Avatar.objects.get(user=request.user.id).imagen.url
                except:
                    avatar = "/media/avatares/default1.png" 
                finally:
                    request.session["avatar"] = avatar

                
                return render(request, "aplicacion/1home.html")
            else:                
                return redirect(reverse_lazy('login'))
                
    else:
        miForm = AuthenticationForm()
    
    return render(request, "aplicacion/login.html", {'form': miForm})
#----------------------------------------------------------------------------------------------#
#                                        REGISTRO                                              #
#----------------------------------------------------------------------------------------------#
def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
                        
            miForm.save()
            messages.success(request, ("El usuario se creó correctamente."))
            return redirect(reverse_lazy('1home'))
    else:
        miForm = RegistroForm()
    
    return render(request, "aplicacion/registro.html" , {"form": miForm })
#----------------------------------------------------------------------------------------------#
#                                        LOGOUT                                                #
#----------------------------------------------------------------------------------------------#
def logout_request(request):
    logout(request)
    messages.success(request, ("Su sesión se cerró correctamente."))
    return redirect('1home')
#----------------------------------------------------------------------------------------------#
#                                EDITAR PERFIL DE USUARIO                                      #
#----------------------------------------------------------------------------------------------#
@login_required
def editarPerfil(request):
    usuario = request.user #request es una base de datos con toda la info que viaja de pestaña en pestaña y que podemos llamar la info que contenga y necesitemos de esta manera
    
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            user = User.objects.get(username=usuario)
            user.email = informacion['email']
            user.first_name = informacion['first_name']
            user.last_name = informacion['last_name']
            user.set_password(informacion['password1'])
            user.save()
            return render(request, "aplicacion/1home.html")
    else:    
        form = UserEditForm(instance=usuario)

    return render(request, "aplicacion/editarPerfil.html", {"form": form }) 
#----------------------------------------------------------------------------------------------#
#                                AVATAR DE PERFIL DE USUARIO                                   #
#----------------------------------------------------------------------------------------------#
@login_required
def agregarAvatar(request):       
        
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            usuario = User.objects.get(username=request.user)            
            
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            
            avatar = Avatar(user=usuario, imagen=form.cleaned_data['imagen'])
            avatar.save()
            
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session["avatar"] = imagen
            return render(request, "aplicacion/1home.html")
    else:    
        form = AvatarForm()

    return render(request, "aplicacion/agregarAvatar.html", {"form": form })  
#----------------------------------------------------------------------------------------------#
#                                          ACERCA DE MI                                        #
#----------------------------------------------------------------------------------------------#
@login_required
def acercademi(request):
    return render(request, "aplicacion/acercademi.html")