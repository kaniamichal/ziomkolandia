from django.http import request, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.utils import timezone

import blog
from blog.models import Post
from newsletter.forms import JoinForm


def blog_latest(request):
    latest_post = Post.objects.filter(publish_date__lte=timezone.now()).order_by('-created_date')[:2]
    return {'latest_post': latest_post}


def join_form(request):
    if request.method == "POST":
        form = JoinForm(request.POST)
        email = request.POST.get('newsletter_email', '')
        print(email)
        if form.is_valid():
            join = form.save(commit=False)
            join.newsletter_email = email
            print(email)
            join.newsletter_timestamp = timezone.now()
            join.save()
            return redirect('/')
    else:
        form = JoinForm()
    return {'form': form}
#
#     if request.method == 'POST':
#
#         form = JoinForm(data=request.POST)
#         email = request.POST.get('newsletter_email', '')
#         if form.is_valid():
#             join = form.save(commit=False)
#             join.newsletter_email = email
#             print(email)
#             join.newsletter_timestamp = timezone.now()
#             join.save()
#             return 'website/thanks.html'
#
#     else:
#         form = JoinForm(request)
#
#     request.news_form = form
