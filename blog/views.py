from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from .models import Publicacion, Comentario
from .forms import ComentarioForm, PublicacionForm, RegistroForm
from django.contrib.auth.forms import AuthenticationForm

def inicio(request):
    publicaciones = Publicacion.objects.all().order_by('-fecha_creacion')
    comentarios = Comentario.objects.all()
    return render(request, 'blog/inicio.html', {'publicaciones': publicaciones, 'comentarios': comentarios})

@login_required(login_url='login')
def crear_post(request):
    if request.method == 'POST':
        form = PublicacionForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('detalle_publicacion', pk=post.pk)
    else:
        form = PublicacionForm()
    return render(request, 'blog/crear_post.html', {'form': form})

def registro(request):
    if request.user.is_authenticated:
        messages.warning(request, 'Ya estás autenticado. No puedes crear otra cuenta.')
        return redirect('inicio')

    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario creado correctamente. Inicia sesión para continuar.')
            return redirect('inicio')  
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'Error en el campo {field}: {error}')
    else:
        form = RegistroForm()

    return render(request, 'blog/registro.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión cerrada exitosamente.')
    return redirect('inicio')

@login_required
def detalle_publicacion(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    comentarios = Comentario.objects.filter(publicacion=publicacion)

    if request.method == 'POST':
        comentario_form = ComentarioForm(request.POST)
        if comentario_form.is_valid():
            comentario = comentario_form.save(commit=False)
            comentario.publicacion = publicacion
            comentario.autor = request.user  
            comentario.save()
            return redirect('detalle_publicacion', pk=publicacion.pk)

    else:
        comentario_form = ComentarioForm()

    return render(request, 'blog/detalle_publicacion.html', {'publicacion': publicacion, 'comentarios': comentarios, 'comentario_form': comentario_form})

def acerca_de(request):
    return render(request, 'blog/acerca_de.html')
