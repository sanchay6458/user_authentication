from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView #new

# def homePageView(request):
#     return HttpResponse('Hello, World!')

# def djangoView(request):
#     return HttpResponse('Hello, Django!')

# def contactView(request):
#     return HttpResponse('This is coming from contact view')

# def about(request):
#     return HttpResponse('This is coming from about view')



# class HomePageView(TemplateView):
#     template_name = 'pages/home.html'  #new


def home(request):
    context = {
        'title': 'Hi I’m Bickky , FullStack Python Developer and Programming Instructor.',
    }
    return render(request, 'pages/home.html',context)

def about(request):
    return render(request, 'pages/about.html')    


# class ContactPageView(TemplateView):
#     template_name = 'pages/contact.html'  #new

# class AboutPageView(TemplateView):
#     template_name = 'pages/about.html'  #new

#aboutpage
#contactpage
#skillpage

# Create your views here.
