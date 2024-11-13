from django.test import TestCase
from django.contrib.auth.models import User
from .models import Label


NAME1 = 'label1'
NAME2 = 'label2'
NAME3 = 'label3'
SUCCESS_URL = '/labels/'


class LabelCRUDCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        Label.objects.create(name=NAME2)
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()

    def setUp(self):
        self.label_id = Label.objects.get(name=NAME2).id
        return self.client.login(username='testuser', password='12345')

    def test_Label_create(self):
        response = self.client.post('/labels/create/',
                                    {'name': NAME1}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Label.objects.get(name=NAME1))
        self.assertRedirects(response, SUCCESS_URL)

    def test_label_update(self):
        response = self.client.post(f'/labels/{self.label_id}/update/',
                                    {'name': NAME3},
                                    follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, SUCCESS_URL)
        label = Label.objects.get(id=self.label_id)
        self.assertEqual(label.name, NAME3)

    def test_label_delete(self):
        response = self.client.post(f'/labels/{self.label_id}/delete/',
                                    follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, SUCCESS_URL)
        self.assertFalse(Label.objects.filter(id=self.label_id).exists())
