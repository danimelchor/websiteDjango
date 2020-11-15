from django.urls import path
from .views import *

urlpatterns = [
    path('', ProjectsView.as_view(), name="projects")
]
