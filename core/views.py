from django.shortcuts import render
from django.views.generic import ListView
from .models import QuestionModel
class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'quiz'
    model = QuestionModel