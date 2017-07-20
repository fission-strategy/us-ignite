from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.http import urlencode

from watson import search as watson

from .forms import SearchForm
from .filters import tag_search

from us_ignite.apps.models import Application, Sector, Feature
from us_ignite.hubs.models import Hub
from us_ignite.common import pagination
from mezzanine.conf import settings
from mezzanine.utils.views import paginate
from us_ignite.programs.models import Program


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

    query = request.GET.get("q", "")
    page = request.GET.get("page", 1)
    per_page = settings.SEARCH_PER_PAGE
    max_paging_links = settings.MAX_PAGING_LINKS
    if form.is_valid():
        object_list = list(watson.search(form.cleaned_data['q'], SEARCH_PARAMS['default']))
        pagination_qs = '&%s' % urlencode({'q': form.cleaned_data['q']})
    else:
        object_list = []
        pagination_qs = ''

    results = object_list
    # page.object_list_top = [o.object for o in page.object_list_top]
    # page.object_list_bottom = [o.object for o in page.object_list_bottom]\

    paginated = paginate(results, page, per_page, max_paging_links)
    context = {
        'query': form.cleaned_data['q'],
        # 'form': form,
        'results': paginated,
        'search_type': "Everything"
        # 'pagination_qs': pagination_qs,
        # 'slug': slug
    }

    # query = request.GET.get("q", "")
    # page = request.GET.get("page", 1)
    # per_page = settings.SEARCH_PER_PAGE
    # max_paging_links = settings.MAX_PAGING_LINKS
    # try:
    #     parts = request.GET.get("type", "").split(".", 1)
    #     search_model = apps.get_model(*parts)
    #     search_model.objects.search  # Attribute check
    # except (ValueError, TypeError, LookupError, AttributeError):
    #     search_model = Displayable
    #     search_type = _("Everything")
    # else:
    #     search_type = search_model._meta.verbose_name_plural.capitalize()
    # results = search_model.objects.search(query, for_user=request.user)
    # paginated = paginate(results, page, per_page, max_paging_links)
    # context = {"query": query, "results": paginated,
    #            "search_type": search_type}
    # context.update(extra_context or {})
    # return TemplateResponse(request, template, context)

    # return TemplateResponse(request, 'search/object_list.html', context)
    return TemplateResponse(request, 'search_results.html', context)

@csrf_exempt
def search_apps(request):
    form = SearchForm(request.GET) if 'q' in request.GET else SearchForm()
    page_no = pagination.get_page_no(request.GET)
    app_terminalogy = None
    if form.is_valid():
        extra_params = {}

        if form.cleaned_data['sector'] != '':
            extra_params.update({'sector__slug': form.cleaned_data['sector'], }, )
        if form.cleaned_data['community'] != '':
            extra_params.update({'hub__slug': form.cleaned_data['community'], }, )
        if 'program' in form.cleaned_data and form.cleaned_data['program'] != '':
            extra_params.update({'program__slug': form.cleaned_data['program'], }, )
            app_terminalogy = (Program.objects.get(slug=form.cleaned_data['program'])).application_terminology
        if 'q' in form.cleaned_data and form.cleaned_data['q'] != '':
            object_list = watson.filter(Application.objects.filter(**extra_params),
                                        form.cleaned_data['q'])
        else:
            object_list = Application.objects.filter(status=Application.PUBLISHED, **extra_params)

        if form.cleaned_data['order'] == 'asc':
            object_list = object_list.order_by('created')
        elif form.cleaned_data['order'] == 'desc':
            object_list = object_list.order_by('-created')

        pagination_qs = '&%s' % urlencode({'q': form.cleaned_data['q']})
    else:
        object_list = []
        pagination_qs = ''

    page = pagination.get_page(object_list, page_no)
    page.object_list_top = [o for o in page.object_list_top]
    page.object_list_bottom = [o for o in page.object_list_bottom]
    community_list_sgc = Hub.objects.filter(status=Hub.PUBLISHED,
                                        programs__slug__in=['smart-gigabit-communities', ]).order_by('name')
    community_list_other = Hub.objects.filter(status=Hub.PUBLISHED).exclude(
                                         programs__slug__in=['smart-gigabit-communities', ]).order_by('name')
    context = {
        'form': form,
        'page': page,
        'pagination_qs': pagination_qs,
        'sector_list': Sector.objects.all(),
        'community_list_sgc': community_list_sgc,
        'community_list_other': community_list_other,
    }
    if app_terminalogy:
        context.update({'app_terminalogy': app_terminalogy},)
    return TemplateResponse(request, 'apps/object_list.html', context)


@csrf_exempt
def search_hubs(request):
    form = SearchForm(request.GET) if 'q' in request.GET else SearchForm()
    page_no = pagination.get_page_no(request.GET)
    if form.is_valid():
        extra_params = {}

        if 'feature' in form.cleaned_data and form.cleaned_data['feature'] != '':
            extra_params.update({'features__slug__in': [form.cleaned_data['feature'], ]}, )
        if 'program' in form.cleaned_data and form.cleaned_data['program'] != '':
            extra_params.update({'programs__slug__in': [form.cleaned_data['program'], ]}, )
        if 'q' in form.cleaned_data and form.cleaned_data['q'] != '':
            object_list = watson.filter(Hub.objects.filter(**extra_params),
                                        form.cleaned_data['q'])
        else:
            object_list = Hub.objects.filter(status=Application.PUBLISHED, **extra_params)

        if form.cleaned_data['order'] == 'asc':
            object_list = object_list.order_by('created')
        elif form.cleaned_data['order'] == 'desc':
            object_list = object_list.order_by('-created')

        pagination_qs = '&%s' % urlencode({'q': form.cleaned_data['q']})
    else:
        object_list = []
        pagination_qs = ''

    page = pagination.get_page(object_list, page_no)
    page.object_list_top = [o for o in page.object_list_top]
    page.object_list_bottom = [o for o in page.object_list_bottom]
    context = {
        'form': form,
        'page': page,
        'pagination_qs': pagination_qs,
        # 'feature_list': Feature.objects.all(),
        'program_list': Program.objects.all(),
    }
    return TemplateResponse(request, 'hubs/object_list.html', context)
