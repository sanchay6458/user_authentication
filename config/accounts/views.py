# from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm
from django.shortcuts import render
from django.http import HttpResponse
from .models import CustomUser

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def passwordchange(request):
    return render(request, 'registration/password_change_form.html')

def passwordreset(request):
    return render(request, 'registration/password_reset_form.html')

# def profile(request):
#     current_profile = request.user
#     currentuser_profile = CustomUser.objects.get(username=current_profile)
#     context = {
#         'profiles': currentuser_profile
#     }
#     return render(request, 'registration/login.html', context)
# Create your views here.
