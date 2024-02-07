from django.contrib.auth.views import LoginView, LogoutView
from blog.views import inicio, registro, detalle_publicacion, crear_post, acerca_de
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registro/', registro, name='registro'),
    path('post/<int:pk>/', detalle_publicacion, name='detalle_publicacion'),
    path('crear_post/', crear_post, name='crear_post'),
    path('acerca_de/', acerca_de, name='acerca_de'),
    path('blog/', include('blog.urls', namespace='blog')),  
    path('', inicio, name='inicio'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)