from django.contrib.auth.views import LoginView, LogoutView
from blog.views import inicio, registro, detalle_publicacion, crear_post, acerca_de
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', include('blog.urls')),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', inicio, name='inicio'),
    path('registro/', registro, name='registro'),
    path('post/<int:pk>/', detalle_publicacion, name='detalle_publicacion'),
    path('crear_post/', crear_post, name='crear_post'),
    path('acerca_de/', acerca_de, name='acerca_de'),
]