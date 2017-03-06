from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.http import urlencode

from watson import search as watson

from forms import SearchForm
from filters import tag_search

from us_ignite.apps.models import Application, Sector
from us_ignite.common import pagination





SEARCH_PARAMS = {
    'default': (),
    'apps': (
        Application,
    )
}


def get_search_results(query, slug):
    if slug not in SEARCH_PARAMS:
        raise Http404("Invalid search slug.")
    models = SEARCH_PARAMS[slug]
    object_list = (watson.filter(models, query))
    # if models:
    #     object_list += list(watson.search(query, exclude=models))
    return object_list


@csrf_exempt
def search(request, slug='default'):
    form = SearchForm(request.GET) if 'q' in request.GET else SearchForm()
    page_no = pagination.get_page_no(request.GET)

    if form.is_valid():
        # if slug == 'apps':
        #     if form.cleaned_data['q'] == '':
        #         object_list = Application.objects.
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
        'slug': slug
    }
    if slug == 'apps':
        context.update ({
            'sector_list': Sector.objects.all()
        })
        return TemplateResponse(request, 'apps/object_list.html', context)
    return TemplateResponse(request, 'search/object_list.html', context)


@csrf_exempt
def search_apps(request):
    form = SearchForm(request.GET) if 'q' in request.GET else SearchForm()
    page_no = pagination.get_page_no(request.GET)

    if form.is_valid():
        if form.cleaned_data['sector'] != '':
            if form.cleaned_data['q'] != '':
                object_list = watson.filter(Application.objects.filter(sector__slug=form.cleaned_data['sector']), form.cleaned_data['q'])
            else:
                object_list = Application.objects.filter(status=Application.PUBLISHED, sector__slug=form.cleaned_data['sector'])
        else:
            if form.cleaned_data['q'] != '':
                object_list = watson.filter(Application, form.cleaned_data['q'])
            else:
                object_list = Application.objects.filter(status=Application.PUBLISHED)
        if form.cleaned_data['order'] == 'asc':
            object_list = object_list.order_by('created')
        elif form.cleaned_data['order'] == 'desc':
            object_list = object_list.order_by('-created')

        pagination_qs = '&%s' % urlencode({'q': form.cleaned_data['q']})
    else:
        object_list = []
        pagination_qs = ''
    for obj in object_list:
        print obj.categories.all()
    page = pagination.get_page(object_list, page_no)
    page.object_list_top = [o for o in page.object_list_top]
    page.object_list_bottom = [o for o in page.object_list_bottom]
    context = {
        'form': form,
        'page': page,
        'pagination_qs': pagination_qs,
        'sector_list': Sector.objects.all(),
    }
    return TemplateResponse(request, 'apps/object_list.html', context)
