from django.urls import path
from .views import AboutView, HomePage, ProjectsView

urlpatterns = [
    path('', HomePage.as_view(), name='homepage'),
    path('about/', AboutView.as_view(), name="about"),
    path('projects/', ProjectsView.as_view(), name='projects'),

]

