# DjangoCrud

Pasos: EJECUTAR Proyecto

VERSIÓN PYTHON: 3.10.2
VERSIÓN DJANGO: 3.2.8

1. Crear base de datos en MySQL. Puede ser con phpmyadmin y el nombre creado se debe configurar en settings.py
2. Se deben tener instalados, con el comando pip install se pueden instalar (ej: pip install PyMySQL) :
        * PyMySQL: Para conectarse a una base de datos MySQL desde Django
        * Pillow: Manejo de imagenes 
        * django-cleanup: Para eliminar las imagenes en la carpeta "imagenes del proyecto" al momento de eliminar un registro
3. Validar url (ej: C:\Users\Desktop\Crud Django\sistema>) y Ejecutar comando python manage.py makemigrations
4. Validar url (ej: C:\Users\Desktop\Crud Django\sistema>) y Ejecutar comando python manage.py migrate

Con esto se debió crear en la base de datos las tablas de Django y lo que está en el modelo (Crud Django\sistema\libreria\models.py)

5. Ejecturar comando python manage.py runserver para ejecutar proyecto
6. Ejecutar comando python manage.py createsuperuser en caso tal de necesitar acceder a consola de admin de Django
