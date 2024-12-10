from django.shortcuts import render
from .forms import ContactForm
from django.views.generic import View, TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from catalog.models import Category


User = get_user_model()


class IndexView(TemplateView):

    template_name = 'index.html'

index = IndexView.as_view()


def contact(request):

    import os
    success = False
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.send_mail()
        success = True
    context = {
        'form': form,
        'success': success,
        # testando variáveis de ambiente no Heroku
        # 'SECRET_KEY': os.getenv('SECRET_KEY'),
        # 'DEBUG': os.getenv('DEBUG')
    }
    return render(request, 'contact.html', context)


class RegisterView(CreateView):

    form_class = UserCreationForm
    template_name = 'register.html'
    model = User
    success_url = reverse_lazy('index')


register = RegisterView.as_view()
