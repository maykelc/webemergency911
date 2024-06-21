from django.db import models

# Create your models here.
# Modelo de Usuario
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        verbose_name_plural = "Usuarios"
        
        
        
# Modelo de Alerta
class Alerta(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='imagenes_alertas', blank=True, null=True)

    def __str__(self):
        return self.titulo
        