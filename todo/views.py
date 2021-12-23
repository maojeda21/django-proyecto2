from django.shortcuts import render, redirect
from .forms import agregarTarea

tareas = ['aprender django', 'estudiar','trabajar']

def home(request):
    context = {'tareas':tareas}
    return render(request, "todo/home.html", context)

def add(request):
    if request.method == 'POST':
        formulario = agregarTarea(request.POST)
        if formulario.is_valid():
            tarea = formulario.cleaned_data['tarea']
            tareas.append(tarea)
            return redirect('home')
    else:
        formulario = agregarTarea()
    context =  {'formulario': formulario}
    return render(request, 'todo/add.html', context)

 