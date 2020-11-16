from django.shortcuts import render
from django.views.generic import View

from django.http import JsonResponse

from .models import Project

class ProjectsView(View):
    def get(self, request):
        context = {
            'projects': list(Project.objects.values())
        }

        if request.is_ajax():
            return JsonResponse(context, status=200)

        return render(request, 'projects.html')
