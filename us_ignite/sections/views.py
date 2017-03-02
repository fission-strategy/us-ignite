from django.http import Http404
from django.template.response import TemplateResponse
from django.shortcuts import get_object_or_404

from us_ignite.apps.models import Application
from us_ignite.hubs.models import Hub
from us_ignite.sections.models import HomepageFeaturedItem, HomepageProgram, Sponsor
from mezzanine.blog.models import BlogPost


def home(request):
    """Homepage of the application.

    List latest featured content.
    """
    context = {
        'featured': HomepageFeaturedItem.objects.filter(status=HomepageFeaturedItem.PUBLISHED).order_by('order').first(),
        'program_list': HomepageProgram.objects.filter(status=HomepageProgram.PUBLISHED).order_by('order').all()[:4],
        'news_list': BlogPost.objects.published(for_user=request.user).all()[:4],
        'application_list': Application.objects.filter(status=Application.PUBLISHED, is_featured=True).order_by('-id').all()[:4],
        'community_list': Hub.objects.filter(status=Hub.PUBLISHED).all(),
        'sponsor_list': Sponsor.objects.filter(status=Sponsor.PUBLISHED).order_by('order').all(),

        # 'resource': Resource.published.get_homepage(),
    }
    return TemplateResponse(request, 'home.html', context)