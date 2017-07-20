

from django.db import models
from django.utils.translation import ugettext_lazy as _

from mezzanine.utils.models import upload_to
from mezzanine.core.fields import FileField, RichTextField


class FundingPartner(models.Model):
    DRAFT = 1
    PUBLISHED = 2
    REMOVED = 3
    STATUS_CHOICES = (
        (PUBLISHED, 'Published'),
        (DRAFT, 'Draft'),
        (REMOVED, 'Removed'),
    )
    program = models.ForeignKey('programs.Program', related_name='program_funding_partner_set')
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
    name = models.CharField(max_length=255)
    image = FileField(_("File"), max_length=255, format="Image",
        upload_to=upload_to("sections.Sponsor.image", "galleries"))
    link = models.URLField(blank=True, null=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=DRAFT)

    class Meta(object):
        ordering = ('order', )

    def __unicode__(self):
        return self.name


class Link(models.Model):
    DRAFT = 1
    PUBLISHED = 2
    REMOVED = 3
    STATUS_CHOICES = (
        (PUBLISHED, 'Published'),
        (DRAFT, 'Draft'),
        (REMOVED, 'Removed'),
    )
    program = models.ForeignKey('programs.Program', related_name='program_link_set')
    name = models.CharField(max_length=255)
    url = models.URLField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=DRAFT)

    def __unicode__(self):
        return self.name


class Program(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100, unique=True)
    logo = FileField(_("Logo"), max_length=255, format="Image",
        upload_to=upload_to("programs.Program.logo", "program"), null=True, blank=True)
    background_image = FileField(_("Background Image"), max_length=255, format="Image",
        upload_to=upload_to("programs.Program.background_image", "program"), null=True, blank=True)
    facts_background = FileField(_("Facts Background"), max_length=255, format="Image",
        upload_to=upload_to("programs.Program.facts_background", "program"), null=True, blank=True)
    display_facts = models.BooleanField(default=True)
    about_desc = RichTextField(_("About description"), blank=True, null=True)
    intro_desc = RichTextField(_("Intro description"), blank=True, null=True)
    application_terminology = models.CharField(max_length=255, default='application')
    accent_color = models.CharField(max_length=7, default='#EE7422')
    default = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.default:
            try:
                temp = Program.objects.get(default=True)
                if self != temp:
                    temp.default = False
                    temp.save()
            except Program.DoesNotExist:
                pass
        super(Program, self).save(*args, **kwargs)
