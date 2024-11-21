from django.test import TestCase
from users.tests import login_user1
from .models import Label


SUCCESS_URL = '/labels/'


class LabelCRUDCase(TestCase):

    fixtures = ['label.json',
                'users/fixtures/user1.json']

    def setUp(self):
        return login_user1(self)

    def test_label_create(self):
        name = 'backend'
        response = self.client.post('/labels/create/',
                                    {'name': name},
                                    follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Label.objects.get(name=name))
        self.assertRedirects(response, SUCCESS_URL)

    def test_label_update(self):
        new_name = 'UI'
        response = self.client.post('/labels/1/update/',
                                    {'name': new_name},
                                    follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, SUCCESS_URL)
        label = Label.objects.get(id=1)
        self.assertEqual(label.name, new_name)

    def test_label_delete(self):
        response = self.client.post('/labels/1/delete/',
                                    follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, SUCCESS_URL)
        self.assertFalse(Label.objects.filter(id=1).exists())
