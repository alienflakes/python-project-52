from django.test import TestCase
from django.contrib.auth.models import User
from .models import Status


NAME1 = 'status1'
NAME2 = 'status2'
NAME3 = 'status3'
SUCCESS_URL = '/statuses/'


class StatusCRUDCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        Status.objects.create(name=NAME2)
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()

    def setUp(self):
        self.id = Status.objects.get(name=NAME2).id
        return self.client.login(username='testuser', password='12345')

    def test_status_create(self):
        response = self.client.post('/statuses/create/',
                                    {'name': NAME1}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Status.objects.get(name=NAME1))
        self.assertRedirects(response, SUCCESS_URL)

    def test_status_update(self):
        response = self.client.post(f'/statuses/{self.id}/update/',
                                    {'name': NAME3},
                                    follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, SUCCESS_URL)
        status = Status.objects.get(id=self.id)
        self.assertEqual(status.name, NAME3)

    def test_status_delete(self):
        response = self.client.post(f'/statuses/{self.id}/delete/',
                                    follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, SUCCESS_URL)
        self.assertFalse(Status.objects.filter(id=self.id).exists())
