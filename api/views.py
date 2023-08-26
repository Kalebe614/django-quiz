from rest_framework import viewsets
from core.models import QuizModel
from .serializers import QuizSerializer

class QuizViewSet(viewsets.ModelViewSet):
    queryset = QuizModel.objects.all()
    serializer_class = QuizSerializer