from django import forms
from apps.mascotas.models import Mascota

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota

        fields=[
            'nombre',
            'raza',
            'sexo',
            'edad',
            'fecha_rescue',
            'persona',
            'vacuna',
        ]
        labels={
            'nombre' : 'Nombre',
            'raza' : 'Raza',
            'sexo' : 'Sexo del Animal',
            'edad' : 'Edad del animal',
            'fecha_rescue' : 'Fecha de rescate',
            'persona' : 'Adoptante',
            'vacuna' : 'Vacunas',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'raza': forms.TextInput(attrs={'class': 'form-control'}),
            'sexo': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_rescue':forms.TextInput(attrs={'class': 'form-control'}),
            'persona': forms.Select(attrs={'class': 'form-control'}),
            'vacuna': forms.CheckboxSelectMultiple(),
        }