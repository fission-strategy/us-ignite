from django.db import models
from django.contrib.auth.models import AbstractUser
from us_ignite.common.fields import URL_HELP_TEXT
from django_extensions.db.fields import AutoSlugField

from django.contrib import admin


class User(AbstractUser):
    NO_AVAILABILITY = 0
    LIMITED_AVAILABILITY = 1
    MODERATE_AVAILABILITY = 2
    HIGH_AVAILABILITY = 3
    AVAILABILITY_CHOICES = (
        (NO_AVAILABILITY, u'I do not have any availability at this time'),
        (LIMITED_AVAILABILITY, u'I have limited availability'),
        (MODERATE_AVAILABILITY, u'I might be available'),
        (HIGH_AVAILABILITY, u'Yes, I would love to join a project'),
    )
    slug = AutoSlugField(
        unique=True, populate_from='username', editable=True,
        help_text=u'Slug used for your profile. Recommended FirstName-LastName')
    avatar = models.ImageField(
        upload_to="avatar", blank=True, max_length=500,
        help_text=u'Select image to use as avatar. If an image is not '
        'provided Gravatar will be used.')
    website = models.URLField(
        max_length=500, blank=True, help_text=URL_HELP_TEXT)
    quote = models.TextField(
        blank=True, max_length=140, help_text=u'Short quote.')
    bio = models.TextField(blank=True)
    skills = models.TextField(
        blank=True, help_text=u'What do you have to contribute? '
                              'Design skills? Programming languages? Subject matter expertise?'
                              ' Project management experience?')
    availability = models.IntegerField(
        choices=AVAILABILITY_CHOICES, default=NO_AVAILABILITY)
    interests = models.ManyToManyField('profiles.Interest', blank=True)
    interests_other = models.CharField(blank=True, max_length=255)

    # created = CreationDateTimeField()
    # modified = ModificationDateTimeField()
    #
    #
    # location = models.CharField(max_length=30, blank=True)
    # birth_date = models.DateField(null=True, blank=True)


class Interest(models.Model):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name', )


class ProfileLink(models.Model):
    profile = models.ForeignKey('profiles.User')
    name = models.CharField(blank=True, max_length=255)
    url = models.URLField(
        max_length=500, help_text=URL_HELP_TEXT, verbose_name=u'URL')

    def __unicode__(self):
        return u'Profile link.'

    @models.permalink
    def get_absolute_url(self):
        return self.url
