from django.test import TestCase
from django.contrib.auth.models import User
from tasks.models import Task
from statuses.models import Status


def login_user1(self):
    user = User.objects.get(id=1)
    self.client.force_login(user)
    return user


class UserCRUDCase(TestCase):

    fixtures = ['user1.json']

    def test_user_create(self):
        username = '2theMoon'
        password = 'ihatejazz'
        response = self.client.post('/users/create/', {
            'username': username,
            'password1': password,
            'password2': password
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, '/login/')
        self.assertTrue(User.objects.filter(username=username).exists())

    def test_user_update(self):
        user = login_user1(self)
        new_username = 'JELLY_FOX'
        first_name = 'Noel'
        last_name = 'Fielding'
        password = 'pinkcrow'

        response = self.client.post(f'/users/{user.id}/update/', {
            'username': new_username,
            'first_name': first_name,
            'last_name': last_name,
            'password1': password,
            'password2': password
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, '/users/')

        user = User.objects.get(username=new_username)
        self.assertEqual(user.first_name, first_name)
        self.assertEqual(user.last_name, last_name)

    def test_user_delete(self):
        user = login_user1(self)

        response = self.client.post(f'/users/{user.id}/delete/',
                                    follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, '/users/')
        self.assertFalse(User.objects.filter(id=user.id).exists())


class UserPermissionsCase(TestCase):

    fixtures = ['user1.json', 'user2.json']

    def test_logged_out_access(self):
        # accessing other pages (/statuses, /labels) would get the same result
        # because they import this access mixin from tasks/views.py
        response = self.client.get('/tasks/', follow=True)
        self.assertRedirects(response, '/login/?next=/tasks/')

    def test_update_other_user(self):
        login_user1(self)
        response = self.client.get('/users/2/update/', follow=True)
        self.assertRedirects(response, '/users/')

    def test_delete_other_task(self):
        task = Task.objects.create(
            name='task1',
            status=Status.objects.create(name='test_status'),
            creator=User.objects.get(id=2)
        )
        login_user1(self)
        response = self.client.get(f'/tasks/{task.id}/delete/')
        self.assertRedirects(response, '/tasks/')
        self.assertTrue(Task.objects.filter(id=1).exists())
