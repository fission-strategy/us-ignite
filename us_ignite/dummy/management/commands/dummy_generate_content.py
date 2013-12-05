from datetime import timedelta
from random import choice

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils import timezone

from us_ignite.profiles.models import Profile
from us_ignite.apps.models import (Application, Domain, Feature, Page,
                                   PageApplication)
from us_ignite.hubs.models import Hub
from us_ignite.events.models import Event
from us_ignite.dummy import text, images


class Command(BaseCommand):

    domain_list = Domain.objects.all()
    feature_list = Feature.objects.all()

    def _create_users(self):
        users = ['banana', 'apple', 'orange', 'peach']
        for f in users:
            user, is_new = User.objects.get_or_create(username=f, is_active=True)
            if is_new and choice([True, False]):
                bio = text.random_paragraphs(2)
                Profile.objects.create(user=user, name=f, bio=bio)
        return True

    def _get_user(self):
        return User.objects.all().order_by('?')[0]

    def _get_domain(self):
        return choice(self.domain_list)

    def _get_feature(self):
        return choice(self.feature_list)

    def _choice(self, *args):
        return choice([''] + list(args))

    def _create_app(self):
        data = {
            'name': text.random_words(3),
            'stage': choice(Application.STAGE_CHOICES)[0],
            'status': choice(Application.STATUS_CHOICES)[0],
            'website': 'http://%s/' % text.random_words(1),
            'summary': self._choice(text.random_paragraphs(1)),
            'impact_statement': text.random_words(20),
            'description': text.random_paragraphs(4),
            'roadmap': self._choice(text.random_words(30)),
            'assistance': self._choice(text.random_words(30)),
            'team_description': self._choice(text.random_words(30)),
            'acknowledgments': self._choice(text.random_words(30)),
            'domain': self._get_domain(),
            'is_featured': choice([True, False]),
            'owner': self._get_user(),
            'image': images.random_image('%s.png' % text.random_words(1)),
        }
        return Application.objects.create(**data)

    def _create_page(self):
        data = {
            'name': text.random_words(3),
            'status': choice(Application.STATUS_CHOICES)[0],
            'description': text.random_paragraphs(2),
        }
        page = Page.objects.create(**data)
        app_list = (Application.objects
                    .filter(status=Application.PUBLISHED).order_by('?')[:10])
        for i, app in enumerate(app_list):
            PageApplication.objects.create(page=page, application=app, order=i)

    def _get_start_date(self):
        days = choice(range(-5, 50))
        return timezone.now() + timedelta(days=days)

    def _create_hub(self):
        data = {
            'name': text.random_words(3),
            'guardian': choice([None, self._get_user()]),
            'summary': text.random_words(10),
            'description': text.random_paragraphs(3),
            'image': images.random_image('%s.png' % text.random_words(1)),
            'website': 'http://%s/' % text.random_words(1),
            'status': choice(Hub.STATUS_CHOICES)[0],
            'is_featured': choice([True, False]),
        }
        return Hub.objects.create(**data)

    def _get_hub(self):
        return Hub.objects.filter(status=Hub.PUBLISHED).order_by('?')[0]

    def _create_event(self):
        start_date = self._get_start_date()
        end_date = start_date + timedelta(hours=5)
        data = {
            'name': text.random_words(5),
            'status': choice(Event.STATUS_CHOICES)[0],
            'image': images.random_image('%s.png' % text.random_words(1)),
            'start_datetime': start_date,
            'end_datetime': choice([None, end_date]),
            'venue': text.random_words(7),
            'description': text.random_paragraphs(2),
            'is_featured': choice([True, False]),
            'user': self._get_user(),
        }
        event = Event.objects.create(**data)
        for i in range(0, 3):
            event.hubs.add(self._get_hub())
        return event

    def handle(self, *args, **options):
        message = ('This command will IRREVERSIBLE poison the existing '
                   'database by adding dummy content and images. '
                   'Proceed? [y/N] ')
        response = raw_input(message)
        if not response or not response == 'y':
            print 'Phew, aborted!'
            exit(0)
        print u'Adding users'
        self._create_users()
        print u'Generating applications.'
        for i in range(1, 20):
            self._create_app()
        print u'Generating app pages.'
        for i in range(1, 5):
            self._create_page()
        print u'Generating hubs.'
        for i in range(1, 10):
            self._create_hub()
        print u'Generate events'
        for i in range(1, 40):
            self._create_event()
