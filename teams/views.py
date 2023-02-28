from django.shortcuts import render
from .models import Team
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import TeamSerializer
# Create your views here.

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [permissions.AllowAny]