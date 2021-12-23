from django import forms

# Formulario para agregar tareas
class agregarTarea(forms.Form):
    tarea = forms.CharField(label="Tarea:")
