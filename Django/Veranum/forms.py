from django import forms
from .models import ReservaHora, Habitacion

class ReservaHoraForm(forms.ModelForm):
    class Meta:
        model = ReservaHora
        fields = ['cliente', 'servicio', 'fecha', 'hora']

class HabitacionForm(forms.ModelForm):
    class Meta:
        model = Habitacion
        fields = ['nombre', 'descripcion', 'precio', 'disponible']



