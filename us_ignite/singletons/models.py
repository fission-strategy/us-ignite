from django.db import models


class SiteAlert(models.Model):

    message = models.TextField(blank=True)

    # Make the plural name singular, to correctly
    # label it in the admin interface.
    class Meta:
        verbose_name_plural = "Site Alert"


class MailChimp(models.Model):

    api_key = models.CharField(blank=True, max_length=100)
    main_list = models.CharField(blank=True, max_length=100, verbose_name='Main Mailing List')

    def __unicode__(self):
        return self.main_list