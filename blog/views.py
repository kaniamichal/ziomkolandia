from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import CommentPost, ReplayCommentForm
from .models import Post, Comment, ReplyComment


def post_detail2(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.filter(active=True, parent__isnull=True)
    if request.method == 'POST':
        comment_form = CommentPost(data=request.POST)
        if comment_form.is_valid():
            parent_obj = None
            try:
                parent_id = int(request.POST.get('parent_id'))
            except:
                parent_id = None
            if parent_id:
                parent_obj = Comment.objects.get(id=parent_id)
                if parent_obj:
                    replay_comment = comment_form.save(commit=False)
                    replay_comment.parent = parent_obj
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return render(request, 'website/post_detail.html', {'post': post})
        else:
            comment_form = CommentPost()
        return render(request, 'website/post_detail.html',
                      {'post': post, 'comments': comments, 'comment_form': comment_form})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments(request, pk=pk)
    # replay_comment(request, comments)
    return render(request, 'website/post_detail.html', {'post': post})


def comments_detail(request, pk):
    com = get_object_or_404(Comment, pk=pk)
    replay_comment(request, com)
    return render(request, 'website/replay_comment.html', {'comment': com})


def aktualnosci(request):
    posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('-created_date')[:12]
    paginator = Paginator(posts, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'website/aktualnosci.html', {'posts': posts, 'page_obj': page_obj})



# def blog(request):
#     posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('-created_date')
#     return render(request, 'website/aktualnosci.html', {'posts': posts})


# comments
def comments(request, pk):
    if request.method == "POST":
        form = CommentPost(request.POST)
        name = request.POST.get('name', '')
        content = request.POST.get('content', '')
        comment = form.save(commit=False)
        comment.post_id = pk
        comment.name = name
        comment.content = content
        comment.date_added = timezone.now()
        comment.save()
        return redirect('/')
    else:
        form = CommentPost()
    return render(request, 'website/post_detail.html', {'form': form})


# replay comments
def replay_comment(request, con):
    con = Comment.objects.get(id)
    if request.method == "POST":
        form = ReplayCommentForm(request.POST)
        replay_name = request.POST.get('replay_name', '')
        replay_content = request.POST.get('replay_content', '')
        replay_com = form.save(commit=False)
        replay_com.replay_comment_id = con
        replay_com.replay_name = replay_name
        replay_com.replay_content = replay_content
        replay_com.replay_date_added = timezone.now()
        replay_com.save()
        return redirect('website/post_detail.html')
    else:
        form = CommentPost()
    return render(request, 'website/post_detail.html', {'form': form})
