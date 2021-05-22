from django.test import TestCase

from todo.models import Todo
from authentication.models import User

from utils.setup_test import TestSetup


class TestModel(TestSetup):

    def test_should_create_todo(self):
        user = self.create_test_user()

        todo = Todo(title="Buy milk", description='get it done', owner=user)
        todo.save()

        self.assertEqual(str(todo), 'Buy milk')
