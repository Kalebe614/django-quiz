from django.urls import path
from core import views
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('quiz/', views.QuizView.as_view(), name='quiz'),
    path('api/questions/', views.QuestionsView.as_view(), name='questions'),
    path('result/', views.ResultView.as_view(), name='resultQuiz'),
]
