"""
Definition of urls for DjangoWebProject1.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views




from django.contrib import admin
admin.autodiscover()


urlpatterns = [
    # Examples:
    url(r'^$', app.views.home),
    url(r'^admin/', admin.site.urls),

    url(r'^interview_questions/$', app.views.InterviewView.as_view(), name='interview_questions'),

    url(r'^(?P<pk>[0-9]+)/$', app.views.SingleQuestionView.as_view(), name='detail'),      
    
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),

    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

  
]
