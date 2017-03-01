from django.db import models
from django.contrib.auth.models import AbstractUser
from us_ignite.common.fields import URL_HELP_TEXT
from django_extensions.db.fields import AutoSlugField
from us_ignite.profiles import managers
from django.core.urlresolvers import reverse


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

    category = models.ForeignKey(
        'blog.BlogCategory', blank=True, null=True,
        verbose_name=u'I associate most with',
        related_name='provile_category')
    category_other = models.ManyToManyField('blog.BlogCategory', blank=True,
                                            verbose_name=u'Other categories I associate with',
                                            related_name='profile_category_other')
    is_public = models.BooleanField(default=False,
                                    help_text='By marking the profile as public it will be shown in search results.',
                                    )

    # created = CreationDateTimeField()
    # modified = ModificationDateTimeField()
    #
    #
    # location = models.CharField(max_length=30, blank=True)
    # birth_date = models.DateField(null=True, blank=True)

    # managers
    objects = models.Manager()
    active = managers.ProfileActiveManager()

    def __unicode__(self):
        return u'Profile for %s' % self.user

    def get_absolute_url(self):
        return reverse('profile_detail', args=[self.slug])

    def get_delete_url(self):
        return reverse('user_profile_delete')

    def get_contact_url(self):
        return reverse('contact_user', args=[self.slug])

    @property
    def name(self):
        if self.first_name or self.last_name:
            name = self.first_name
            if self.first_name and self.last_name:
                name += u' '
            name += self.last_name
            return name
        return u''

    @property
    def full_name(self):
        return self.name

    @property
    def display_name(self):
        return self.name if self.name else u'US Ignite user'

    @property
    def display_email(self):
        return u'%s <%s>' % (self.display_name, self.email)

    def get_gravatar_url(self, size=276):
        """Determines gravatar icon url"""
        username = self.username
        return u'//www.gravatar.com/avatar/%s?s=%s' % (username, size)

    def is_owned_by(self):
        return self


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
