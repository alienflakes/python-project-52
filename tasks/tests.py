from django.test import TestCase
from django.contrib.auth.models import User
from .models import Task
from statuses.models import Status


NAME1 = 'task1'
NAME2 = 'task2'
NAME3 = 'task3'
STATUS = 'wow'


class TaskCRUDCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        status = Status.objects.create(name=STATUS)
        Task.objects.create(name=NAME2, creator=user, status=status)

    def setUp(self):
        self.task_id = Task.objects.get(name=NAME2).id
        return self.client.login(username='testuser', password='12345')

    def test_task_create(self):
        response = self.client.post('/tasks/create/',
                                    {'name': NAME1,
                                     'status': [1]}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Task.objects.filter(name=NAME1).exists())

    def test_task_update(self):
        response = self.client.post(f'/tasks/{self.task_id}/update/',
                                    {'name': NAME3,
                                     'status': [1]},
                                    follow=True)
        self.assertEqual(response.status_code, 200)
        task = Task.objects.get(id=self.task_id)
        self.assertEqual(task.name, NAME3)

    def test_task_delete(self):
        response = self.client.post(f'/tasks/{self.task_id}/delete/',
                                    follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Task.objects.filter(id=self.task_id).exists())
