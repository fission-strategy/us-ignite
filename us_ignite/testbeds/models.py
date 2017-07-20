from django.core.urlresolvers import reverse
from django.db import models

from us_ignite.common.fields import URL_HELP_TEXT
from us_ignite.testbeds import managers

from geoposition.fields import GeopositionField
from django_extensions.db.fields import (
    AutoSlugField, CreationDateTimeField, ModificationDateTimeField)
from taggit.managers import TaggableManager


class NetworkSpeed(models.Model):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', unique=True)

    def __unicode__(self):
        return self.name


class Testbed(models.Model):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    EXPERIMENTATION_CHOICES = (
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    )
    PUBLISHED = 1
    DRAFT = 2
    STATUS_CHOICES = (
        (PUBLISHED, 'Published'),
        (DRAFT, 'Draft'),
    )
    name = models.CharField(
        max_length=255, verbose_name='Name of the Testbed')
    slug = AutoSlugField(populate_from='name', unique=True)
    summary = models.TextField(blank=True)
    description = models.TextField()
    contact = models.ForeignKey(
        'profiles.User', blank=True, null=True, on_delete=models.SET_NULL)
    organization = models.ForeignKey(
        'organizations.Organization', blank=True, null=True,
        on_delete=models.SET_NULL)
    website = models.URLField(
        max_length=500, blank=True, help_text=URL_HELP_TEXT)
    image = models.ImageField(blank=True, upload_to='testbed', max_length=500)
    network_speed = models.ForeignKey(
        'testbeds.NetworkSpeed', blank=True, null=True,
        on_delete=models.SET_NULL)
    connections = models.TextField(
        blank=True, verbose_name='Connections to other networks')
    experimentation = models.IntegerField(
        choices=EXPERIMENTATION_CHOICES, default=MEDIUM,
        verbose_name='Willingness to experiment')
    passes_homes = models.PositiveIntegerField(
        default=0, verbose_name='Estimated passes # homes')
    passes_business = models.PositiveIntegerField(
        default=0, verbose_name='Estimated passes # business')
    passes_anchor = models.PositiveIntegerField(
        default=0, verbose_name='Estimated passes # community anchor')
    is_advanced = models.BooleanField(
        default=False, help_text='Does it have advanced characteristics?')
    hubs = models.ManyToManyField(
        'hubs.Hub', blank=True, verbose_name='Communities')
    applications = models.ManyToManyField(
        'apps.Application', blank=True, verbose_name='Applications being '
        'piloted')
    programs = models.ManyToManyField('programs.Program', blank=True, help_text='Does this testbed belong to any program(s)?')
    features = models.ManyToManyField(
        'apps.Feature', blank=True, help_text='Existing NextGen features in '
        'this community.')
    position = GeopositionField(blank=True)
    tags = TaggableManager(blank=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=DRAFT)
    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    # Managers:
    objects = models.Manager()
    active = managers.TestbedActiveManager()

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('testbed_detail', args=[self.slug])

    def get_edit_url(self):
        return reverse('admin:testbeds_testbed_change', args=[self.pk])

    def is_contact(self, user):
        return self.contact == user

    def is_published(self):
        return self.status == self.PUBLISHED

    def is_draft(self):
        return self.status == self.DRAFT

    def is_visible_by(self, user):
        return self.is_published() or self.is_contact(user)

    def is_editable_by(self, user):
        """Only editable in the admin section."""
        return user and user.is_superuser
