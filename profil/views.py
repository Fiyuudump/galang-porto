from django.shortcuts import render
from profil.models import About, Resume, Service, Skill, Blog, Contact

def home(request):
    abouts = About.objects.first()
    resumes = Resume.objects.all()
    services = Service.objects.all()
    skills = Skill.objects.all()
    blogs = Blog.objects.all()
    contacts = Contact.objects.all()

    context = {
        'abouts': abouts,
        'resumes': resumes,
        'services': services,
        'skills': skills,
        'blogs': blogs,
        'contacts': contacts,
    }

    return render(request, 'index.html', context)

def single(request):
    return render(request, 'single.html')
