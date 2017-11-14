from django.contrib.auth import get_user_model
from django.shortcuts import redirect

User = get_user_model()

__all__ = (
    'follow_toggle',
)


def follow_toggle(request, user_pk):
    if request.method == 'POST':
        from_user = request.user
        to_user = User.objects.get(pk=user_pk)
        from_user.follow_toggle(to_user)
        return redirect('member:profile', user_pk=user_pk)
