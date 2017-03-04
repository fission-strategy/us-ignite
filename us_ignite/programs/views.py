from django.shortcuts import render
from django.template.response import TemplateResponse

from us_ignite.news.models import NewsPost as BlogPost
from us_ignite.hubs.models import Hub
from us_ignite.apps.models import Application, TaggedFunder, TaggedCategory, Sector
from us_ignite.testbeds.models import Testbed
from models import Program, Link


def program_home(request, slug):
    program = Program.objects.get(slug=slug)
    sector_list = Sector.objects.all()
    app_list = {}
    for sector in sector_list:
        apps = list([Application.objects.filter(status=Application.PUBLISHED,
                                                sector=sector,
                                                program=program).all()[:3], sector.slug])
        app_list.update({sector: apps})

    context = {
        'program': program,
        'app_list': app_list,
        'latest_news': BlogPost.objects.published(for_user=request.user).filter(event=False).order_by('-created').first(),
        'upcoming_event': BlogPost.objects.published(for_user=request.user).filter(event=True).order_by('-created').first(),
        'funding_agent_list': program.program_funding_partner_set.all(),
        'link_list': program.program_link_set.filter(status=Link.PUBLISHED).all()[:3],
        'app_count': Application.objects.filter(status=Application.PUBLISHED, program=program).count(),
        'hub_count': Hub.objects.filter(status=Hub.PUBLISHED, programs__in=[program, ]).count(),
        'funder_count': TaggedFunder.objects.count(),
        'testbed_count': Testbed.objects.filter(status=Testbed.PUBLISHED, programs__in=[program, ]).count(),
    }
    return TemplateResponse(request, 'programs/home.html', context)
