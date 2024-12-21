from django.views.generic import TemplateView, ListView
from django.http import FileResponse
import os
from django.conf import settings



class HomePage(TemplateView):
    template_name = 'projects/homepage.html'


class AboutView(TemplateView):
    template_name = "projects/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "About Me"
        context["description"] = "I am a professional software developer with expertise in Django, React, and more."
        context["skills"] = [
            "Django",
            "React.js",
            "Redux",
            "PostgreSQL",
            "Docker",
            "AWS",
            "Next.js"
        ]
        return context




class ResumeView(TemplateView):
    template_name = 'projects/resume.html'

def download_resume(request):
    # Use the actual path to your resume file
    file_path = os.path.join(settings.BASE_DIR, 'static', 'resume', 'resume.pdf')
    try:
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='Benjamin_Andoh_Resume.pdf')
    except FileNotFoundError:
        return HttpResponseNotFound("The requested file was not found.")


class ProjectsView(TemplateView):
    template_name = 'projects/projects.html'

    def get_context_data(self, **kwargs):
        # Adding mock project data based on resume
        context = super().get_context_data(**kwargs)
        context['projects'] = [
            {
                'title': 'Inventory Management System - Reboot Canada',
                'description': (
                    'Designed and implemented an inventory management system using Django, '
                    'enhancing operational efficiency with real-time inventory updates and '
                    'advanced search capabilities.'
                )
            },
            {
                'title': 'Shift Tracking System - MeshLabs',
                'description': (
                    'Developed a robust shift-tracking system using SpringBoot, enabling real-time '
                    'notifications and improving HR and finance operations by 40%.'
                )
            },
            {
                'title': 'Document Management System - AmaliTech',
                'description': (
                    'Architected and managed a scalable Document Management System leveraging AWS services '
                    'such as EC2, S3, and CloudFormation, reducing manual provisioning errors by 90%.'
                )
            },
            {
                'title': 'Real-Time Chat Application - AITI-KACE',
                'description': (
                    'Developed and deployed a real-time chat application using Laravel and WebSocket technologies, '
                    'enabling seamless customer communication and increasing customer support efficiency by 40%.'
                )
            },
            {
                'title': 'E-Commerce Analytics Dashboard',
                'description': (
                    'Built an interactive analytics dashboard for an e-commerce platform, utilizing Vue.js and Flask to provide '
                    'real-time insights into sales trends, customer behavior, and inventory status.'
                )
            },
            {
                'title': 'Automated Code Quality Monitoring System',
                'description': (
                    'Created an automated code quality monitoring system using Jenkins and SonarQube, achieving 95% code coverage '
                    'and improving team productivity by 30%.'
                )
            },
        ]
        return context




