from rest_framework import viewsets, mixins, generics
from core.models import QuizModel, QuestionModel, AnswerModel
from .serializers import QuizSerializer, QuestionSerializer, AnswerSerializer
class QuizView(mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin,
                    mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = QuizModel.objects.all()
    serializer_class = QuizSerializer
 

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = QuestionModel.objects.all()
    serializer_class = QuestionSerializer

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = AnswerModel.objects.all()
    serializer_class = AnswerSerializer