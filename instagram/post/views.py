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
    comment_form = CommentForm()
    context = {
        'post': post,
        'comment_form': comment_form
    }
    return render(request, 'post/post_detail.html', context)


def comment_create(request, post_pk):
    """
    post_pk에 해당하는 Post에 연결된 PostComment를 작성
    PostComment Form을 생성해서 사용
    기본적인 루틴은 위의 post_create와 같음
    :param request:
    :param post_pk:
    :return:
    """
    # URL get parameter로 온 'post_pk'에 해당하는
    # Post instance를 'post'변수에 할당
    # 찾지못하면 404Error를 브라우저에 리턴
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        # 데이터가 바인딩된 CommentForm인스턴스를 form에 할당
        form = CommentForm(request.POST)
        # 유효성 검증
        if form.is_valid():
            # 통과한 경우, post에 해당하는 Comment인스턴스를 생성
            PostComment.objects.create(
                post=post,
                content=form.cleaned_data['content']
            )
            # 생성 후 Post의 detail화면으로 이동
            return redirect('post_detail', post_pk=post_pk)
