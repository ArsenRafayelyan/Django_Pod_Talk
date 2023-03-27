from django.shortcuts import render, redirect
from .models import (HomeLogo, HomeBgInfo, HomeSlider, Lastest_Episode,Topic,Trending,About_page,
                     About_boody,AboutSlider,Contact)
from .forms import ContactForm
# Create your views here.

def global_items():
    home_logo = HomeLogo.objects.all()[0]
    return home_logo

def index(request):
    home_bg_info = HomeBgInfo.objects.all()
    home_slider = HomeSlider.objects.all()
    episodes = Lastest_Episode.objects.all()
    topic = Topic.objects.all()
    trending = Trending.objects.all()
    
    
    return render(request, 'main/index.html', context={
    'nbar': 'home',
    'home_logo': global_items(),
    'home_bg_info':home_bg_info,
    'home_slider':home_slider,
    'episodes':episodes,
    'topic':topic,
    'trending':trending
    })

def detail_page(request):
    return render(request, 'main/detail-page.html', context={
    'nbar': 'detail_page',
    'home_logo': global_items()

        
    })

def listing_page(request):
    return render(request, 'main/listing-page.html', context={
    'nbar': 'listing_page',
    'home_logo': global_items()
        
    })

def contact(request):
    name = request.POST.get('full-name')
    email = request.POST.get('email')
    company = request.POST.get('company')
    message = request.POST.get('message')
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            Contact.objects.create(**form.cleaned_data)
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'main/contact.html', context={
    'nbar': 'contact',
    'home_logo': global_items()

        
    })

def about(request):
    about_page = About_page.objects.all()[0]
    about_boody = About_boody.objects.all()[0]
    aboutSlider = AboutSlider.objects.all()
    return render(request, 'main/about.html', context={
    'nbar': 'about',
    'home_logo': global_items(),
    'about_page':about_page,
    'about_boody':about_boody,
    'aboutSlider':aboutSlider
        
    })