from django.test import TestCase

from authentication.models import User

from faker import Faker


class TestSetup(TestCase):
    def setUp(self):
        print('Test started')

        self.faker = Faker()
        self.password = self.faker.paragraph(nb_sentences=5)

        self.user = {
            'username': self.faker.name().split(" ")[0],
            'email': self.faker.email(),
            'password': self.password,
            'password2': self.password,
        }
        #return super().setUp()

    def create_test_user(self):
        user = User.objects.create(username='username', email='email@gmail.com')
        user.set_password('123456')
        user.save()
        return user

    def create_test_user_two(self):
        user = User.objects.create(username='username2', email='email2@gmail.com')
        user.set_password('123456')
        user.save()
        return user

    def tearDown(self):
        print("Test finished")
        return super().tearDown()