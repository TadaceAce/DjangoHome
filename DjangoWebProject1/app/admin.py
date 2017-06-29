from django.contrib import admin

from .models import Question, Answer

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    fieldsets = [
        (None, {'fields':['question_text']}),        
    ]
    inlines = [AnswerInline]    
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
