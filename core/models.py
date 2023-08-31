from django.db import models

LEVEL_CHOICE = [(1,'Easy'),
                (2,'Medium'),
                (3,'Hard'),]
QUESTION_TYPE =[
            ('MCQ', 'Multiple Choice Question'),
            ('TF', 'True/False Question'),
]
class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class CategoryModel(BaseModel):
    name = models.CharField(max_length=100, null=False, blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'

    def __str__(self):
        return self.name
    

class QuestionModel(BaseModel):
    category = models.ForeignKey(CategoryModel, related_name='question_category', on_delete=models.CASCADE)
    level_choice = models.IntegerField('Level Choice', choices=LEVEL_CHOICE, null=False, blank=False)
    question_type = models.CharField('Question Type', max_length=3, choices=QUESTION_TYPE, null=False, blank=False)
    question = models.CharField('Question',max_length=255, null=False, blank=False)
    
    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

    def __str__(self):
        return self.question

class AnswerModel(BaseModel):
    question = models.ForeignKey(QuestionModel, related_name='answer_question', on_delete=models.CASCADE)
    text = models.CharField('Text Answer', max_length=255)
    is_correct = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'

    def __str__(self):
        return self.text

class QuizModel(models.Model):
    title = models.CharField('Title', max_length=255, default='Quiz Temporary')
    question = models.ForeignKey(QuestionModel, related_name='quiz_question', on_delete=models.CASCADE)
    answer = models.CharField('Answer User', max_length=255)
    correct_answer = models.ForeignKey(AnswerModel, related_name='quiz_answer', default=1, on_delete=models.CASCADE)
    category = models.ForeignKey(CategoryModel, related_name='quiz_category', on_delete=models.CASCADE)
    total_time = models.TimeField(blank=True, null=True)
    is_correct = models.BooleanField(default=False)
    class Meta:
        verbose_name = 'Quiz'
        verbose_name_plural='Quizzes'
    
    def __str__(self):
        return self.title

    #Set correct answer, category and is_correct based on question
    def save(self, *args, **kwargs):
    
        self.correct_answer = AnswerModel.objects.get(question=self.question, is_correct=True)
    
        self.category = self.question.category


        if (self.answer == str(self.correct_answer)):
            self.is_correct = True
        else:
            self.is_correct = False

        super().save(*args, **kwargs)
