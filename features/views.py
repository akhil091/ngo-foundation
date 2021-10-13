from django.shortcuts import render, get_object_or_404
from datetime import datetime
from .models import *
from django import forms
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    today = datetime.today()
    volunteers = Volunteer.objects.all()
    causes = Cause.objects.all()
    blogs = Blog.objects.all()
    upevent = events.objects.filter(eventdate__gte=today)
    context = {
        "volunteers":volunteers,
        "causes":causes,
        "blogs":blogs,
        'upevent':upevent
    }
    return render(request,"index.html",context)

def volunteer(request):
    obj = Volunteer.objects.all()

    context = {
        "obj":obj,
    }
    return render(request,"volunteer.html",context)

def about(request):
    return render(request,"about.html")

def causes(request):
    objlist = Cause.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(objlist, 6)
    try:
        obj = paginator.page(page)
    except PageNotAnInteger:
        obj = paginator.page(1)
    except EmptyPage:
        obj = paginator.page(paginator.num_pages)
    context = {
        "obj":obj,
    }
    return render(request,"causes.html",context)

def causes_detail(request,*args, **kwargs):
    obj_list = Cause.objects.all()
    blog_obj = get_object_or_404(Cause,pk=kwargs.get("pk"))
    context = {
        'obj' : blog_obj,
        'causes': obj_list,
    }
    return render(request,"causes_detail.html",context)

def blog(request):
    obj_list = Blog.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(obj_list, 8)
    try:
        obj = paginator.page(page)
    except PageNotAnInteger:
        obj = paginator.page(1)
    except EmptyPage:
        obj = paginator.page(paginator.num_pages)
    context = {
        "obj":obj,
    }
    return render(request,"blog.html",context)

def blog_detail(request,*args, **kwargs):
    obj_list = Blog.objects.all()
    blog_obj = get_object_or_404(Blog,pk=kwargs.get("pk"))
    context = {
        'obj' : blog_obj,
        'blogs': obj_list,
    }
    return render(request,"blog_detail.html",context)

def contact(request):
    return render(request,"contact.html")

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['name','email','subject','message']


def contacts(request):
    thanks = False
    if request.method=="POST":
        thanks = False
        contactform = ContactForm(request.POST,None)
        if contactform.is_valid():
            name = contactform.cleaned_data.get('name')
            email = contactform.cleaned_data.get('email')
            subject = contactform.cleaned_data.get('subject')
            message = contactform.cleaned_data.get('message')

            contact = Contact(name=name, email=email, subject=subject, message=message)
            contact.save()
            thanks = True
            return render(request, 'contact.html', {'thanks': thanks})
        else:
            thanks = False
            return render(request, 'contact.html', {'thanks': thanks})

    return render(request, 'contact.html', {'thanks': thanks})

def pics(request):
    photo = gallery.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(photo, 8)
    try:
        obj = paginator.page(page)
    except PageNotAnInteger:
        obj = paginator.page(1)
    except EmptyPage:
        obj = paginator.page(paginator.num_pages)
    context = {
        "obj":obj,
    }
    return render(request, 'gallery.html', context)

def event(request):
    today = datetime.today()
    pastevent = events.objects.filter(eventdate__lt=today)
    upevent = events.objects.filter(eventdate__gte=today)
    context = { 'upevent': upevent,
               'pastevent':pastevent}
    return render(request, 'events.html', context)

def events_detail(request,*args, **kwargs):
    obj_list = events.objects.all()
    blog_obj = get_object_or_404(events,pk=kwargs.get("pk"))
    context = {
        'obj' : blog_obj,
        'events': obj_list,
    }
    return render(request,"events_detail.html",context)