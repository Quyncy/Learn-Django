from django.shortcuts import render


posts = [
    {
        'author': 'Corey',
        'title': 'Blog1',
        'content': 'First post content',
        'date': 'August 27,2018'
    },
    {
        'author': 'Schafer',
        'title': 'Blog2',
        'content': 'Second post content',
        'date': 'August 28,2018'
    }
]

# a view always have to return a Httpresponse or a Exception
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'AboutME'})

def news(request):
    return render(request, 'blog/news.html')

