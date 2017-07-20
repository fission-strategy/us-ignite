import shortuuid

from django.db import models


# from south.modelsinspector import add_introspection_rules

URL_HELP_TEXT = 'Please enter a URL starting with http or https'
IMAGE_HELP_TEXT = 'Image suggested ratio: 3:2'


class AutoUUIDField(models.SlugField):
    """Generates an automatic short UUID field."""
    description = "An automatic short UUID field."

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('blank', True)
        kwargs.setdefault('editable', False)
        super(AutoUUIDField, self).__init__(*args, **kwargs)

    def _get_uuid(self):
        return shortuuid.uuid()

    def get_queryset(self, model_cls, slug_field):
        print(model_cls)
        # for field, model in model_cls._meta.get_fields_with_model():
        #     if model and field == slug_field:
        #         return model._default_manager.all()
        return model_cls._default_manager.all()

    def create_slug(self, model_instance, add):
        """Creates a unique shortuuid field."""
        slug = self._get_uuid()
        slug_field = model_instance._meta.get_field(self.attname)
        queryset = self.get_queryset(model_instance.__class__, slug_field)
        if model_instance.pk:
            queryset = queryset.exclude(pk=model_instance.pk)
        kwargs = {self.attname: slug}
        # Keep generating uuids until one found is free:
        while not slug or queryset.filter(**kwargs):
            slug = self._get_uuid()
            kwargs[self.attname] = slug
        return slug

    def pre_save(self, model_instance, add):
        # Get value from the current instance:
        value = getattr(model_instance, self.attname)
        if not value:
            value = self.create_slug(model_instance, add)
        setattr(model_instance, self.attname, value)
        return value

    def get_internal_type(self):
        return "SlugField"

# add_introspection_rules([], ["^us_ignite\.common\.fields\.AutoUUIDField"])
