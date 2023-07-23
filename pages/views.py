from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView

# Create your views here.


class Home(TemplateView):
    template_name = 'index.html'

class About(TemplateView):
    template_name = 'about.html'

class Blog(TemplateView):
    template_name = 'blog.html'    

class Client(TemplateView):
    template_name = 'client.html'
   

class Contact(TemplateView):
    template_name = 'contact.html'

class Services(TemplateView):
    template_name = 'services.html'