from rest_framework import routers
from .views import QuizViewSet, QuestionViewSet, AnswerViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'quiz', QuizViewSet, basename='quiz')
router.register(r'questions', QuestionViewSet, basename='questions')
router.register(r'answer', AnswerViewSet, basename='answers')

urlpatterns = [
    path('', include(router.urls)),
]