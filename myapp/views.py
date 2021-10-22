from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
                                    
from myapp.models import Home
from myapp.models import Personal_Information
from myapp.models import Skill
from myapp.models import Interest
from myapp.models import Testimonials
from myapp.models import Profile
from myapp.models import Education
from myapp.models import Career
from myapp.models import Category
from myapp.models import Project
from myapp.models import Temp


# Create your views here.

def index(request):
    
    home = Home.objects.all()
    personal_information = Personal_Information.objects.all()
    skill = Skill.objects.all()
    interest = Interest.objects.all()
    testimonial = Testimonials.objects.all()
    profile = Profile.objects.all()
    education = Education.objects.all()
    career = Career.objects.all()
    project = Project.objects.all()
    category = Category.objects.all()
    
    context = {'home':home, 'personal_information':personal_information, 'skill':skill, 'interest':interest, 'testimonial':testimonial,'profile':profile,'education':education,'career':career,'category':category,'project':project}
    
    return render(request, 'index.html', context)
    
def work_details(request):
    
    name=request.POST['name']
    temp=Temp(id=1,Name=name)
    temp.save()
    
    project = Project.objects.all()
    temp1 = Temp.objects.all()
    
    context = {'project':project, 'temp1':temp1}
    return render(request, 'work_details.html', context)


