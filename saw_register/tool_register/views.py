from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from .models import *
from django.views import generic
from django import forms
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class WorkPlaceView(ListView):
    model = WorkPlace
    template_name = "pages/home.html"

class SawBrandView(ListView):
    model = SawBrand
    template_name = "pages/saw_brands.html"

    def get(self, request, *args, **kwargs):
        workplace_id = kwargs['pk']
        saw_brands = SawBrand.objects.filter(workplace=workplace_id)

        return render(request, 'pages/saw_brands.html', context={'object_list': saw_brands})

class SawView(ListView):
    model = Saw
    template_name = "pages/meters.html"

    def get(self, request, *args, **kwargs):
        saw_id = kwargs['pk']
        saws = Saw.objects.filter(saw_brand=saw_id)


        return render(request, 'pages/saw.html', context={'object_list': saws})    
    
class MetersView(ListView):
    model = Meter
    template_name = "pages/meters.html"

    def get(self, request, *args, **kwargs):
        meter_id = kwargs['pk']
        meters = Meter.objects.filter(saw=meter_id)
        saw = Saw.objects.get(pk=meter_id)
        


        return render(request, 'pages/meters.html', context={'object_list': meters, 'saw': saw} ) 
    

class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','email','password1','password2']

    #perrašom init metoda, kad neliktu pagalbinio teksto (help text)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        self.fields['username'].help_text = None    


def sign_up(request):
    form = RegisterForm()
    if request.method == 'GET':

        return render(request, 'registration/signup.html', { 'form': form})

    if request.method == 'POST':
        # trūksta firstname, lastname laukeliu formoje, duombazėje yra, galimybė pridėti
        username = request.POST.get('username')
        password = request.POST.get('password1')
        email = request.POST.get('email')
        password2 = request.POST.get('password2')

        #tikriname ar useris neegzistuoja
        if User.objects.filter(username=username).exists():
            err_message = {
                'err_message': 'user already exist, choose different username',
                'form': form
                }

            return render(request, 'registration/signup.html', context=err_message)

        if User.objects.filter(email=email).exists():
            err_message = {
                'err_message': 'email already exist, choose different email',
                'form': form
                }

            return render(request, 'registration/signup.html', context=err_message)
        
        if password != password2:
            err_message = {
                'err_message': 'passwords did not match, please check your password input',
                'form': form
            }

            return render(request, 'registration/signup.html', context=err_message)

        
        #sukuriame useri
        new_user = User(username=username, password=password, email=email)
        new_user.save()

        return render(request, 'pages/home.html')      