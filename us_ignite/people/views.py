from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse
from django.shortcuts import get_object_or_404

from us_ignite.apps.models import Application
from us_ignite.programs.models import Program
from us_ignite.awards.models import UserAward
from us_ignite.news.models import NewsPost as Post
from us_ignite.common import pagination, forms
# from us_ignite.events.models import Event
from us_ignite.hubs.models import Hub, HubMembership, HubRequest
from us_ignite.organizations.models import Organization, OrganizationMember
from us_ignite.profiles.models import User as Profile
from us_ignite.resources.models import Resource


PROFILE_SORTING_CHOICES = (
    ('', 'Select ordering'),
    ('user__first_name', 'Name a-z'),
    ('-user__first_name', 'Name z-a'),
)


@login_required
def profile_list(request):
    page_no = pagination.get_page_no(request.GET)
    order_form = forms.OrderForm(
        request.GET, order_choices=PROFILE_SORTING_CHOICES)
    order_value = order_form.cleaned_data['order'] if order_form.is_valid() else ''
    object_list = Profile.active.all()
    if order_value:
        # TODO consider using non case-sensitive ordering:
        object_list = object_list.order_by(order_value)
    page = pagination.get_page(object_list, page_no)
    context = {
        'page': page,
        'order': order_value,
        'order_form': order_form,
    }
    return TemplateResponse(request, 'people/object_list.html', context)


def get_application_list(owner, viewer=None, program=None):
    """Returns visible ``Applications`` from the given ``viewer``."""
    qs_kwargs = {'owner': owner}
    if program:
        qs_kwargs.update({'program': program})
    if not viewer or not owner == viewer:
        qs_kwargs.update({'status': Application.PUBLISHED})
    return Application.active.filter(**qs_kwargs)


# def get_actioncluster_list(owner, viewer=None):
#     """Returns visible ``Action Cluster`` from the given ``viewer``."""
#     qs_kwargs = {'owner': owner}
#     if not viewer or not owner == viewer:
#         qs_kwargs.update({'status': ActionCluster.PUBLISHED})
#     return ActionCluster.active.filter(**qs_kwargs)


def get_similar_applications(application_list, total=4):
    params = {
        'status': Application.PUBLISHED,
    }
    if application_list:
        application = application_list[0]
        params['sector'] = application.sector
        object_list =  (Application.active.filter(**params)
                        .exclude(owner=application.owner))
    else:
        object_list = Application.active.filter(**params)
    return object_list.order_by('?')[:total]


# def get_event_list(user, viewer=None):
#     """Returns visible ``Events`` from the given ``viewer``."""
#     qs_kwargs = {'user': user}
#     if not viewer or not user == viewer:
#         qs_kwargs.update({'status': Event.PUBLISHED})
#     return Event.objects.filter(**qs_kwargs)


def get_resource_list(contact, viewer=None):
    qs_kwargs = {'contact': contact}
    if not viewer or not contact == viewer:
        qs_kwargs.update({'status': Resource.PUBLISHED})
    return Resource.objects.filter(**qs_kwargs)


def get_hub_owned_list(contact, viewer=None):
    qs_kwargs = {'contact': contact}
    if not contact or not contact == viewer:
        qs_kwargs.update({'status': Hub.PUBLISHED})
    return Hub.objects.filter(**qs_kwargs)

# def get_actioncluster_owned_list(contact, viewer=None):
#     qs_kwargs = {'contact': contact}
#     if not contact or not contact == viewer:
#         qs_kwargs.update({'status': ActionCluster.PUBLISHED})
#     return ActionCluster.objects.filter(**qs_kwargs)

def get_organization_list(user, viewer=None):
    qs_kwargs = {'user': user}
    if not user or not user == viewer:
        qs_kwargs.update({'organization__status': Organization.PUBLISHED})
    return (OrganizationMember.objects.select_related('organization')
            .filter(**qs_kwargs))


def get_hub_membership_list(user, viewer=None):
    qs_kwargs = {'user': user}
    if not user or not user == viewer:
        qs_kwargs.update({'hub__status': Hub.PUBLISHED})
    membership_list = (HubMembership.objects.select_related('hub')
                       .filter(**qs_kwargs))
    return [m.hub for m in membership_list]


def get_hub_list(user, viewer=None):
    hub_list = list(get_hub_owned_list(user, viewer=viewer))
    #hub_list += list(get_appl_owned_list(user, viewer=viewer))
    hub_list += get_hub_membership_list(user, viewer=viewer)
    return list(set(hub_list))


def get_featured_hub_list(limit=2):
    return (Hub.objects.filter(status=Hub.PUBLISHED, is_featured=True)
            .order_by('?')[:limit])


def get_award_list(user, viewer=None):
    qs_kwargs = {'user': user}
    award_qs = UserAward.objects.select_related('award').filter(**qs_kwargs)
    return [a.award for a in award_qs]


def get_post_list(limit=7):
    return (Post.objects.filter(status=2).all()
            .order_by('-is_featured', '-publish_date')[:limit])


def get_featured_resources(limit=2):
    return Resource.published.filter(is_featured=True)[:limit]

# def get_featured_events(limit=2):
#     return (Event.published.filter(is_featured=True)
#             .order_by('?')[:limit])


@login_required
def profile_detail(request, slug):
    """Public profile of a user."""
    profile = get_object_or_404(
        Profile.active, slug__exact=slug)
    # is_owner = profile.user == request.user
    # Content available when the ``User`` owns this ``Profile``:
    hub_request_list = HubRequest.objects.filter(user=profile) if profile else []
    # actioncluster_list = list(get_actioncluster_list(user, viewer=request.user))
    get_hub_list(profile, viewer=request.user)
    context = {
        'object': profile,
        'is_owner': profile,
        'application_list': get_application_list(profile, viewer=request.user),
        'event_list': {},
        'resource_list': get_resource_list(profile, viewer=request.user),
        'hub_list': get_hub_list(profile, viewer=request.user),
        'hub_request_list': hub_request_list,
        'organization_list': get_organization_list(profile, viewer=request.user),
        'award_list': get_award_list(profile, viewer=request.user),
        # 'actioncluster_list': actioncluster_list[:3],
    }
    return TemplateResponse(request, 'people/object_detail.html', context)


@login_required
def dashboard(request):
    profile, is_new = Profile.objects.get_or_create(username=request.user)
    user = profile.id
    application_list = list(get_application_list(user, viewer=request.user))
    programs = Program.objects.all()
    program_app_list = {}
    for program in programs:
        program_app_list.update({program: list(get_application_list(user, viewer=request.user, program=program))})
    similar_applications = get_similar_applications(application_list)
    event_list = {}
    resource_list = get_resource_list(user, viewer=request.user)
    content_list = (list(event_list) + list(resource_list))
    hub_list = get_hub_list(user, viewer=request.user)
    hub_id_list = [h.id for h in hub_list]
    context = {
        'object': profile,
        'application_list': application_list[:3],
        'program_app_list': program_app_list,
        'similar_applications': similar_applications,
        'post_list': get_post_list(),
        'hub_list': hub_list[:7],
        'hub_event_list': {},
        'featured_event_list': {},
        'featured_hub_list': get_featured_hub_list(),
        'featured_resource_list': get_featured_resources(),
        'content_list': content_list,
        'hub_request_list': HubRequest.objects.filter(user=user)[:6],
    }
    return TemplateResponse(request, 'people/dashboard.html', context)
