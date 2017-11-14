from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

User = get_user_model()

__all__ = (
    'profile'
)

@login_required
def profile(request, user_pk):
    user = User.objects.get(pk=user_pk)
    context = {
        'profile_user': user,
    }
    return render(request, 'member/profile.html', context)