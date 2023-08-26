from typing import Any, Dict
from django.views.generic import ListView
from .models import QuestionModel, QuizModel
from django.db.models import Sum
from django.http import HttpRequest, HttpResponse, JsonResponse
import random

class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'quiz'
    model = QuestionModel

class QuizView(ListView):
    template_name = 'quiz.html'
    model = QuestionModel
    paginate_by = 1
    
class QuestionsView(ListView):
    template_name = 'questions.html'
    context_object_name = 'questions'
    queryset = QuestionModel.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        
        category_filter = self.request.GET.get('category')

        if category_filter:
            queryset = queryset.filter(category__name=category_filter)
        
        return queryset


class ResultView(ListView):
    template_name = 'result.html'
    context_object_name = 'results'
    model = QuizModel

    def get_context_data(self, **kwargs: Any):
        context= super().get_context_data(**kwargs)
       
        total_questions = QuizModel.objects.count()
        total_points = QuizModel.objects.filter(is_correct=True).count()

        context['total_questions']= total_questions
        context['total_points']= total_points
        context['score']= round(total_points*100/total_questions)

       
        return context