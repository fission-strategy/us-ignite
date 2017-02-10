from django.db import models

class SiteAlert(models.Model):

    message = models.TextField(blank=True)

    # Make the plural name singular, to correctly
    # label it in the admin interface.
    class Meta:
        verbose_name_plural = "Site Alert"