from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, "blogposts.html", {'posts': posts})


def post_details(request, id):
    """
    :param request:
    :param id:
    :return:

    """
    post = get_object_or_404(Post, pk=id)
    post.views += 1
    post.save()
    return render(request, "postdetail.html", {'post': post})


def top_posts(request):
    """
    :param request:
    :return:
    """
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-views')[:5]
    return render


