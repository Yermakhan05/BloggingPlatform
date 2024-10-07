import datetime

from django.contrib.auth import logout
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt

from blog.form import PostForm, PostUpdateForm, CommentForm
from blog.models import Post, Comment


@csrf_exempt
def post_list(request):
    query = request.GET.get('q')
    posts = Post.objects.all().order_by('-Created_at')

    if query:
        posts = posts.filter(Q(Title__icontains=query) | Q(Content__icontains=query))

    paginator = Paginator(posts, 6)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'post_list.html', {'page_obj': page_obj})


def post_view(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(Post=post).order_by('-Created_at')

    if request.method == 'POST':
        commentForm = CommentForm(request.POST)
        if commentForm.is_valid():
            new_comment = commentForm.save(commit=False)
            new_comment.Created_at = datetime.datetime.now()
            new_comment.Post = post
            new_comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        commentForm = CommentForm()

    return render(request, 'post_detail.html', {
        'post': post,
        'comments': comments,
        'commentForm': commentForm
    })


def post_form(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.Created_at = datetime.datetime.now()
            new_post.save()
            return redirect('post_list')
        else:
            return render(request, 'post_form.html', {'form': form})
    else:
        form = PostForm()
    return render(request, 'post_form.html', {'form': form})


@csrf_exempt
def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return redirect('post_detail.html', pk=pk)


def custom_logout_view(request):
    logout(request)
    return redirect('post_list')


@csrf_exempt
def post_update(request, pk):
    post = Post.objects.get(pk=pk)
    formUpdate = PostUpdateForm(request.POST, instance=post)
    if request.method == 'POST':
        if formUpdate.is_valid():
            new_post = formUpdate.save(commit=False)
            new_post.Created_at = datetime.datetime.now()
            new_post.Author = post.Author
            new_post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        formUpdate = PostUpdateForm(instance=post)

    isUpdate = True
    return render(request, 'post_detail.html', {'formUpdate': formUpdate, 'post': post, 'isUpdate': isUpdate})
