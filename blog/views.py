from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Publicacion, Comentario
from .forms import ComentarioForm, PublicacionForm, RegistroForm
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistroForm
from django.contrib import messages

def inicio(request):
    publicaciones = Publicacion.objects.all()
    return render(request, 'blog/inicio.html', {'publicaciones': publicaciones})

@login_required
def crear_post(request):
    if request.method == 'POST':
        form = PublicacionForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('detalle_publicacion', pk=post.pk)
    else:
        form = PublicacionForm()
    return render(request, 'blog/crear_post.html', {'form': form})

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario creado correctamente.')
            return redirect('inicio')  
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'Error en el campo {field}: {error}')
    else:
        form = RegistroForm()

    return render(request, 'blog/registro.html', {'form': form})

def detalle_publicacion(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    comentarios = Comentario.objects.filter(publicacion=publicacion)
    if request.method == 'POST':
        comentario_form = ComentarioForm(request.POST)
        if comentario_form.is_valid():
            comentario = comentario_form.save(commit=False)
            comentario.publicacion = publicacion
            comentario.save()
            return redirect('detalle_publicacion', pk=publicacion.pk)
    else:
        comentario_form = ComentarioForm()
    return render(request, 'blog/detalle_publicacion.html', {'publicacion': publicacion, 'comentarios': comentarios, 'comentario_form': comentario_form})

@login_required
def acerca_de(request):
    return render(request, 'blog/acerca_de.html')
