from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.models import Site
from django.contrib.sites.requests import RequestSite

from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.views.generic.base import TemplateView
from django.contrib.sites.shortcuts import get_current_site


from registration import signals
from registration.backends.model_activation import views as registration_views
from registration.models import RegistrationProfile
from registration.views import ActivationView as BaseActivationView
from registration.forms import RegistrationForm


from us_ignite.apps.models import Application
from us_ignite.common import decorators
from us_ignite.events.models import Event
from us_ignite.profiles import forms
from us_ignite.profiles.models import User as Profile
from us_ignite.resources.models import Resource


class USICustomUserForm(RegistrationForm):
    class Meta:
        model = Profile

        fields = [
            Profile.USERNAME_FIELD,
            'email',
            'password1',
            'password2'
        ]
        required_css_class = 'required'


class EmailRegistrationView(registration_views.RegistrationView):
    """
    Register a new (inactive) user account, generate and store an
    activation key, and email it to the user.

    """
    def register(self, form):
        new_user = RegistrationProfile.objects.create_inactive_user(
            form,
            site=get_current_site(self.request)
        )
        signals.user_registered.send(sender=self.__class__,
                                     user=new_user,
                                     request=self.request)
        return new_user


class ActivationView(BaseActivationView):

    def activate(self, request, activation_key):
        """
        Given an an activation key, look up and activate the user
        account corresponding to that key (if possible).

        After successful activation, the signal
        ``registration.signals.user_activated`` will be sent, with the
        newly activated ``User`` as the keyword argument ``user`` and
        the class of this backend as the sender.
        """
        activated_user = RegistrationProfile.objects.activate_user(activation_key)
        return activated_user

    def get_success_url(self, request, user):
        return 'registration_activation_complete', (), {}


# Registration views:
# Using function aliases for lazy loadind and readability in the urls file.
registration_view = decorators.not_auth_required(
    EmailRegistrationView.as_view(form_class=USICustomUserForm))
registration_activation_complete = TemplateView.as_view(
    template_name='registration/activation_complete.html')
# Using local ``Activation`` view to avoid sending duplicate
# user_activated signals:
registration_activate = ActivationView.as_view()
registration_complete = TemplateView.as_view(
    template_name='registration/registration_complete.html')
registration_disallowed = TemplateView.as_view(
    template_name='registration/registration_closed.html')


@login_required
def user_profile(request):
    """Edit the ``User`` owned ``Profile``."""
    # Make sure the user has a profile:
    profile, is_new = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = forms.ProfileForm(request.POST, request.FILES, instance=profile)
        formset = forms.ProfileLinkFormSet(request.POST, instance=profile)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            messages.success(request, 'Thank you for updating your Profile.')
            return redirect('user_profile')
    else:
        form = forms.ProfileForm(instance=profile, initial={
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'username': request.user.username,
        })
        formset = forms.ProfileLinkFormSet(instance=profile)
    context = {
        'object': profile,
        'form': form,
        'formset': formset,
    }
    return TemplateResponse(request, 'profile/user_profile.html', context)


@login_required
def user_profile_delete(request):
    """Removes the authenticated ``User`` details."""
    # List of the content to be disassociated:
    application_list = Application.objects.filter(owner=request.user)
    event_list = Event.objects.filter(user=request.user)
    resource_list = Resource.objects.filter(contact=request.user)
    if request.method == 'POST':
        request.user.delete()
        # Logut user
        logout(request)
        msg = 'Your account and all associated data has been removed.'
        messages.success(request, msg)
        return redirect('home')
    context = {
        'application_list': application_list,
        'event_list': event_list,
        'resource_list': resource_list,
    }
    return TemplateResponse(
        request, 'profile/user_profile_delete.html', context)