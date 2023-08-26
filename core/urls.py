from django.urls import path, include
from core import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('quiz/', views.QuizView.as_view(), name='quiz'),
    path('result/', views.ResultView.as_view(), name='resultQuiz'),
    path('api-auth/', include('rest_framework.urls')),
]
