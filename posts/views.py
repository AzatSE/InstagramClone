from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import JsonResponse
from .models import Post, Profile


@login_required
def feed(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        caption = request.POST.get('caption', '')
        if image:
            Post.objects.create(author=request.user, image=image, caption=caption)
        return redirect('feed')

    posts = Post.objects.all()
    return render(request, 'posts/feed.html', {'posts': posts})


@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user

    if user in post.likes.all():
        post.likes.remove(user)
        liked = False
    else:
        post.likes.add(user)
        liked = True

    return JsonResponse({'liked': liked, 'total_likes': post.total_likes()})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            login(request, user)
            return redirect('feed')
    else:
        form = UserCreationForm()
    return render(request, 'posts/register.html', {'form': form})


@login_required
def profile(request):
    profile_obj, _ = Profile.objects.get_or_create(user=request.user)
    posts = Post.objects.filter(author=request.user)


    if request.method == 'POST':
        profile_photo = request.FILES.get('profile_photo')
        bio = request.POST.get('bio', '')
        if profile_photo:
            profile_obj.profile_photo = profile_photo
        profile_obj.bio = bio
        profile_obj.save()
        return redirect('profile')
    return render(request, 'posts/profile.html', {'profile_obj': profile_obj, 'posts': posts})