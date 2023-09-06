from django.views.generic import ListView, CreateView
from .models import QuestionModel, QuizModel, AnswerModel, CategoryModel
from django.db.models import Prefetch
from .utils import reset_quiz_data
class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'categories'
    model = CategoryModel


class QuizView(ListView):
    template_name = 'quiz.html'
    model = QuestionModel
    context_object_name = 'questions'
  
    def get_queryset(self):

        reset_quiz_data(self, QuizModel)#reset the temporary quiz data

        queryset = super().get_queryset() 
        
        category = self.request.GET.get('category')# Get the selected category 

        # Category 0 represents all categories
        if category == "0":
            queryset = QuestionModel.objects.all().prefetch_related(
                Prefetch('answer_question', queryset=AnswerModel.objects.all().order_by('?')))
        else:
            queryset = QuestionModel.objects.filter(category=category).prefetch_related(
                Prefetch('answer_question', queryset=AnswerModel.objects.all().order_by('?')))
        
        # If an non-existent number was forced, get all questions
        if not queryset.exists():
             queryset = QuestionModel.objects.all().prefetch_related(
                Prefetch('answer_question', queryset=AnswerModel.objects.all().order_by('?')))

        return queryset[:30] # Limit to 30 questions
    


class ResultView(ListView):
    template_name = 'result.html'
    context_object_name = 'results'
    model = QuizModel

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)

        #Get the total number of questions answered correctly
        total_correct_answers = QuizModel.objects.filter(is_correct=True).count()  
        
        #Get the total number of questions
        total_questions = QuizModel.objects.all().count()

        #Get the total time taken to complete the quiz
        time = QuizModel.objects.last()
    
        #Create all context objects
        context['total_correct_answers'] = total_correct_answers
        context['score'] =  round((total_correct_answers / total_questions)*100,1)
        context['total_time'] = time.total_time
        
        return context


    