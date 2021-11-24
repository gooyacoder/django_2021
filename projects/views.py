from django.shortcuts import render, redirect
from .models import Project
from django.http import HttpResponse
from .forms import ProjectForm



def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})

def project(request, pk):
    result = Project.objects.get(id=pk)
    return render(request, 'single-project.html',
                  {'project': result})


def createProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, 'project_form.html', context)

def updateProject(request, pk):
    project = Project.objects.get(id=pk)

    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, 'project_form.html', context)

def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'project': project}
    return render(request, 'delete_object.html', context)