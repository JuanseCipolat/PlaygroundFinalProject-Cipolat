from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comentario, Publicacion

class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['titulo', 'contenido', 'imagen']

    widgets = {
        'titulo': forms.TextInput(attrs={'class': 'form-control'}),
        'contenido': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        'imagen': forms.FileInput(attrs={'class': 'form-control'})
    }

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['texto'].label = 'Comentario'
