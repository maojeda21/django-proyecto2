from django.shortcuts import render

tareas = ['aprender django', 'estudiar','trabajar']

def home(request):
    context = {'tareas':tareas}
    return render(request, "todo/home.html", context)

def add(request):
    return render(request, 'todo/add.html')

