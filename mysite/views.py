from django.shortcuts import render
from .models import NewsPost


# Create your views here.
def index(request):
    posts = NewsPost.objects.all()
    return render(request, 'site/index.html', {'posts': posts})
