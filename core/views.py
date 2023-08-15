from django.views.generic import ListView
from .models import QuestionModel
from django.http import JsonResponse
import random

class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'quiz'
    model = QuestionModel

class QuizView(ListView):
    template_name = 'quiz.html'
    model = QuestionModel

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

    def render_to_response(self, context, **response_kwargs):
        questions = list(self.get_queryset())
        data = []

        random.shuffle(questions)

        for question in questions:
            answers = question.answers.all() 
            answers_data = []

            for answer in answers:
                answers_data.append({
                    "text": answer.text,
                    "is_correct": answer.is_correct
                })

            random.shuffle(answers_data)

            data.append({
                "category": question.category.name,
                "question": question.question,
                "question_type": question.question_type,
                "answers": answers_data
            })

        return JsonResponse(data, safe=False)