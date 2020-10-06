from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import Group
from django.test.utils import tag
from io import BytesIO
from PIL import Image
from random import randint

from .models import Book
from ..users.models import User


class BookViewTestCase(APITestCase):
    uri = '/api/books/'

    @staticmethod
    def create_test_image():
        file = BytesIO()
        image = Image.new('RGBA', size=(50, 50), color=(randint(0, 256), randint(0, 256), randint(0, 256)))
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)
        return file

    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(title="Test",
                                       genre="F",
                                       price=12.99,
                                       author="Test Test",
                                       release_date="2019-11-13",
                                       description="Test")

        cls.admin_group = Group.objects.create(name="admin")

        cls.user = User.objects.create(username="Test_admin",
                                       password="Test_admin1234",
                                       email="Test_admin@test.pl",
                                       groups=cls.admin_group)

        cls.token = Token.objects.create(user=cls.user)

    def setUp(self):
        method = getattr(self, self._testMethodName)
        tags = getattr(method, 'tags', {})
        if 'skip_setup' not in tags:
            self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token}")

# Tests

    @tag('skip_setup')
    def test_book_list_GET(self):
        response = self.client.get(self.uri)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), 1)

    @tag('skip_setup')
    def test_book_retrieve_GET(self):
        response = self.client.get(f'{self.uri}{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'id': self.book.id,
                                         'genre_display': 'Fantasy',
                                         'title': 'Test',
                                         'genre': 'F',
                                         'price': '12.99',
                                         'author': 'Test Test',
                                         'release_date': '2019-11-13',
                                         'description': 'Test',
                                         'cover': None})

    def test_book_POST(self):
        data = {'title': 'Test2',
                'genre': 'B',
                'price': 20.99,
                'author': 'Test2 Test2',
                'release_date': '2020-10-01',
                'description': 'Test2',
                'cover': BookViewTestCase.create_test_image()}

        response = self.client.post(self.uri, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_book_PUT(self):
        data = {'title': 'Test changed',
                'genre': 'F',
                'price': 12.99,
                'author': 'Test Test',
                'release_date': '2019-11-13',
                'description': 'Test',
                'cover': BookViewTestCase.create_test_image()}

        response = self.client.put(f"{self.uri}{self.book.id}/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], data["title"])

    def test_book_PATCH(self):
        data = {"title": "Changed_title"}
        response = self.client.patch(f"{self.uri}{self.book.id}/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], data["title"])

    def test_book_DELETE(self):
        response = self.client.delete(f"{self.uri}{self.book.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
