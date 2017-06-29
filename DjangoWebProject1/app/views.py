"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

from .models import Question

from django.views import generic

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )


class InterviewView(generic.ListView):
    model = Question
    template_name='app/interview_questions.html'

    def get_context_data(self, **kwargs):
        context = super(InterviewView, self).get_context_data(**kwargs)
        context['random_question_list'] = Question.objects.all().order_by('?')[:3]
        context['full_question_list'] = Question.objects.all()
        return context


class SingleQuestionView(generic.DetailView):
    model = Question
    template_name = 'app/single_question.html'

    def get_context_data(self, **kwargs):
        context = super(SingleQuestionView, self).get_context_data(**kwargs)
        context['all_questions'] = Question.objects.all()
        return context

