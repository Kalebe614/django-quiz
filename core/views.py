from django.db.models.query import QuerySet
from django.views.generic import ListView, CreateView
from .models import QuestionModel, QuizModel, AnswerModel
from django.db.models import Prefetch

class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'quiz'
    model = QuestionModel


class QuizView(ListView):
    template_name = 'quiz.html'
    model = QuestionModel
    context_object_name = 'questions'


    queryset = QuestionModel.objects.all().prefetch_related(
        Prefetch('answer_question', queryset=AnswerModel.objects.all().order_by('?'))
    )

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

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
       
        total_questions = QuizModel.objects.count()
        total_points = QuizModel.objects.filter(is_correct=True).count()

        context['total_questions']= total_questions
        context['total_points']= total_points
        context['score']= round(total_points*100/total_questions)

       
        return context
class CreateAnswerView(CreateView):
    model = QuizModel
    fields = ['question', 'answer', 'correct_answer', 'is_correct', 'category', 'total_time']
    