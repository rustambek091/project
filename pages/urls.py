from django.urls import path 
from .views import * 

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('blog/', Blogs.as_view(), name='blog'),
    path('client/', Client.as_view(), name='client'),
    path('contact/', Contact.as_view(), name='contact'),
    path('services/', Services.as_view(), name='services'),
]