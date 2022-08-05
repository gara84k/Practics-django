from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
def list_tasks(request):
    tasks = Task.objects.all()
    return render(request, "list_tasks.html", {"tasks": tasks})


def create_task(request):
    new_tipo = request.POST["tipo"]
    new_title = request.POST["title"]
    new_description = request.POST["description"]
    if new_tipo == "" or new_title == "" or new_description == "":
        tasks = Task.objects.all()
        return render(
            request, "list_tasks.html", {"tasks": tasks, "error": "All fields are required"}
        )
    task = Task(tipo = new_tipo,title=new_title, description=new_description)
    task.save()
    return redirect("/tasks/")


def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect("/tasks/")