from django.test import TestCase
from django.contrib.auth.models import User


USERNAME = 'vince69'
NEW_USERNAME = 'JELLY_FOX'
FIRST_NAME = 'Noel'
LAST_NAME = 'Fielding'
PASSWORD = 'pinkcrow'

USERNAME2 = '2theMoon'
PASSWORD2 = 'ihatejazz'


class UserCRUDCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username=USERNAME)
        user.set_password(PASSWORD)
        user.save()

    def login(self):
        self.client.login(username=USERNAME, password=PASSWORD)
        return User.objects.get(username=USERNAME)

    def test_user_create(self):
        response = self.client.post('/users/create/', {
            'username': USERNAME2,
            'password1': PASSWORD2,
            'password2': PASSWORD2
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, '/login/')
        self.assertTrue(User.objects.filter(username=USERNAME2).exists())

    def test_user_update(self):
        user = self.login()

        response = self.client.post(f'/users/{user.id}/update/', {
            'username': NEW_USERNAME,
            'first_name': FIRST_NAME,
            'last_name': LAST_NAME,
            'password1': PASSWORD,
            'password2': PASSWORD
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, '/users/')

        user = User.objects.get(username=NEW_USERNAME)
        self.assertEqual(user.first_name, FIRST_NAME)
        self.assertEqual(user.last_name, LAST_NAME)

    def test_user_delete(self):
        user = self.login()

        response = self.client.post(f'/users/{user.id}/delete/',
                                    follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, '/users/')
        self.assertFalse(User.objects.filter(username=USERNAME).exists())
