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
    category = models.ForeignKey(CategoryModel, related_name='questions', on_delete=models.CASCADE)
    level_choice = models.IntegerField('Level Choice', choices=LEVEL_CHOICE, null=False, blank=False)
    question_type = models.CharField('Question Type', max_length=3, choices=QUESTION_TYPE, null=False, blank=False)
    question = models.CharField('Question',max_length=255, null=False, blank=False)
    
    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

    def __str__(self):
        return self.question

class AnswerModel(BaseModel):
    question = models.ForeignKey(QuestionModel, related_name='answers', on_delete=models.CASCADE)
    text = models.CharField('Text Answer', max_length=255)
    is_correct = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'


    def __str__(self):
        return self.text

        
