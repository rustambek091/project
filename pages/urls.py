from django.urls import path 
from .views import * 

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('blog/', Blogs.as_view(), name='blog'),
    path('client/', Client.as_view(), name='client'),
    path('contact/', Contact.as_view(), name='contact'),
    path('services/', Services, name='services'),
    path('services/<int:pk>/', Services, name='services_detail'),
    ]