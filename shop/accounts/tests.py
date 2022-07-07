from urllib import response
from django.test import TestCase, Client
from django.urls import reverse
from django.db.models import QuerySet
from requests import request
from accounts.views import login
from django.contrib.auth import get_user_model



User = get_user_model()


class LoginPagesTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        

    def setUp(self):
        self.user = User.objects.create_user(username='StasBasov', password='12345')
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)    

    def test_about_page_uses_correct_template(self):
        """URL-адрес использует шаблон accounts/login.html."""
        response = self.authorized_client.get(reverse('login'))
        self.assertTemplateUsed(response, 'accounts/login.html')

    def test_home_page_correct_template(self):
        """URL-адрес использует шаблон includs/base.html."""
        response = self.authorized_client.get(reverse('login'))
        self.assertTemplateUsed(response, 'includs/base.html')

    def test_task_list_page_authorized_uses_correct_template(self):
        """URL-адрес использует шаблон includs/messages.html."""
        response = self.authorized_client.get(reverse('login'))
        self.assertTemplateUsed(response, 'includs/messages.html')

   







       

