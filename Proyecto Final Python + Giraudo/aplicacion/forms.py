from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#----------------------------------------------------------------------------------------------
class ConsultorioForm(forms.Form):    
    nombre = forms.CharField(max_length=50, required=True)
    direccion = forms.CharField(max_length=50, required=True)
    telefono = forms.IntegerField(required=True)
    email = forms.EmailField(required=True)
#----------------------------------------------------------------------------------------------    
class ProfesionalForm(forms.Form):    
    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    profesion = forms.CharField(max_length=50, required=True)
#----------------------------------------------------------------------------------------------        
class EspecialidadForm(forms.Form):    
    nombre = forms.CharField(max_length=50, required=True)
    consultorio = forms.CharField(max_length=50, required=True)
    telefono = forms.IntegerField(required=True)
#----------------------------------------------------------------------------------------------        
class PacienteForm(forms.Form):    
    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    dni = forms.IntegerField(required=True)
    telefono = forms.IntegerField(required=True)
    obrasocial = forms.CharField(max_length=50, required=True)
#----------------------------------------------------------------------------------------------  
class RegistroForm(UserCreationForm):
    email = forms.EmailField(max_length=50 , required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username' , 'email' , 'password1' , 'password2'] 
#----------------------------------------------------------------------------------------------  
class UserEditForm(UserCreationForm):
    email = forms.EmailField(max_length=50, required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Nombre/s", max_length=50, required=True)
    last_name = forms.CharField(label="Apellido/s", max_length=50, required=True)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']
#----------------------------------------------------------------------------------------------  
class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)
#----------------------------------------------------------------------------------------------  
  