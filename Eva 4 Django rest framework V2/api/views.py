from rest_framework import viewsets
from .serializer import programadorSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Programador

# Create your views here.

class ProgramadoresViewSets(viewsets.ModelViewSet):
    queryset = Programador.objects.all()
    serializer_class = programadorSerializer
    permission_classes = [IsAuthenticated]
    