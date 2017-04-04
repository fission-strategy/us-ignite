from __future__ import unicode_literals
from future.builtins import str

from django.core.exceptions import ImproperlyConfigured
from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.template.response import TemplateResponse
from django.views.decorators.csrf import requires_csrf_token
from django.template.loader import get_template
from django.utils import six

from mezzanine.utils.urls import home_slug
from mezzanine.conf import settings
from us_ignite.news.models import NewsPost as BlogPost
from us_ignite.common.models import LinkResource



def page(request, slug, template=u"pages/page.html", extra_context={}):
    """
    Select a template for a page and render it. The request
    object should have a ``page`` attribute that's added via
    ``mezzanine.pages.middleware.PageMiddleware``. The page is loaded
    earlier via middleware to perform various other functions.
    The urlpattern that maps to this view is a catch-all pattern, in
    which case the page attribute won't exist, so raise a 404 then.

    For template selection, a list of possible templates is built up
    based on the current page. This list is order from most granular
    match, starting with a custom template for the exact page, then
    adding templates based on the page's parent page, that could be
    used for sections of a site (eg all children of the parent).
    Finally at the broadest level, a template for the page's content
    type (it's model class) is checked for, and then if none of these
    templates match, the default pages/page.html is used.
    """

    from mezzanine.pages.middleware import PageMiddleware
    if not PageMiddleware.installed():
        raise ImproperlyConfigured("mezzanine.pages.middleware.PageMiddleware "
                                   "(or a subclass of it) is missing from " +
                                   "settings.MIDDLEWARE_CLASSES or " +
                                   "settings.MIDDLEWARE")

    if not hasattr(request, "page") or request.page.slug != slug:
        raise Http404

    # Check for a template name matching the page's slug. If the homepage
    # is configured as a page instance, the template "pages/index.html" is
    # used, since the slug "/" won't match a template name.
    template_name = str(slug) if slug != home_slug() else "index"
    templates = [u"pages/%s.html" % template_name]
    method_template = request.page.get_content_model().get_template_name()
    if method_template:
        templates.insert(0, method_template)
    if request.page.content_model is not None:
        templates.append(u"pages/%s/%s.html" % (template_name,
            request.page.content_model))
    for parent in request.page.get_ascendants(for_user=request.user):
        parent_template_name = str(parent.slug)
        # Check for a template matching the page's content model.
        if request.page.content_model is not None:
            templates.append(u"pages/%s/%s.html" % (parent_template_name,
                request.page.content_model))
    # Check for a template matching the page's content model.
    if request.page.content_model is not None:
        templates.append(u"pages/%s.html" % request.page.content_model)
    templates.append(template)

    extra_context.update({
        'latest_news': BlogPost.objects.published(for_user=request.user).filter(event=False).order_by('-created').first(),
        'upcoming_event': BlogPost.objects.published(for_user=request.user).filter(event=True).order_by('-created').first(),
        'link_list': LinkResource.objects.filter(page=request.page).filter(status=LinkResource.PUBLISHED).all(),
    })
    return TemplateResponse(request, templates, extra_context)


@requires_csrf_token
def page_not_found(request, exception, template_name="errors/404.html"):
    """
    Mimics Django's 404 handler but with a different template path.
    """
    exception_repr = exception.__class__.__name__
    # Try to get an "interesting" exception message, if any (and not the ugly
    # Resolver404 dictionary)
    try:
        message = exception.args[0]
    except (AttributeError, IndexError):
        pass
    else:
        if isinstance(message, six.text_type):
            exception_repr = message

    context = {
        "STATIC_URL": settings.STATIC_URL,
        "request_path": request.path,
        "exception": exception_repr,
    }
    t = get_template(template_name)
    return HttpResponseNotFound(t.render(context, request))
