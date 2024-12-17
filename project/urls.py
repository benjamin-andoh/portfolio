from django.urls import path
from .views import ProjectListCreate, ProjectListView

urlpatterns = [
    path('', ProjectListView.as_view(), name='project-list'),
]

