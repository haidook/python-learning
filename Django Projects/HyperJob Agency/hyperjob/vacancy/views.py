from django.shortcuts import render
from django.views import View
from .models import Vacancy
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.contrib.auth.models import User
from .forms import NewForm
from django.http import HttpResponseRedirect, HttpResponseForbidden


# Create your views here.
class HomeView(View):
    def get(self, request):
        return render(request, 'vacancy/menu.html')

class VacanciesView(View):
    def get(self, request):
        vacancies = Vacancy.objects.all()
        return render(request,"vacancy/vacancies.html", context={'vacancies': vacancies})

class MySignupView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'vacancy/signup.html'

class MyLoginView(LoginView):
    form_class = AuthenticationForm
    redirect_authenticated_user = True
    template_name = 'vacancy/login.html'

class MyProfileView(View):
    def get(self, request):
        template_name = 'vacancy/profile.html'
        form = NewForm()
        return render(request, template_name, context={'form': form})

class NewVacancyView(View):
    def post(self, request):
        data = request.POST.get('description')
        if request.user.is_staff:
            Vacancy.objects.create(description=data, author=request.user)
        elif request.user.is_authenticated:
            return HttpResponseForbidden()
        else:
            return HttpResponseForbidden()
        return HttpResponseRedirect('/home')
