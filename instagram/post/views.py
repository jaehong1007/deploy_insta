from django.shortcuts import render

from .models import Post


def post_list(request):
    """
      모든 Post 목록을 리턴,
      template은 'post/post_list.html'을 사용,
    """
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'post/post_list.html', context)
