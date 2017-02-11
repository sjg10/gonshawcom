from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .models import Post

# Create your views here.
def index(request):
    math_posts = Post.objects.filter(post_topic='m')
    software_posts = Post.objects.filter(post_topic='s')
    context = {'math_posts': math_posts,
        'software_posts': software_posts}
    return render(request, 'content/index.html', context)
