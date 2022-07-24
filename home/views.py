from django.shortcuts import get_object_or_404, render
from home.models import *
from django.http import HttpResponse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
# from django.core.mail import EmailMessage
from django.conf import settings



def home(request):
    
    if request.method == 'POST':
       name = request.POST.get('name')
       email = request.POST.get('email')
       subject = request.POST.get('subject')
       message = request.POST.get('message')
       contactform = ContactForm(name=name, email=email, subject=subject, message=message)
       contactform.save()
       
       messages.success(request,"Message sent successfully")
       print(name, email, subject, message)
       
       send_mail(f'email from {name}, {subject}', message,email,['mastergentility5@gmail.com'])
    #    print(name, email, subject, message)

       return HttpResponseRedirect('/')
           
    my_profile = Userprofile.objects.all()
    skills = Skill.objects.all()
    service = Services.objects.all()
    potfolio = Portfolios.objects.all()
    achievements = Achievements.objects.all()
    # contact_me = ContactMe.objects.get(id=1)
    
    context = {
        'my_profile':my_profile,
        'skills':skills,
        
        'service':service,
        'potfolio':potfolio,
        'achievements':achievements,
        # 'contact_me':contact_me,
        # 'contactform':form
     
    }

    return render(request,'home/index.html', context)

def portfolio_detail(request, id):
    details = get_object_or_404(Portfolios, pk=id)
    context = {
        'details':details
    }
    return render(request,'home/portfolio-details.html', context )
