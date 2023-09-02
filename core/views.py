from django.views.generic import ListView, CreateView
from .models import QuestionModel, QuizModel, AnswerModel
from django.db.models import Prefetch
from .utils import reset_quiz_data
class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'quiz'
    model = QuestionModel


class QuizView(ListView):
    template_name = 'quiz.html'
    model = QuestionModel
    context_object_name = 'questions'
  
    def get_queryset(self):

        reset_quiz_data(self, QuizModel)

        queryset = super().get_queryset()
        
        queryset = QuestionModel.objects.all().prefetch_related(
            Prefetch('answer_question', queryset=AnswerModel.objects.all().order_by('?'))
        )
        return queryset

class ResultView(ListView):
    template_name = 'result.html'
    context_object_name = 'results'
    model = QuizModel

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)

        total_correct_answers = QuizModel.objects.filter(is_correct=True).count()  
        total_questions = QuizModel.objects.all().count()
        time = QuizModel.objects.last()
    

        context['total_correct_answers'] = total_correct_answers
        context['score'] =  round((total_correct_answers / total_questions)*100,1)
        context['total_time'] = time.total_time
        return context


    