from django.test import TestCase
from django.contrib.auth.models import User
from users.tests import login_user1
from .models import Task
from statuses.models import Status


class TaskCRUDCase(TestCase):
    # should probably add testing labels and executors later

    fixtures = ['users/fixtures/user1.json']

    @classmethod
    def setUpTestData(cls):
        status = Status.objects.create(id=1,
                                       name='wow')
        Task.objects.create(id=1,
                            name='do stuff',
                            creator=User.objects.get(id=1),
                            status=status)

    def setUp(self):
        return login_user1(self)

    def test_task_create(self):
        name = 'take a break'
        response = self.client.post('/tasks/create/',
                                    {'name': name,
                                     'status': [1]},
                                    follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Task.objects.filter(name=name).exists())

    def test_task_update(self):
        new_name = 'get help'
        response = self.client.post('/tasks/1/update/',
                                    {'name': new_name,
                                     'status': [1]},
                                    follow=True)
        self.assertEqual(response.status_code, 200)
        task = Task.objects.get(id=1)
        self.assertEqual(task.name, new_name)

    def test_task_delete(self):
        response = self.client.post('/tasks/1/delete/',
                                    follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Task.objects.filter(id=1).exists())
