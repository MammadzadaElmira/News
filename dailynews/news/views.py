from django.shortcuts import render
#from django.http import HttpResponse
from .models import Feed
# Create your views here.

"""def home(request):
    newsfeed = Feed.objects.all()
    return HttpResponse(newsfeed)
"""
def home(request):
    sites = Feed.objects.all()
    context = {
        "news": sites
    }
    return render(request, "news/home.html", context)