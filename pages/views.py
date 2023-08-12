from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView

from pages.models import Blog

# Create your views here.


class Home(TemplateView):
    template_name = 'index.html'

class About(TemplateView):
    template_name = 'about.html'

class Blogs(ListView):
    model = Blog
    template_name = 'blog.html'    

class Client(TemplateView):
    template_name = 'client.html'
   

class Contact(TemplateView):
    template_name = 'contact.html'

class Services(TemplateView):
    template_name = 'services.html'