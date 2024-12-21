from django.urls import path
from .views import AboutView, HomePage, ProjectsView, ResumeView, download_resume

urlpatterns = [
    path('', HomePage.as_view(), name='homepage'),
    path('about/', AboutView.as_view(), name="about"),
    path('projects/', ProjectsView.as_view(), name='projects'),
    path('resume/', ResumeView.as_view(), name='resume'),
    path('resume/download/', download_resume, name='download_resume'),

]

