from django.shortcuts import render
from django.views.generic import CreateView
from .models import Contact
from .forms import ContactForm

# Create your views here.
class ContactView(CreateView):
    form_class = ContactForm
    model = Contact
    queryset = Contact.objects.all()
    success_url = '/'
    template_name = 'contact.html'
