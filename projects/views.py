from django.shortcuts import render
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
    context = {'form': form}
    return render(request, 'project_form.html', context)
