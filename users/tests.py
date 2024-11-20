from django.test import TestCase
from django.contrib.auth.models import User
# from tasks.models import Task
# from statuses.models import Status


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


class UserPermissionsCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        user1 = User.objects.create(username=USERNAME)
        user1.set_password(PASSWORD)
        user1.save()

        user2_id = 2
        user2 = User.objects.create(username=USERNAME2,
                                    id=user2_id)
        user2.set_password(PASSWORD2)
        user2.save()

    def login(self):
        self.client.login(username=USERNAME, password=PASSWORD)
        return User.objects.get(username=USERNAME)

    def test_logged_out_access(self):
        response = self.client.get('/tasks/', follow=True)
        self.assertRedirects(response, '/login/?next=/tasks/')

    def test_update_other_user(self):
        self.login()
        user2_id = User.objects.get(username=USERNAME2).id
        response = self.client.get(f'/users/{user2_id}/update/', follow=True)
        self.assertRedirects(response, '/users/')

    # def test_delete_other_task(self):
    # definetely need fixtures for this (users, status, task)
