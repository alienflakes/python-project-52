from django.test import TestCase
from users.tests import login_user1
from .models import Status


SUCCESS_URL = '/statuses/'


class StatusCRUDCase(TestCase):

    fixtures = ['status.json',
                'users/fixtures/user1.json']

    def setUp(self):
        return login_user1(self)

    def test_status_create(self):
        name = 'new'
        response = self.client.post('/statuses/create/',
                                    {'name': name}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Status.objects.get(name=name))
        self.assertRedirects(response, SUCCESS_URL)

    def test_status_update(self):
        new_name = 'finished'
        response = self.client.post('/statuses/1/update/',
                                    {'name': new_name},
                                    follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, SUCCESS_URL)
        status = Status.objects.get(id=1)
        self.assertEqual(status.name, new_name)

    def test_status_delete(self):
        response = self.client.post('/statuses/1/delete/',
                                    follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, SUCCESS_URL)
        self.assertFalse(Status.objects.filter(id=1).exists())
