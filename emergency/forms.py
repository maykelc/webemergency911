from django import forms
from .models import Usuario, Alerta

class UsuarioForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'correo', 'contrasena']
        widgets = {
            'contrasena': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("contrasena")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Las contraseñas no coinciden")

        return cleaned_data
    

class AlertaForm(forms.ModelForm):
    class Meta:
        model = Alerta
        fields = ['titulo', 'descripcion', 'imagen']