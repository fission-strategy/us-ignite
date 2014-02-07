import mailchimp

from mock import patch
from nose.tools import eq_, ok_

from django.test import TestCase

from us_ignite.common.tests import utils
from us_ignite.mailinglist import views


class TestMailingSubscribeView(TestCase):

    def test_get_request_is_successful(self):
        request = utils.get_request('get', '/subscribe/')
        response = views.mailing_subscribe(request)
        eq_(response.status_code, 200)
        eq_(response.template_name, 'mailinglist/form.html')
        eq_(sorted(response.context_data.keys()), ['form'])

    def test_invalid_post_request_fails(self):
        request = utils.get_request('post', '/subscribe/', data={'email': ''})
        response = views.mailing_subscribe(request)
        eq_(response.status_code, 200)
        ok_(response.context_data['form'].errors)

    @patch('us_ignite.mailinglist.views.subscribe_email')
    def test_valid_post_request_is_successful(self, mock_subscribe):
        request = utils.get_request(
            'post', '/subscribe/', data={'email': 'user@us-ignite.org'})
        request._messages = utils.TestMessagesBackend(request)
        response = views.mailing_subscribe(request)
        eq_(response.status_code, 302)
        eq_(response['Location'], '/subscribe/')
        mock_subscribe.assert_called_once_with('user@us-ignite.org')

    @patch('us_ignite.mailinglist.views.subscribe_email')
    def test_subscribed_email_returns_error(self, mock_subscribe):
        mock_subscribe.side_effect = mailchimp.ListAlreadySubscribedError
        request = utils.get_request(
            'post', '/subscribe/', data={'email': 'user@us-ignite.org'})
        request._messages = utils.TestMessagesBackend(request)
        response = views.mailing_subscribe(request)
        eq_(response.status_code, 302)
        eq_(response['Location'], '/subscribe/')
        mock_subscribe.assert_called_once_with('user@us-ignite.org')
