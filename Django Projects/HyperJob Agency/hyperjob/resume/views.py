from django.shortcuts import render
from django.views import View
from .models import Resume
from django.http import HttpResponseRedirect, HttpResponseForbidden

class ResumesView(View):
    def get(self, request):
        resume = Resume.objects.all()
        return render(request,"resume/resumes.html", {'resumes': resume})

class NewResumeView(View):
    def post(self, request):
        data = request.POST.get('description')
        if request.user.is_staff:
            return HttpResponseForbidden()
        elif request.user.is_authenticated:
            Resume.objects.create(description=data, author=request.user)
        else:
            return HttpResponseForbidden()
        return HttpResponseRedirect('/home')