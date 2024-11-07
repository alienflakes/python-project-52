from django.test import TestCase
from django.contrib.auth.models import User


USERNAME = 'vince69'
NEW_USERNAME = 'JELLY_FOX'
FIRST_NAME = 'Noel'
LAST_NAME = 'Fielding'
PASSWORD = 'pinkcrow'


def create_user(self):
    return self.client.post('/users/create/', {
        'username': USERNAME,
        'password1': PASSWORD,
        'password2': PASSWORD
    })


def set_up(self):
    create_user(self)
    return self.client.post('/login/', {
        'username': USERNAME,
        'password': PASSWORD
    })


class UserCreateCase(TestCase):

    def test_user_create(self):
        response = create_user(self)
        self.assertTrue(User.objects.get(username=USERNAME))
        self.assertRedirects(response, '/login/')


class UserUpdateCase(TestCase):

    def test_user_update(self):

        set_up(self)
        user = User.objects.get(username=USERNAME)

        response = self.client.post(f'/users/{user.id}/update/', {
            'username': NEW_USERNAME,
            'first_name': FIRST_NAME,
            'last_name': LAST_NAME,
            'password': PASSWORD
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, '/users/')

        user = User.objects.get(username=NEW_USERNAME)
        self.assertEqual(user.first_name, FIRST_NAME)
        self.assertEqual(user.last_name, LAST_NAME)


class UserDeleteCase(TestCase):

    def test_user_delete(self):

        set_up(self)
        user = User.objects.get(username=USERNAME)

        response = self.client.post(f'/users/{user.id}/delete/',
                                    follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, '/users/')
        self.assertFalse(User.objects.filter(username=USERNAME).exists())
