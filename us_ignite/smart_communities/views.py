from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.template.loader import render_to_string
from django.template.response import TemplateResponse
from django.views.decorators.http import require_http_methods
from django.utils import timezone

from mezzanine.blog.models import BlogPost

from us_ignite.apps.models import Application


def home_view(request):
    extra_qs = {}
    featured_list = Application.objects.filter(status=Application.PUBLISHED, is_featured=True, **extra_qs)[:3]
    latest_news_list = BlogPost.objects.filter(status=1).latest('created')

