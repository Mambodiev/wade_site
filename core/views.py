from django.shortcuts import render
from django.views import generic
from .forms import ContactForm
from django.shortcuts import render, reverse
from django.views.generic import View, TemplateView
from django.contrib.auth.views import LoginView
from .models import Login, About, Signup


# Create your views here.
class ContactView(generic.FormView):
    form_class = ContactForm
    template_name = 'blog/contact.html'

    def get_success_url(self):
        return reverse("contact")



class BlogLoginView(LoginView):
    model = Login
    template_name = 'core/login.html'

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['login'] = Login.objects.all()
        return context



class BlogAboutView(TemplateView):
    model = About
    template_name = 'core/about.html'

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.all()
        return context



class BlogSignupView(LoginView):
    model = Signup
    template_name = 'core/signup.html'

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['signup'] = Signup.objects.all()
        return context



