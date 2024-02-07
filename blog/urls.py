from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import inicio, registro, detalle_publicacion, crear_post, acerca_de

app_name = 'blog'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='blog:inicio'), name='logout'),
    path('registro/', registro, name='registro'),
    path('post/<int:pk>/', detalle_publicacion, name='detalle_publicacion'),
    path('crear_post/', crear_post, name='crear_post'),
    path('acerca_de/', acerca_de, name='acerca_de'),
    path('', inicio, name='inicio'),
]