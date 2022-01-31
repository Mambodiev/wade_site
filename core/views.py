from django.shortcuts import render
from django.views import generic
from .forms import ContactForm
from django.shortcuts import render, reverse




# Create your views here.
class ContactView(generic.FormView):
    form_class = ContactForm
    template_name = 'blog/contact.html'

    def get_success_url(self):
        return reverse("contact")