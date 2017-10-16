from django.http import HttpResponse

from post.forms import PostForm, CommentForm
from .models import Post, PostComment
from django.shortcuts import render, redirect, get_object_or_404

__all__ = {}


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
        """
        Post를 생성
        반드시 photo필드에 해당하는 파일이 와야한다
        :param request:
        :return:
        1. post_create.html파일을 만들고
             /post/create/ URL로 요청이 온 경우
             이 뷰에서 해당 파일을 render해서 response
        2. post_create.html에 form을 만들고,
            file input과 button요소를 배치
            file input의 name은 'photo'로 지정
        3. 이 뷰에서 request.method가 'POST'일 경우,
            request.POST와 request.FILES를 print문으로 출력
            'GET'이면 템플릿파일을 보여주는 기존 로직을 그대로 실행
        """
        # photo = request.FILES.get('photo')
        if request.method == 'POST':
            # 1. 파일이 오지 않았을 경우, GET요청과 같은 결과를 리턴
            #   1-1. 단, return render(...)하는 같은 함수를 두번 호출하지 말 것
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                print(form.cleaned_data)
                post = Post.objects.create(
                    photo=form.cleaned_data['photo']
                )
                return HttpResponse(f'<img src="{post.photo.url}">')
        else:
            # GET요청의 경우 빈 PostForm인스턴스를 생성해서 템플릿에 전달
            form = PostForm()
        # GET요청에선 이부분이 무조건 실행
        # POST요청에선 formis_valid()를 통과하지 못하면 비부분이 실행
        context = {
            'form': form
        }
        return render(request, 'post/post_create.html', context)


def post_detail(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    context = {
        'post': post
    }
    return render(request, 'post/post_detail.html', context)


def comment_create(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = PostComment.objects.create(
                post=post,
                content=content,
            )
        # post = Post.objects.get(pk=post_pk)
        # content = request.POST.get('content')
        return redirect('post_detail', post_pk=pk)
    else:
        form = CommentForm()
        context = {
            'form': form
        }
        return render(request, 'post/comment_create.html/', context)
