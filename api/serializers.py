from rest_framework import serializers
from core.models import QuizModel, AnswerModel, QuestionModel, CategoryModel

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionModel
        fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerModel
        fields = '__all__'

class QuizSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuizModel
        fields = ['question', 'answer', 'total_time']
