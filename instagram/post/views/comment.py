from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect

from ..forms import CommentForm
from ..models import Post, PostComment

__all__ = (
    'comment_create',
    'comment_delete'
)


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
    if not request.user.is_authenticated:
        return redirect('member:signin')
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        # 데이터가 바인딩된 CommentForm인스턴스를 form에 할당
        form = CommentForm(request.POST)
        # 유효성 검증
        if form.is_valid():
            # 통과한 경우, post에 해당하는 Comment인스턴스를 생성
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            # 생성 후 Post의 detail화면으로 이동
            next = request.GET.get('next', '').strip()
            if next:
                return redirect(next)
            return redirect('post:post_list')


def comment_delete(request, comment_pk):
    next_path = request.GET.get('next').strip()
    if request.method == 'POST':
        comment = get_object_or_404(PostComment, pk=comment_pk)
        if comment.author == request.user:
            comment.delete()
            if next_path:
                return redirect(next_path)

            return redirect('post:post_detail', post_pk=comment.post.pk)
        else:
            raise PermissionDenied('작성자가 아닙니다')
