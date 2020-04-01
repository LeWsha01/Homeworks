from rest_framework import response, status, viewsets
from rest_framework.decorators import api_view

from dashboard import models
from dashboard import serializers


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProjectSerializer
    queryset = models.Project.objects.all()


class IssueViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.IssueSerializer
    queryset = models.Issue.objects.all()
