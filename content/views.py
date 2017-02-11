from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .models import Post

# Create your views here.
def index(request):
    math_posts = Post.objects.all()
    context = {'math_posts': math_posts}
    return render(request, 'content/index.html', context)

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'content/post.html', {'post': post})
