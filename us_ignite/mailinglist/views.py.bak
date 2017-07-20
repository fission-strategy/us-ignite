import hashlib
import logging
import mailchimp

from django.contrib import messages
# from django.conf import settings
from django.shortcuts import redirect
from django.template.response import TemplateResponse

from us_ignite.mailinglist.forms import EmailForm
from us_ignite.singletons.models import MailChimp

logger = logging.getLogger('us_ignite.mailinglist.views')


def subscribe_email(form_data, slug):
    settings = MailChimp.objects.get()

    MAILING_LISTS = {
        'default': settings.main_list,
    }

    if not slug in MAILING_LISTS:
        raise mailchimp.ValidationError('Error while subscribing.')

    master = mailchimp.Mailchimp(settings.api_key)

    mailing_list = mailchimp.Lists(master)
    uid = hashlib.md5(form_data['email']).hexdigest()
    email_data = {
        'email': form_data['email'],
        'euid': uid,
        'leid': uid,
    }
    return mailing_list.subscribe(settings.main_list, email_data)


def mailing_subscribe(request, slug='default'):
    """Handles MailChimp email registration."""
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            try:
                subscribe_email(form.cleaned_data, slug)
                messages.success(request, 'Successfully subscribed.')
                redirect_to = 'home'
            except mailchimp.ListAlreadySubscribedError:
                messages.error(request, 'Already subscribed.')
                redirect_to = 'mailing_subscribe'
            except mailchimp.ValidationError, e:
                messages.error(request, 'ERROR: %s' % e.args[0])
                redirect_to = 'mailing_subscribe'
            return redirect(redirect_to)
    else:
        form = EmailForm()
    context = {
        'form': form,
    }
    return TemplateResponse(request, 'mailinglist/form.html', context)
