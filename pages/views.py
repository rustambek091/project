from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView

from .models import * 

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

def Services(request):
    servis = Service.objects.all()
    context = {
        'servis':servis
    }
    return render(request,'services.html', context)

class Service_Detail(DetailView):
    model = Service
    template_name = "detail_servise.html"
    