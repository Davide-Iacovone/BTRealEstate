from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing 
from realtors.models import Realtor

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings
    }
    return render(request, 'index.html', context)

def about(request):
    realtors = Realtor.objects.order_by('name')
    MVP = Realtor.objects.all().filter(is_mvp=True)
    context = {
        'realtors': realtors,
        'MVP': MVP
    }
    return render(request, 'about.html', context)
