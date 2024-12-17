from django.urls import path
from .views import ProjectListCreate, ProjectListView

urlpatterns = [
    path('api/projects/', ProjectListCreate.as_view(), name='project-list-create'),
    path('projects/', ProjectListView.as_view(), name='project-list'),
]

