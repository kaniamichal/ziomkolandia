from django.http import request, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template.defaultfilters import first
from django.utils import timezone

import blog
from blog.models import Post
from newsletter.forms import JoinForm


def blog_latest(request):
    latest_post = Post.objects.filter(publish_date__lte=timezone.now()).order_by('-created_date')[:2]
    return {'latest_post': latest_post}


def blog_latest_pos4(request):
    latest_post_pos4 = Post.objects.all().order_by('-id')[0:1]
    return {'latest_post_pos4': latest_post_pos4}


def blog_latest_pos3(request):
    latest_post_pos3 = Post.objects.all().order_by('-id')[1:2]
    return {'latest_post_pos3': latest_post_pos3}


def blog_latest_pos2(request):
    latest_post_pos2 = Post.objects.all().order_by('-id')[2:3]
    return {'latest_post_pos2': latest_post_pos2}


def blog_latest_pos1(request):
    latest_post_pos1 = Post.objects.all().order_by('-id')[3:4]
    return {'latest_post_pos1': latest_post_pos1}


def blog_latest3(request):
    latest_post3 = Post.objects.filter(publish_date__lte=timezone.now()).order_by('-created_date')[:3]
    return {'latest_post3': latest_post3}



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
            email = ''
    else:
        form = JoinForm()
    return {'form': form}


def cookielaw(request):
    """Add cookielaw context variable to the context."""

    cookie = request.COOKIES.get('cookielaw_accepted')
    return {
        'cookielaw': {
            'notset': cookie is None,
            'accepted': cookie == '1',
            'rejected': cookie == '0',
        }
    }
