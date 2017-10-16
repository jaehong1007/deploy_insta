
from .models import Post, PostComment
from django.shortcuts import render, redirect


def post_list(request):
    """
      모든 Post 목록을 리턴,
      template은 'post/post_list.html'을 사용,
    """
    posts = Post.objects.all()
    comments = PostComment.objects.all()
    context = {
        'posts': posts,
        'comments': comments
    }
    return render(request, 'post/post_list.html', context)


def post_create(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        # photo = request.FILES['photo']
        # Post.objects.create(photo=photo)
    elif request.method == 'GET':
        return render(request, 'post/post_create.html')


def add_comment(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        content = request.POST.get('content')
        PostComment.objects.create(
            post=post,
            content=content,
        )
        return redirect('post_list')
