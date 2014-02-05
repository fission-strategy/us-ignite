from django.db import models


class ResourcePublishedManager(models.Manager):

    def get_query_set(self, *args, **kwargs):
        return (super(ResourcePublishedManager, self)
                .get_query_set(*args, **kwargs)
                .filter(status=self.model.PUBLISHED))

    def get_featured(self):
        try:
            return (self.get_query_set().filter(is_featured=True)
                    .order_by('-is_featured', '-created')[0])
        except IndexError:
            return None
