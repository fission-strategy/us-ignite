from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.template.response import TemplateResponse
from models import *

from us_ignite.apps.forms import (ApplicationForm, ApplicationLinkFormSet,
                                  MembershipForm, ApplicationMediaFormSet,
                                  ApplicationMembershipFormSet)

from us_ignite.actionclusters.models import ActionCluster
from us_ignite.common import pagination, forms
from itertools import chain


APPS_SORTING_CHOICES = (
    ('', 'Select ordering'),
    ('created', 'Created (Oldest first)'),
    ('-created', 'Created (Recent first)'),
    ('stage', 'Stage (Ideas first)'),
    ('-stage', 'Stage (Completed first)'),
)


def get_stage_or_404(stage):
    for pk, name in Application.STAGE_CHOICES:
        if pk == int(stage):
            return pk, name
    raise Http404('Invalid stage.')


def app_list(request, sector=None, stage=None, filter_name=''):
    """Lists the published ``Applications``"""
    extra_qs = {}
    if sector:
        # Validate sector is valid if provided:
        extra_qs['sector'] = get_object_or_404(Sector, slug=sector)
        filter_name = extra_qs['sector'].name
    if stage:
        # Validate stage is valid if provided:
        pk, name = get_stage_or_404(stage)
        extra_qs['stage'] = pk
        filter_name = name
    page_no = pagination.get_page_no(request.GET)
    order_form = forms.OrderForm(
        request.GET, order_choices=APPS_SORTING_CHOICES)
    order_value = order_form.cleaned_data['order'] if order_form.is_valid() else ''
    object_list = Application.objects.select_related('sector').filter(
        status=Application.PUBLISHED, **extra_qs)
    # object_list_ac = ActionCluster.objects.select_related('domain').filter(
    #     status=ActionCluster.PUBLISHED, **extra_qs)
    # object_list = list(chain(object_list_app, object_list_ac))
    if order_value:
        object_list = object_list.order_by(order_value)
    featured_list = Application.objects.select_related('sector').filter(
        status=Application.PUBLISHED, is_featured=True, **extra_qs)[:3]
    # # featured_list_ac = ActionCluster.objects.select_related('sector').filter(
    # #     status=ActionCluster.PUBLISHED, is_featured=True, **extra_qs)[:3]
    # featured_list = list(chain(featured_list_app, featured_list_ac))[:3]
    page = pagination.get_page(object_list, page_no)
    context = {
        'featured_list': featured_list,
        'page': page,
        'order': order_value,
        'order_form': order_form,
        'sector_list': Sector.objects.all(),
        'stage_list': Application.STAGE_CHOICES,
        'filter_name': filter_name,
        'current_sector': sector,
        'current_stage': int(stage) if stage else None,
    }
    return TemplateResponse(request, 'apps/object_list.html', context)


def get_app_for_user(slug, user):
    """Validates the user can access the given app."""
    app = get_object_or_404(Application.active, slug__exact=slug)
    # Application is published, no need for validation:
    if app.is_visible_by(user):
        return app
    raise Http404


def get_award_list(app):
    """Returns the list of awards for an app."""
    award_queryset = (ApplicationAward.objects
                      .select_related('award').filter(application=app))
    return [a.award for a in award_queryset]


def get_hub_list(app):
    """Returns the list of hubs for an app."""
    hub_queryset = app.hubappmembership_set.select_related('hub').all()
    return [h.hub for h in hub_queryset]


def app_detail(request, slug):
    app = get_app_for_user(slug, request.user)
    related_list = Application.active.filter(sector=app.sector).order_by('?')[:3]

    context = {
        'object': app,
        'sector': app.sector,
        'url_list': app.applicationurl_set.all(),
        'media_list': app.applicationmedia_set.all(),
        'feature_list': app.features.all(),
        'member_list': app.members.select_related('profile').all(),
        'hub_list': get_hub_list(app),
        'related_list': related_list,
        'award_list': get_award_list(app),
        'can_edit': app.is_editable_by(request.user),
        'is_owner': app.is_owned_by(request.user),
    }
    return TemplateResponse(request, 'apps/object_detail.html', context)


@login_required
def app_add(request):
    """View for adding an ``Application``."""
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
            form.save_m2m()
            messages.success(
                request, 'The application "%s" has been added.' % instance.name)
            return redirect(instance.get_absolute_url())
    else:
        form = ApplicationForm()
    context = {
        'form': form,
    }
    return TemplateResponse(request, 'apps/object_add.html', context)


@login_required
def app_edit(request, slug):
    app = get_object_or_404(Application.active, slug__exact=slug)
    if not app.is_editable_by(request.user):
        raise Http404
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES, instance=app)
        link_formset = ApplicationLinkFormSet(request.POST, instance=app)
        image_formset = ApplicationMediaFormSet(
            request.POST, request.FILES, instance=app)
        if (form.is_valid() and link_formset.is_valid()
            and image_formset.is_valid()):
            instance = form.save()
            link_formset.save()
            image_formset.save()
            messages.success(
                request, 'The application "%s" has been updated.' % instance.name)
            return redirect(instance.get_absolute_url())
    else:
        form = ApplicationForm(instance=app)
        link_formset = ApplicationLinkFormSet(instance=app)
        image_formset = ApplicationMediaFormSet(instance=app)
    context = {
        'object': app,
        'form': form,
        'link_formset': link_formset,
        'image_formset': image_formset,
    }
    return TemplateResponse(request, 'apps/object_edit.html', context)