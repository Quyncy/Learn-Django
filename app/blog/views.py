from django.shortcuts import render
from .models import Post


# a view always have to return a Httpresponse or a Exception
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'AboutME'})

def news(request):
    return render(request, 'blog/news.html')

