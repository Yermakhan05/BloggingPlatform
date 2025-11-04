from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Follow
from .form import ProfileForm


def user_registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('create_profile', user_id=user.id)
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})


def create_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        profileForm = ProfileForm(request.POST, request.FILES)
        if profileForm.is_valid():
            profileUser = profileForm.save(commit=False)
            profileUser.User = user
            profileUser.save()
            return redirect('profile', profileUser.User.id)
    else:
        profileForm = ProfileForm()
    return render(request, 'registration.html', {'form': profileForm, 'user': user})


def user_profile(request, user_id):
    user_p = get_object_or_404(User, id=user_id)

    try:
        profile = Profile.objects.get(User=user_p)
    except Profile.DoesNotExist:
        return redirect('create_profile', user_id=user_id)
    profiles = Profile.objects.exclude(id=profile.id)
    following = Follow.objects.filter(follower=user_p)
    profiles_follow = profiles.filter(User__in=[f.following for f in following])
    profiles_unfollow = profiles.exclude(User__in=[f.following for f in following])
    return render(request, 'profile.html', {
        'profile': profile,
        'profiles_unfollow': profiles_unfollow,
        'profiles_follow': profiles_follow
    })


def edit_profile(request, profile_id):
    profile = get_object_or_404(Profile, pk=profile_id)
    formProfile = ProfileForm(request.POST, instance=profile)
    if request.method == 'POST':
        if formProfile.is_valid():
            profile_edit = formProfile.save(commit=False)
            profile_edit.User = profile.User
            profile_edit.save()
            return redirect('profile', profile_edit.User.id)
    else:
        formProfile = ProfileForm(instance=profile)

    isUpdate = True
    return render(request, 'profile.html', {'formProfile': formProfile, 'profile': profile, 'isUpdate': isUpdate})


def follow_user(request, follower_id, following_id):
    if request.method == 'POST':
        follower_user = get_object_or_404(User, id=follower_id)
        profile = get_object_or_404(Profile, User=follower_user)
        following_user = get_object_or_404(User, id=following_id)
        Follow.objects.get_or_create(follower=follower_user, following=following_user)
        return redirect('profile', profile.User.id)


def unfollow_user(request, follower_id, following_id):
    if request.method == 'POST':
        follower_user = get_object_or_404(User, id=follower_id)
        profile = get_object_or_404(Profile, User=follower_user)
        following_user = get_object_or_404(User, id=following_id)
        Follow.objects.filter(follower=follower_user, following=following_user).delete()
        return redirect('profile', profile.User.id)
