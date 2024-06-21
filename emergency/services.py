# tu_app/services.py

from .models import Usuario, Alerta

class QueryService:
    @staticmethod
    def get_usuario(correo, contrasena):
        try:
            # Filtramos por correo y contraseña
            usuario = Usuario.objects.get(correo=correo, contrasena=contrasena)
            return usuario
        except Usuario.DoesNotExist:
            return None

    @staticmethod
    def obt_correo_contra():
        return Usuario.objects.values('correo', 'contrasena')

    @staticmethod
    def obtener_alertas():
        return Alerta.objects.values('titulo', 'descripcion', 'imagen')
