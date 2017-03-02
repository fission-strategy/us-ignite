from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.http import urlencode

from watson import search as watson

from forms import SearchForm
from filters import tag_search

from us_ignite.apps.models import Application
from us_ignite.common import pagination


@csrf_exempt
def search_apps(request):
    return tag_search(
        request, Application.active.filter(status=Application.PUBLISHED, program=None),
        'search/application_list.html'
    )


SEARCH_PARAMS = {
    'default': (),
    'apps': (
        Application
    )
}


def get_search_results(query, slug):
    if slug not in SEARCH_PARAMS:
        raise Http404("Invalid search slug.")
    models = SEARCH_PARAMS[slug]
    object_list = list(watson.search(query, models=models))
    if models:
        object_list += list(watson.search(query, exclude=models))
    return object_list


@csrf_exempt
def search(request, slug='default'):
    form = SearchForm(request.GET) if 'q' in request.GET else SearchForm()
    page_no = pagination.get_page_no(request.GET)

    if form.is_valid():
        object_list = get_search_results(form.cleaned_data['q'], slug)
        pagination_qs = '&%s' % urlencode({'q': form.cleaned_data['q']})
    else:
        object_list = []
        pagination_qs = ''
    page = pagination.get_page(object_list, page_no)
    page.object_list_top = [o.object for o in page.object_list_top]
    page.object_list_bottom = [o.object for o in page.object_list_bottom]
    context = {
        'form': form,
        'page': page,
        'pagination_qs': pagination_qs,
    }
    return TemplateResponse(request, 'search/object_list.html', context)
