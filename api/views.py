from rest_framework import viewsets
from core.models import QuizModel, QuestionModel, AnswerModel
from .serializers import QuizSerializer, QuestionSerializer, AnswerSerializer

class QuizViewSet(viewsets.ModelViewSet):
    queryset = QuizModel.objects.all()
    serializer_class = QuizSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = QuestionModel.objects.all()
    serializer_class = QuestionSerializer

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = AnswerModel.objects.all()
    serializer_class = AnswerSerializer