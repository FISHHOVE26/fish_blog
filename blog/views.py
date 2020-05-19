from django.shortcuts import render,get_object_or_404
from .models import Posts


# Create your views here.
def home(request):
    posts = Posts.objects.all()
    title= 'home'
    return render(request, 'blog/home.html', {'posts': posts,'title':title })


def about(request):
    return render(request, 'blog/about.html',{'title': 'about'})


def detail(request, post_id):
    post = get_object_or_404(Posts, pk=post_id)
    title= 'detail'
    return render(request, 'blog/detail.html', {'post': post,'title':title})

    

