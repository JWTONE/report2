from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required


def users(request):
    return render(request, "users/users.html")

@login_required
def profile(request, username):
    member = get_object_or_404(get_user_model(), username=username)
    article = member.like_articles.all()
    my_article = member.articles.all()
    context = {
        "member": member,
        "article": article,
        "my_article": my_article,
    }
    return render(request, "users/profile.html", context)


@require_POST
def follow(request, user_id):
    if request.user.is_authenticated:
        member = get_object_or_404(get_user_model(), pk=user_id)
        if member != request.user:
            if member.followers.filter(pk=request.user.pk).exists():
                member.followers.remove(request.user)
            else:
                member.followers.add(request.user)
        return redirect("users:profile", member.username)
    return redirect("accounts:login")


