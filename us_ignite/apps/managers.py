from django.db import models


class ApplicationActiveManager(models.Manager):

    def get_query_set(self):
        return (super(ApplicationActiveManager, self).get_query_set()
                .filter(~models.Q(status=self.model.REMOVED)))


class ApplicationPublishedManager(models.Manager):

    def get_query_set(self):
        return (super(ApplicationPublishedManager, self).get_query_set()
                .filter(status=self.model.PUBLISHED))


class ApplicationVersionManager(models.Manager):

    def create_version(self, application):
        """Generates an ``ApplicationVersion`` of the given ``application``."""
        data = {
            'application': application,
            'name': application.name,
            'stage': application.stage,
            'website': application.website,
            'image': application.image,
            'summary': application.summary,
            'impact_statement': application.impact_statement,
            'description': application.description,
            'roadmap': application.roadmap,
            'assistance': application.assistance,
            'team_description': application.team_description,
            'acknowledgments': application.acknowledgments,
            'notes': application.notes,
        }
        return self.create(**data)

    def get_latest_version(self, application):
        results = self.filter(application=application).order_by('-created')
        if results:
            return results[0]
        return None
