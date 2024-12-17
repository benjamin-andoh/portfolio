from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import Project
from .serializers import ProjectSerializer
from django.views.generic import ListView
from .models import Project

class ProjectListCreate(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectListView(ListView):
    model = Project
    template_name = 'projects/project_list.html'  
    context_object_name = 'projects'
