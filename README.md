# PlaygroundFinalProject-Cipolat

Alumno: Juan Sebastian Cipolat

Proyecto final, curso Python CODERHOUSE Comisión 56060

Aplicacion tipo BLOG:

Este es un proyecto creado para crear posts, los usuarios que se registren pueden crear publicaciones de distinto tipo, subir una imagen al articulo creado y realizar comentarios en publicaciones de otros usuarios o en publicaciones propias. desde el panel de administrador podemos eliminar usuarios y tambien posts que no deseemos.


## Requisitos

Asegúrate de tener Python y Django instalados en tu sistema. Puedes instalar Django utilizando el siguiente comando:

pip install Django

## Configuración del Proyecto

Clona el repositorio:

git clone: https://github.com/obijuankanabi/PlaygroundFinalProject-Cipolat.git 

Navega al directorio del proyecto:

Crea un entorno virtual (opcional pero recomendado):

python -m venv venv

Activa el entorno virtual:

En Windows:
.\venv\Scripts\activate

En Linux/Mac:
source venv/bin/activate

Instala las dependencias del proyecto:

pip install -r requirements.txt

Aplica las migraciones de la base de datos:

python manage.py migrate

## Ejecución del Proyecto

Ejecuta el servidor de desarrollo:

python manage.py runserver

Abre tu navegador y visita http://127.0.0.1:8000/.
