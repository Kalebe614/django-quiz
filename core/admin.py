from django.contrib import admin
from .models import *
@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    readonly_fields = ('created', 'updated')

class AnswerAdmin(admin.StackedInline):
    model = AnswerModel
    readonly_fields = ('created', 'updated')
    extra = 4
class QuestionAdmin(admin.ModelAdmin):
     inlines = [AnswerAdmin]
     readonly_fields = ('created', 'updated')
@admin.register(QuizModel)
class QuizModelAdmin(admin.ModelAdmin):
    list_display = ['title','question','answer','correct_answer','is_correct','category', 'total_time']
    readonly_fields = ['category', 'correct_answer', 'title']

admin.site.register(QuestionModel, QuestionAdmin)
admin.site.register(AnswerModel)